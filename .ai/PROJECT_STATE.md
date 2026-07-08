# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-07-08
> 更新者：Agent

## 目前目標
- 將既有每日英文教材系統漸進升級為個人英文訓練作業系統，不重新開發完整新 app。

## 目前進度
- [x] 已完成 2026-07-08 Day 73 正式英文學習材料；連載進度為 `The Blue Receipt · Episode 15`。
- [x] `LEARNING_SYSTEM_ROADMAP.md` 已列出 P0-P3 系統調整清單，核心決策是不重開完整新系統。
- [x] 首頁 `index.html` 已有學習儀表板、今日訓練路線、Review Center、能力地圖與最近回饋入口。
- [x] `review/index.html` 可讀取 `vocabulary/learning.json` 並產生 Active Recall Quiz。
- [x] `assets/srs.js` 已集中單字 SRS 同步、間隔、本機日期與同日防重複更新邏輯。
- [x] 新增 `assets/feedback.js` 與 Day 72 Daily Feedback；首頁可顯示最近回饋，資料暫存於瀏覽器 `localStorage`。
- [x] 新增 `ability_map.json` 作為能力地圖 source of truth；首頁顯示本週四條能力訓練狀態。
- [x] Day 73 延續 `Ability Focus` 與 8 題 `Context Recall`。
- [x] 新增 `vocabulary/sentences.json` 與 `assets/sentence-srs.js`；Day 72 Context Recall 可自評並同步句子 SRS 到 GitHub。
- [x] 新增 `scripts/validate_daily.py`；`.ai/daily-english-learning/SKILL.md` 已要求未來正式教材產出後跑 `python3 scripts/validate_daily.py YYYY-MM-DD`。
- [x] 未來正式教材需包含 Context Recall 自評、句子 SRS、Daily Feedback、Ability Focus，並同步 `ability_map.json` / `vocabulary/sentences.json`。

## 驗證狀態
- [x] `node --check assets/feedback.js` 通過。
- [x] `assets/feedback.js` 本地行為測試通過：同日覆寫、最近排序、儲存 / 清除正常。
- [x] `ability_map.json` JSON parse 與能力 ID 檢查通過。
- [x] `index.html` 與 `daily/2026-07-08/index.html` HTML parser 檢查通過。
- [x] 本機 HTTP server：`/`、`/daily/2026-07-08/` 均回傳 200。
- [x] In-app browser 首頁可顯示本週能力地圖與最近回饋；Day 72 可顯示 `Ability Focus` 與 8 題 `Context Recall`，手機 390px 無水平 overflow。
- [x] 句子 SRS MVP 驗證通過：`assets/sentence-srs.js` 語法、`vocabulary/sentences.json` JSON、排程函式、Day 72 自評進度、未評完同步阻擋、HTTP 200、手機 390px 無水平 overflow。
- [x] `python3 scripts/validate_daily.py 2026-07-08` 通過：70 checks，0 warnings，0 errors。

## 目前 Blocker
- 無。

## 下一步
- P2 可接：讓驗證腳本補查連載 `CONTINUITY_LOG.md` 是否更新，或新增 `vocabulary/phrases.json` 作為片語 SRS 資料源。
- 後續若要完整驗證 GitHub 寫入路徑，需由使用者明確同意後再按滿 8 題並執行 `同步句子 SRS`。
- 下次產出正式英文教材時，仍需先讀 `.ai/serial-story/CONTINUITY_LOG.md`，接續 Episode 16。

## 活躍工作區
- `assets/feedback.js`
- `assets/sentence-srs.js`
- `ability_map.json`
- `vocabulary/sentences.json`
- `scripts/validate_daily.py`
- `index.html`
- `daily/2026-07-08/index.html`
- `.ai/daily-english-learning/SKILL.md`
