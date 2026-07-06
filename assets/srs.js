(function () {
  const DEFAULT_CONFIG = {
    owner: "CarryJone",
    repo: "english-learning",
    filePath: "vocabulary/learning.json",
    tokenStorageKey: "github_pat",
    intervals: [1, 3, 7, 14, 30, 60, 90]
  };

  function localYmd(date = new Date()) {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, "0");
    const d = String(date.getDate()).padStart(2, "0");
    return `${y}-${m}-${d}`;
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

    const message = options.promptMessage || "首次使用：請輸入 GitHub Personal Access Token（repo write 權限，儲存在本機）：";
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

  async function readRemoteVocab(token, config = {}) {
    const resp = await fetch(apiUrl(config), {
      headers: {
        Authorization: "token " + token,
        Accept: "application/vnd.github.v3+json"
      }
    });
    if (!resp.ok) throw new Error("讀取 learning.json 失敗 (" + resp.status + ")");
    const fileData = await resp.json();
    return {
      sha: fileData.sha,
      vocab: decodeGithubJson(fileData.content)
    };
  }

  async function writeRemoteVocab(token, vocab, sha, message, config = {}) {
    const resp = await fetch(apiUrl(config), {
      method: "PUT",
      headers: {
        Authorization: "token " + token,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message,
        content: encodeGithubJson(vocab),
        sha
      })
    });
    if (!resp.ok) throw new Error("更新失敗 (" + resp.status + ")");
    return resp.json();
  }

  function applyReviewResults(vocab, results, options = {}) {
    const today = options.today || localYmd();
    const intervals = options.intervals || DEFAULT_CONFIG.intervals;
    const words = Array.isArray(vocab.words) ? vocab.words : [];
    let updatedCount = 0;
    let skippedCount = 0;

    for (const result of results) {
      const word = words.find((item) => item.word === result.word);
      if (!word || word.lastReviewedDate === today) {
        skippedCount += 1;
        continue;
      }

      word.lastReviewedDate = today;
      const next = new Date();
      if (result.correct) {
        word.reviewCount = (word.reviewCount || 0) + 1;
        next.setDate(next.getDate() + (intervals[Math.min(word.reviewCount, intervals.length - 1)] || 90));
      } else {
        word.reviewCount = 0;
        next.setDate(next.getDate() + 1);
      }
      word.nextReview = localYmd(next);
      updatedCount += 1;
    }

    return { vocab, updatedCount, skippedCount };
  }

  function isAlreadySynced(storagePrefix, today = localYmd()) {
    return Boolean(localStorage.getItem(storagePrefix + today));
  }

  function markSynced(storagePrefix, today = localYmd()) {
    localStorage.setItem(storagePrefix + today, "1");
  }

  async function syncReviewResults(results, options = {}) {
    const today = options.today || localYmd();
    const storagePrefix = options.storagePrefix || "rq_done_";
    if (isAlreadySynced(storagePrefix, today)) {
      return { status: "already-synced", today };
    }

    const token = options.token || getOrPromptToken(options);
    const { sha, vocab } = await readRemoteVocab(token, options);
    const applied = applyReviewResults(vocab, results, { today, intervals: options.intervals });
    const commitPrefix = options.commitPrefix || "SRS update: review quiz";
    await writeRemoteVocab(token, applied.vocab, sha, `${commitPrefix} ${today}`, options);
    markSynced(storagePrefix, today);
    return {
      status: "synced",
      today,
      updatedCount: applied.updatedCount,
      skippedCount: applied.skippedCount
    };
  }

  window.SrsReview = {
    DEFAULT_CONFIG,
    localYmd,
    isAlreadySynced,
    markSynced,
    applyReviewResults,
    syncReviewResults,
    getOrPromptToken,
    readRemoteVocab,
    writeRemoteVocab
  };
}());
