(function () {
  "use strict";

  const STORAGE_KEY = "english_learning_feedback_v1";
  const MAX_ENTRIES = 90;

  const difficultyLabels = {
    "too-easy": "太簡單",
    "just-right": "剛好",
    "too-hard": "太難"
  };

  const frictionLabels = {
    vocabulary: "單字",
    listening: "聽力",
    speaking: "口說",
    reading: "文章理解",
    sentence: "句型"
  };

  function localYmd(date = new Date()) {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, "0");
    const d = String(date.getDate()).padStart(2, "0");
    return `${y}-${m}-${d}`;
  }

  function readStore() {
    try {
      const raw = window.localStorage.getItem(STORAGE_KEY);
      if (!raw) return { version: 1, entries: [] };
      const parsed = JSON.parse(raw);
      return {
        version: 1,
        entries: Array.isArray(parsed.entries) ? parsed.entries : []
      };
    } catch (err) {
      return { version: 1, entries: [] };
    }
  }

  function writeStore(store) {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
  }

  function cleanText(value) {
    return String(value || "").trim();
  }

  function normalizeEntry(entry) {
    const now = new Date().toISOString();
    const frictions = Array.isArray(entry.frictions) ? entry.frictions : [];
    return {
      date: cleanText(entry.date) || localYmd(),
      difficulty: cleanText(entry.difficulty),
      frictions: frictions.filter((item) => frictionLabels[item]),
      usefulSentence: cleanText(entry.usefulSentence),
      note: cleanText(entry.note),
      createdAt: entry.createdAt || now,
      updatedAt: now
    };
  }

  function saveEntry(entry) {
    const nextEntry = normalizeEntry(entry);
    const store = readStore();
    const existing = store.entries.find((item) => item.date === nextEntry.date);
    if (existing && existing.createdAt) nextEntry.createdAt = existing.createdAt;

    const entries = store.entries.filter((item) => item.date !== nextEntry.date);
    entries.unshift(nextEntry);
    entries.sort((a, b) => String(b.date).localeCompare(String(a.date)));
    writeStore({ version: 1, entries: entries.slice(0, MAX_ENTRIES) });
    return nextEntry;
  }

  function getFeedback(date) {
    return readStore().entries.find((item) => item.date === date) || null;
  }

  function deleteFeedback(date) {
    const store = readStore();
    const entries = store.entries.filter((item) => item.date !== date);
    writeStore({ version: 1, entries });
  }

  function listRecent(limit = 7) {
    return readStore().entries
      .slice()
      .sort((a, b) => String(b.date).localeCompare(String(a.date)))
      .slice(0, limit);
  }

  function labelList(values, labels) {
    if (!values || !values.length) return "未標記";
    return values.map((value) => labels[value] || value).join("、");
  }

  function setStatus(form, message, type) {
    const status = form.querySelector("[data-feedback-status]");
    if (!status) return;
    status.textContent = message;
    status.className = `feedback-status ${type || ""}`.trim();
  }

  function setSelectedDifficulty(form, value) {
    form.querySelectorAll("[data-feedback-difficulty]").forEach((button) => {
      const active = button.dataset.feedbackDifficulty === value;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  function formValue(form, selector) {
    const el = form.querySelector(selector);
    return el ? el.value : "";
  }

  function fillForm(form, entry) {
    if (!entry) return;
    setSelectedDifficulty(form, entry.difficulty);
    form.querySelectorAll('[name="feedback-friction"]').forEach((input) => {
      input.checked = entry.frictions.includes(input.value);
    });
    const useful = form.querySelector('[name="feedback-useful"]');
    const note = form.querySelector('[name="feedback-note"]');
    if (useful) useful.value = entry.usefulSentence || "";
    if (note) note.value = entry.note || "";
    setStatus(form, `已載入 ${entry.date} 的回饋，可再調整後儲存。`, "saved");
  }

  function resetForm(form) {
    setSelectedDifficulty(form, "");
    form.querySelectorAll('[name="feedback-friction"]').forEach((input) => {
      input.checked = false;
    });
    const note = form.querySelector('[name="feedback-note"]');
    if (note) note.value = "";
  }

  function initDailyFeedback(root = document) {
    const form = root.querySelector("[data-feedback-form]");
    if (!form) return;

    let selectedDifficulty = "";
    const date = form.dataset.feedbackDate || localYmd();
    const saved = getFeedback(date);

    form.querySelectorAll("[data-feedback-difficulty]").forEach((button) => {
      button.addEventListener("click", () => {
        selectedDifficulty = button.dataset.feedbackDifficulty;
        setSelectedDifficulty(form, selectedDifficulty);
        setStatus(form, "", "");
      });
    });

    if (saved) {
      selectedDifficulty = saved.difficulty;
      fillForm(form, saved);
    }

    const saveButton = form.querySelector("[data-feedback-save]");
    if (!saveButton) return;
    saveButton.addEventListener("click", () => {
      if (!selectedDifficulty) {
        setStatus(form, "先選今天的難度，系統才知道要怎麼調整。", "warn");
        return;
      }

      const frictions = Array.from(form.querySelectorAll('[name="feedback-friction"]:checked'))
        .map((input) => input.value);
      const entry = saveEntry({
        date,
        difficulty: selectedDifficulty,
        frictions,
        usefulSentence: formValue(form, '[name="feedback-useful"]'),
        note: formValue(form, '[name="feedback-note"]')
      });

      const frictionText = labelList(entry.frictions, frictionLabels);
      setStatus(form, `已儲存：${difficultyLabels[entry.difficulty]} · 卡點：${frictionText}`, "saved");
    });

    const clearButton = form.querySelector("[data-feedback-clear]");
    if (clearButton) {
      clearButton.addEventListener("click", () => {
        deleteFeedback(date);
        selectedDifficulty = "";
        resetForm(form);
        setStatus(form, "已清除今天的回饋。", "saved");
      });
    }
  }

  function renderHomeSummary(target) {
    const el = typeof target === "string" ? document.querySelector(target) : target;
    if (!el) return;
    const latest = listRecent(1)[0];
    if (!latest) {
      el.innerHTML = '<div class="feedback-empty">尚未留下回饋。完成今日教材後，回到頁尾標記難度與卡點。</div>';
      return;
    }

    const difficulty = difficultyLabels[latest.difficulty] || "未標記";
    const frictions = labelList(latest.frictions, frictionLabels);
    const useful = latest.usefulSentence || "尚未填寫";
    el.innerHTML = `
      <div class="feedback-summary-row">
        <span class="feedback-summary-label">日期</span>
        <strong>${escapeHtml(latest.date)}</strong>
      </div>
      <div class="feedback-summary-row">
        <span class="feedback-summary-label">難度</span>
        <strong>${escapeHtml(difficulty)}</strong>
      </div>
      <div class="feedback-summary-row">
        <span class="feedback-summary-label">卡點</span>
        <span>${escapeHtml(frictions)}</span>
      </div>
      <div class="feedback-useful-line">最有用一句：${escapeHtml(useful)}</div>
    `;
  }

  function escapeHtml(value) {
    return String(value || "").replace(/[&<>"']/g, (ch) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    }[ch]));
  }

  window.LearningFeedback = {
    STORAGE_KEY,
    difficultyLabels,
    frictionLabels,
    localYmd,
    saveEntry,
    getFeedback,
    deleteFeedback,
    listRecent,
    initDailyFeedback,
    renderHomeSummary
  };
})();
