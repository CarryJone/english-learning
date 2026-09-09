# 2026-07 工作日誌歸檔

> 用途：保存已歸檔工作日誌。
> 注意：本檔不是開發規則、不是待辦清單、不是規格來源。

---
## 2026-07-07 — 能力地圖 P1 初版

- 新增 `ability_map.json`，定義 `travelSpeaking`、`publicEnglish`、`onlineReading`、`dailyResponse` 四條能力主線與最近 session。
- 更新首頁 `index.html`，新增「本週能力地圖」卡，從 `ability_map.json` 計算本週能力覆蓋狀態。
- 更新 `daily/2026-07-07/index.html`，新增 `Ability Focus` 區，顯示今日能力標記與 evidence。
- 更新 `.ai/daily-english-learning/SKILL.md`，未來正式教材產出時需選能力、顯示 Ability Focus，並同步 `ability_map.json`。
- 驗證：`ability_map.json` JSON parse、HTML parser、HTTP 200、in-app browser 首頁 / Day 72 桌面與 390px 手機寬度檢查，console 無 error / warn。

---

## 2026-07-07 — 每日難度與卡點回饋 P1 初版

- 新增 `assets/feedback.js`，用 `localStorage` key `english_learning_feedback_v1` 儲存每日難度、卡點、最有用一句與補充卡點。
- 更新 `daily/2026-07-07/index.html`，在 Learning Tips 後加入 Daily Feedback 區，支援儲存與清除今日回饋。
- 更新首頁 `index.html`，新增「最近回饋」卡，讀取同一台瀏覽器最近一筆回饋。
- 更新 `.ai/daily-english-learning/SKILL.md`，讓未來 daily 頁延續同一套回饋表單與共用模組。
- 更新 `LEARNING_SYSTEM_ROADMAP.md`，標記回饋區與等效資料來源完成，並記錄 localStorage 仍需匯出 / 同步機制才能讓產出 agent 穩定讀取。
- 驗證：`node --check assets/feedback.js`、HTML parser、本機 HTTP 200、in-app browser 桌面互動、首頁摘要顯示、390px 手機寬度無水平 overflow。

---

## 2026-07-07 — Day 72 正式教材產出

- 先 `git fetch origin`，確認遠端多了 `SRS update: review quiz 2026-07-06`，再只同步最新 `vocabulary/learning.json` 後生成今天教材，避免用到過期複習狀態。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-07/`，標題為 `The Blue Receipt · Episode 14`。
- 今日新字：`safe`、`follow`、`decide`；文章融入複習字：`paper`、`shadow`、`post`。
- Review Quiz / Review Words 依同步後的最新 `learning.json` 生成，共納入 5 個到期複習字。
- Speaking Bridge 使用 `paper`、`circle`、`folded`、`speaker`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：HTML 結構完整、句子編號連續、25 個單句音檔存在、`article.mp3` 存在、JSON parse 通過。

---

## 2026-07-06 — Day 71 正式教材產出

- 先 `git fetch origin`，確認遠端 `origin/main` 有較新的 SRS 更新後，只同步 `vocabulary/learning.json`，避免用過期 review 狀態生成今天教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-06/`，標題為 `The Blue Receipt · Episode 13`。
- 今日新字：`shadow`、`careful`、`exact`；文章融入複習字：`outside`、`voice`、`inside`。
- Review Quiz / Review Words 依同步後的最新 `learning.json` 生成，共納入 37 個到期複習字。
- Speaking Bridge 使用 `circle`、`folded`、`speaker`、`date`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：HTML 結構完整、句子編號連續、25 個單句音檔存在、`article.mp3` 存在、本機 HTTP 200、JSON parse 通過。

---

## 2026-07-03 — SRS 共用模組抽出

