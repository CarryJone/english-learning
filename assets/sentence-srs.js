(function () {
  const DEFAULT_CONFIG = {
    owner: "CarryJone",
    repo: "english-learning",
    filePath: "vocabulary/sentences.json",
    tokenStorageKey: "github_pat",
    intervals: [1, 3, 7, 14, 30, 60, 90]
  };

  function localYmd(date = new Date()) {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, "0");
    const d = String(date.getDate()).padStart(2, "0");
    return `${y}-${m}-${d}`;
  }

  function addDays(ymd, days) {
    const parts = ymd.split("-").map(Number);
    const date = new Date(parts[0], parts[1] - 1, parts[2]);
    date.setDate(date.getDate() + days);
    return localYmd(date);
  }

  function apiUrl(config = {}) {
    const merged = { ...DEFAULT_CONFIG, ...config };
    return `https://api.github.com/repos/${merged.owner}/${merged.repo}/contents/${merged.filePath}`;
  }

  function readStoredToken(config = {}) {
    const merged = { ...DEFAULT_CONFIG, ...config };
    return localStorage.getItem(merged.tokenStorageKey);
  }

  function storeToken(token, config = {}) {
    const merged = { ...DEFAULT_CONFIG, ...config };
    localStorage.setItem(merged.tokenStorageKey, token);
  }

  function getOrPromptToken(options = {}) {
    const token = readStoredToken(options);
    if (token) return token;

    const message = options.promptMessage || "首次使用句子 SRS：請輸入 GitHub Personal Access Token（repo write 權限，儲存在本機）：";
    const nextToken = prompt(message);
    if (!nextToken) throw new Error("未提供 Token，無法同步");
    storeToken(nextToken, options);
    return nextToken;
  }

  function decodeGithubJson(content) {
    const raw = atob(content.replace(/\n/g, ""));
    const bytes = new Uint8Array(raw.length);
    for (let i = 0; i < raw.length; i += 1) bytes[i] = raw.charCodeAt(i);
    return JSON.parse(new TextDecoder("utf-8").decode(bytes));
  }

  function encodeGithubJson(value) {
    const bytes = new TextEncoder().encode(JSON.stringify(value, null, 2));
    let binary = "";
    bytes.forEach((b) => { binary += String.fromCharCode(b); });
    return btoa(binary);
  }

  async function readRemoteSentenceStore(token, config = {}) {
    const resp = await fetch(apiUrl(config), {
      headers: {
        Authorization: "token " + token,
        Accept: "application/vnd.github.v3+json"
      }
    });
    if (!resp.ok) throw new Error("讀取 sentences.json 失敗 (" + resp.status + ")");
    const fileData = await resp.json();
    return {
      sha: fileData.sha,
      store: decodeGithubJson(fileData.content)
    };
  }

  async function writeRemoteSentenceStore(token, store, sha, message, config = {}) {
    const resp = await fetch(apiUrl(config), {
      method: "PUT",
      headers: {
        Authorization: "token " + token,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message,
        content: encodeGithubJson(store),
        sha
      })
    });
    if (!resp.ok) throw new Error("更新 sentences.json 失敗 (" + resp.status + ")");
    return resp.json();
  }

  function normalizeRating(rating) {
    if (rating === "remembered" || rating === "hinted" || rating === "forgot") return rating;
    return "";
  }

  function applySentenceResults(store, results, options = {}) {
    const today = options.today || localYmd();
    const intervals = options.intervals || DEFAULT_CONFIG.intervals;
    const items = Array.isArray(store.items) ? store.items : [];
    let updatedCount = 0;
    let skippedCount = 0;
    let missingCount = 0;

    for (const result of results) {
      const rating = normalizeRating(result.rating);
      const item = items.find((entry) => entry.id === result.id);
      if (!item || !rating) {
        missingCount += 1;
        continue;
      }
      if (item.lastReviewedDate === today) {
        skippedCount += 1;
        continue;
      }

      item.lastReviewedDate = today;
      if (rating === "remembered") {
        item.reviewCount = (item.reviewCount || 0) + 1;
        const interval = intervals[Math.min(Math.max(item.reviewCount - 1, 0), intervals.length - 1)] || 90;
        item.nextReview = addDays(today, interval);
      } else if (rating === "hinted") {
        item.reviewCount = item.reviewCount || 0;
        item.nextReview = addDays(today, 1);
      } else {
        item.reviewCount = 0;
        item.nextReview = addDays(today, 1);
      }
      item.lastRating = rating;
      updatedCount += 1;
    }

    return { store: { ...store, items }, updatedCount, skippedCount, missingCount };
  }

  function collectContextResults(root = document) {
    return Array.from(root.querySelectorAll(".context-item[data-sentence-id]")).map((item) => ({
      id: item.dataset.sentenceId,
      rating: item.dataset.rating || ""
    }));
  }

  function isAlreadySynced(storagePrefix, today = localYmd()) {
    return Boolean(localStorage.getItem(storagePrefix + today));
  }

  function markSynced(storagePrefix, today = localYmd()) {
    localStorage.setItem(storagePrefix + today, "1");
  }

  async function syncSentenceResults(results, options = {}) {
    const today = options.today || localYmd();
    const storagePrefix = options.storagePrefix || "sentence_srs_done_";
    if (isAlreadySynced(storagePrefix, today)) {
      return { status: "already-synced", today };
    }

    const token = options.token || getOrPromptToken(options);
    const { sha, store } = await readRemoteSentenceStore(token, options);
    const applied = applySentenceResults(store, results, { today, intervals: options.intervals });
    const commitPrefix = options.commitPrefix || "Sentence SRS update";
    await writeRemoteSentenceStore(token, applied.store, sha, `${commitPrefix} ${today}`, options);
    markSynced(storagePrefix, today);
    return {
      status: "synced",
      today,
      updatedCount: applied.updatedCount,
      skippedCount: applied.skippedCount,
      missingCount: applied.missingCount
    };
  }

  window.SentenceSrs = {
    DEFAULT_CONFIG,
    localYmd,
    addDays,
    isAlreadySynced,
    markSynced,
    collectContextResults,
    applySentenceResults,
    syncSentenceResults,
    getOrPromptToken,
    readRemoteSentenceStore,
    writeRemoteSentenceStore
  };
}());
