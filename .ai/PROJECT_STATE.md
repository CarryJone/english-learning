# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-07-06
> 更新者：Agent

## 目前目標
- 將既有每日英文教材系統漸進升級為個人英文訓練作業系統，不重新開發完整新 app

## 目前進度
- [x] 已完成 2026-07-06 Day 71 正式英文學習材料產出，連載進度為 `The Blue Receipt · Episode 13`
- [x] 新增 `LEARNING_SYSTEM_ROADMAP.md`，列出 P0–P3 系統調整清單與不重開系統的判斷
- [x] 首頁 `index.html` 已加入學習儀表板，會讀取 `profile.json` 與 `vocabulary/learning.json`
- [x] 首頁顯示累計天數、SRS 單字數、已掌握、今日到期、逾期與目前 episode
- [x] 首頁已加入今日訓練路線，對齊聽全文、逐句聽讀、Review Quiz、Speaking Bridge
- [x] 首頁今日連結已改用本機日期，避免 UTC 日期造成台灣凌晨連錯天
- [x] 修正 `daily/2026-07-03/index.html` 的瀏覽器 `<title>` 日期為 `2026-07-03`
- [x] `WORKLOG.md` 已依規則保留最新 30 筆，舊 2026-05 紀錄封存到 `.ai/archive/WORKLOG_2026_05.md`
- [x] 新增 `review/index.html` 作為獨立 Review Center，可讀取 `vocabulary/learning.json`
- [x] Review Center 顯示今日到期、逾期、active、mastered、到期單字清單與未來 7 天複習量
- [x] Review Center 可產生 Active Recall Quiz，支援先本機檢查答案，再手動同步 SRS
- [x] 首頁已新增「前往複習中心」入口
- [x] 新增 `assets/srs.js` 作為共用 SRS 模組，集中 GitHub Contents API 同步、SRS 間隔、同日防重複更新與本機日期邏輯
- [x] `review/index.html` 已改用 `assets/srs.js`
- [x] `daily/2026-07-03/index.html` 已改用 `assets/srs.js`
- [x] `.ai/daily-english-learning/SKILL.md` 已更新，未來新產出的 daily 頁會引用共用 SRS 模組
- [x] 已新增 `daily/2026-07-06/`，延續 `The Blue Receipt` 到 Episode 13，並補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`
- [x] 首頁 `index.html` 已加入 Day 71 入口，`profile.json` 已更新為 `totalDays = 71`、`currentEpisode = 13`
- [x] 產出前已先 `git fetch origin`，並從 `origin/main` 同步最新 `vocabulary/learning.json` 後再生成 Review Quiz、Review Words 與 Speaking Bridge

## 驗證狀態
- [x] `index.html` HTML parser 檢查通過
- [x] 本機 HTTP server：首頁 `/` 回傳 200
- [x] 本機 HTTP server：`/daily/2026-07-03/` 回傳 200
- [x] In-app browser 桌面寬度載入首頁成功，console 無 error / warn
- [x] 首頁儀表板正確顯示 Day 70、225 words、13 mastered、6 due、0 overdue、Episode 12
- [x] 今日按鈕可導向 `/daily/2026-07-03/`
- [x] In-app browser 手機寬度載入首頁成功，無水平 overflow，console 無 error / warn
- [x] Review Center 本機 HTTP 回傳 200
- [x] In-app browser 載入 Review Center 成功，顯示 6 個到期、0 逾期、6 題測驗與 7 天預覽，console 無 error / warn
- [x] Review Center 本機檢查答案互動通過，6/6 答對後啟用同步按鈕；未實際按同步，避免驗證時寫回 GitHub
- [x] Review Center 手機寬度載入成功，無水平 overflow，console 無 error / warn
- [x] `assets/srs.js` 通過 `node --check`
- [x] 共用 SRS 模組本地單元檢查通過：答對推進間隔、答錯隔天複習
- [x] Day 70 頁面引用共用 SRS 後載入成功，Review Quiz 仍有 6 題，console 無 error / warn
- [x] Day 71 頁面 HTML 結構完整，25 句故事、25 個單句音檔與 `article.mp3` 均存在
- [x] 本機 HTTP server：`/daily/2026-07-06/` 回傳 200
- [x] `profile.json` 與 `vocabulary/learning.json` JSON parse 通過

## 目前 Blocker
- 無

## 下一步
- P1 優先：加入每日難度 / 卡點回饋資料，讓教材能依實際阻塞調整
- P1 優先：定義能力地圖資料結構，追蹤旅行開口、英文資訊判讀、網路閱讀、日常反應
- 下次產出正式英文教材時，仍需先讀 `.ai/serial-story/CONTINUITY_LOG.md`，接續 Episode 14

## 活躍工作區
- `LEARNING_SYSTEM_ROADMAP.md`
- `assets/srs.js`
- `index.html`
- `review/index.html`
- `.ai/daily-english-learning/SKILL.md`
- `daily/2026-07-03/index.html`
- `daily/2026-07-06/index.html`
- `.ai/PROJECT_STATE.md`
- `.ai/WORKLOG.md`
- `.ai/archive/WORKLOG_2026_05.md`