- 完成：新增 `assets/srs.js`，集中本機日期、GitHub Contents API 讀寫、SRS 間隔、同日防重複同步與 review result 套用邏輯。
- 修改：`review/index.html` 改用 `window.SrsReview.syncReviewResults()` 同步 SRS，不再內嵌 GitHub API 更新流程。
- 修改：`daily/2026-07-03/index.html` 與 `.ai/daily-english-learning/SKILL.md` 改為引用 `../../assets/srs.js`，未來新 daily 頁會走共用模組。
- 修改：`LEARNING_SYSTEM_ROADMAP.md` 將「Review Quiz 的同步邏輯整理成可共用模組」標記完成。
- 驗證：`node --check assets/srs.js`、HTML parser、HTTP asset/review/day70 200、SRS 模組本地單元檢查、in-app browser Review Center 本機檢查 6/6、Day 70 載入無 console 錯誤。
- 注意：驗證未實際按 GitHub 同步，避免測試過程寫回遠端 `learning.json`。

---

## 2026-07-03 — 學習系統 P0 升級

- 完成：新增 `LEARNING_SYSTEM_ROADMAP.md`，列出不重開系統、沿用現有核心並分階段升級的調整清單。
- 修改：首頁 `index.html` 升級為入口儀表板，讀取 `profile.json` 與 `vocabulary/learning.json` 顯示累計天數、SRS 單字、已掌握、今日到期、逾期與連載進度。
- 修改：首頁加入今日訓練路線，並將今日連結日期從 UTC 改成本機日期，避免台灣凌晨連到錯誤日期。
- 修正：`daily/2026-07-03/index.html` 的 `<title>` 日期由 `2026-07-02` 改為 `2026-07-03`。
- 驗證：本機 HTTP 首頁與今日頁回傳 200；in-app browser 桌面與手機寬度載入成功、console 無錯誤、今日連結可進入 Day 70。

---

## 2026-07-03 — Day 70 正式教材產出

- 先 `git fetch origin`，發現遠端有新的 SRS 提交 `601d261`，再 `git pull --rebase origin main` 同步最新 `vocabulary/learning.json`。
- 延續 serial story continuity，新增 `daily/2026-07-03/`，標題為 `The Blue Receipt · Episode 12`。
- 今日新字：`speaker`、`folded`、`circle`；文章融入複習字：`match`、`history`、`truth`。
- Review Quiz / Review Words 依最新 `learning.json` 生成，共納入 6 個到期複習字。
- Speaking Bridge 使用 `history`、`match`、`result`、`date`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：HTML 完整區塊存在、句子編號連續、25 個單句音檔存在、本機 HTTP 200。

---
## 2026-07-03 — Review Center P1 初版

- 完成：新增 `review/index.html`，作為獨立 Review Center，讀取 `vocabulary/learning.json` 即時計算今日到期、逾期、active、mastered 與未來 7 天複習量。
- 完成：Review Center 會列出到期單字並動態產生 Active Recall Quiz；使用者可先本機檢查答案，再手動同步 SRS。
- 修改：首頁 `index.html` 新增「前往複習中心」入口；`LEARNING_SYSTEM_ROADMAP.md` 更新 P1 複習中心完成狀態。
- 驗證：HTML parser、`git diff --check`、HTTP `/review/` 200；in-app browser 桌面與手機寬度載入成功、console 無錯誤、6 題本機檢查互動通過。
- 注意：驗證時未按「同步 SRS」，避免測試過程寫回 GitHub。

---
## 2026-07-02 — Day 69 正式教材產出

- 先 `git fetch origin main` 確認遠端狀態，因 `origin/main` 與本地一致，直接用目前最新的 `vocabulary/learning.json` 生成今日教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-02/`，標題為 `The Blue Receipt · Episode 11`。
- 新增單字：`truth`、`alone`、`early`；文章融入複習字：`voice`、`inside`、`outside`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、25 個單句音檔存在、Review Quiz 11 題、Speaking Bridge 4 題、本機 HTTP 200。

---
## 2026-07-01 — Day 68 正式教材產出

- 先 `git fetch origin main`，確認遠端多了 `SRS update: review quiz 2026-06-30` 後，再 `git pull --ff-only origin main` 同步最新 `vocabulary/learning.json`。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-01/`，標題為 `The Blue Receipt · Episode 10`。
- 新增單字：`voice`、`inside`、`outside`；文章融入複習字：`paper`、`date`、`tomorrow`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、25 個單句音檔存在、Review Quiz 5 題、Speaking Bridge 4 題、本機 HTTP 200。
