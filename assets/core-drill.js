/**
 * Survival Lines 核心句訓練區塊。
 *
 * 頁面需提供 window.CORE_LINES = [{ id, zh, en, audio }]，
 * 以及一個 #core-drill 容器。SRS 同步沿用 sentence-srs.js 的引擎，
 * 只把 filePath 換成 vocabulary/core-phrases.json。
 */
(function () {
  const SRS_CONFIG = {
    filePath: "vocabulary/core-phrases.json",
    storagePrefix: "core_srs_done_",
    commitPrefix: "Core phrase SRS update",
    intervals: [1, 2, 4, 7, 14, 30, 60],
    promptMessage:
      "首次使用核心句 SRS：請輸入 GitHub Personal Access Token（repo write 權限，儲存在本機）："
  };
  const SECONDS_KEY = "core_drill_seconds";
  const ALLOWED_SECONDS = [3, 5, 8];

  let lines = [];
  let index = 0;
  let timerId = null;
  let audio = null;

  function el(id) {
    return document.getElementById(id);
  }

  function seconds() {
    const stored = Number(localStorage.getItem(SECONDS_KEY));
    return ALLOWED_SECONDS.includes(stored) ? stored : 5;
  }

  function setSeconds(value) {
    localStorage.setItem(SECONDS_KEY, String(value));
    syncSecondButtons();
  }

  function syncSecondButtons() {
    const current = seconds();
    document.querySelectorAll(".core-sec-btn").forEach((btn) => {
      const active = Number(btn.dataset.sec) === current;
      btn.classList.toggle("active", active);
      btn.setAttribute("aria-pressed", String(active));
    });
  }

  function stopTimer() {
    if (timerId) {
      clearInterval(timerId);
      timerId = null;
    }
  }

  function updateProgress() {
    const rated = lines.filter((line) => line.rating).length;
    const progress = el("core-progress");
    if (progress) progress.textContent = `已完成 ${rated} / ${lines.length} 句`;
    const sync = el("core-sync-btn");
    if (sync) sync.disabled = rated < lines.length;
  }

  function renderCard() {
    const line = lines[index];
    if (!line) return;
    stopTimer();
    el("core-position").textContent = `${index + 1} / ${lines.length}`;
    el("core-prompt").textContent = line.zh;
    el("core-count").textContent = "";
    el("core-answer").textContent = line.en;
    el("core-reveal").hidden = true;
    el("core-start").hidden = false;
    el("core-start").textContent = line.rating ? "再練一次" : "開始（先自己說）";
    el("core-next").hidden = index >= lines.length - 1;
    el("core-next").disabled = !line.rating;
    document.querySelectorAll(".core-rate-btn").forEach((btn) => {
      btn.classList.toggle("active", line.rating === btn.dataset.rating);
    });
    updateProgress();
  }

  function play() {
    const line = lines[index];
    if (!line || !line.audio) return;
    if (!audio) audio = new Audio();
    audio.src = line.audio;
    audio.play().catch(() => {});
  }

  function reveal() {
    stopTimer();
    el("core-count").textContent = "";
    el("core-reveal").hidden = false;
    el("core-start").hidden = true;
    play();
  }

  function start() {
    stopTimer();
    el("core-reveal").hidden = true;
    let left = seconds();
    el("core-count").textContent = String(left);
    timerId = setInterval(() => {
      left -= 1;
      if (left <= 0) {
        reveal();
        return;
      }
      el("core-count").textContent = String(left);
    }, 1000);
  }

  function rate(button) {
    const line = lines[index];
    if (!line) return;
    line.rating = button.dataset.rating;
    document.querySelectorAll(".core-rate-btn").forEach((btn) => {
      btn.classList.toggle("active", btn === button);
    });
    el("core-next").disabled = index >= lines.length - 1;
    updateProgress();
  }

  function next() {
    if (index < lines.length - 1) {
      index += 1;
      renderCard();
    }
  }

  async function sync() {
    const result = el("core-result");
    const button = el("core-sync-btn");
    const pending = lines.filter((line) => !line.rating);
    if (pending.length) {
      result.textContent = `還有 ${pending.length} 句尚未自評。`;
      return;
    }
    if (!window.SentenceSrs) {
      result.textContent = "找不到 SRS 模組，無法同步。";
      return;
    }
    button.disabled = true;
    result.textContent = "同步中…";
    try {
      const payload = lines.map((line) => ({ id: line.id, rating: line.rating }));
      const outcome = await window.SentenceSrs.syncSentenceResults(payload, SRS_CONFIG);
      result.textContent =
        outcome.status === "already-synced"
          ? "今天已經同步過了。"
          : `已同步 ${outcome.updatedCount} 句核心句。`;
    } catch (error) {
      result.textContent = "同步失敗：" + (error && error.message ? error.message : error);
      button.disabled = false;
    }
  }

  function init() {
    const container = el("core-drill");
    if (!container || !Array.isArray(window.CORE_LINES) || !window.CORE_LINES.length) return;
    lines = window.CORE_LINES.map((line) => ({ ...line, rating: "" }));
    index = 0;
    syncSecondButtons();
    renderCard();
  }

  window.CoreDrill = { init, start, reveal, rate, next, sync, play, setSeconds };
  document.addEventListener("DOMContentLoaded", init);
}());
