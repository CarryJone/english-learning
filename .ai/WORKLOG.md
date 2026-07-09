# 工作日誌

> 用途：記錄已發生的近期工作事件，最新紀錄放最上方。
> 注意：本檔不是開發規則、不是待辦清單、不是規格來源；不要依本檔決定實作方式。
> 維護：超過 30 筆時，建議歸檔到 `.ai/archive/WORKLOG_YYYY_MM.md`。

---
## 2026-07-09 — Day 74 產出錯誤修復

- 同步遠端 `origin/main`，保留 2026-07-08 的 review quiz 與 sentence SRS 更新。
- 檢查前一輪失敗留下的 `daily/2026-07-09/`，確認內容錯置為 2026-07-08 / Episode 15 複製品。
- 將 `daily/2026-07-09/index.html` 修正為 Day 74、`The Blue Receipt · Episode 16`，主線為 Mina 帶著 report 到 front office。
- 今日新字：`proof`、`clerk`、`deliver`；文章融入複習字：`report`、`guard`、`record`。
- 重新產生 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，確保音檔對應 Episode 16。
- 更新首頁、`profile.json`、`vocabulary/learning.json`、`vocabulary/sentences.json`、`ability_map.json` 與 `.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：`python3 scripts/validate_daily.py 2026-07-09` 通過，70 checks，0 warnings，0 errors。

---
## 2026-07-08 — Day 73 正式教材產出

- 先 `git fetch origin`，確認遠端只比本地多 `vocabulary/sentences.json`，先同步句子 SRS 資料後再生成今天教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-08/`，標題為 `The Blue Receipt · Episode 15`。
- 今日新字：`office`、`report`、`guard`；文章正式揭露門後的人是 May Lin，主線進入收束段。
- Active Recall Quiz 依最新 `learning.json` 生成 5 個今日到期複習字；Speaking Bridge 使用 `voice`、`truth`、`folded`、`careful`。
- 補齊 `Ability Focus`、8 題 `Context Recall`、`vocabulary/sentences.json`、`ability_map.json`、首頁、`profile.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：`article.mp3` 與 `s01.mp3` 到 `s25.mp3` 已生成；`python3 scripts/validate_daily.py 2026-07-08` 通過；本機 HTTP `/` 與 `/daily/2026-07-08/` 回傳 200。

## 2026-07-07 — 每日教材驗證腳本

- 新增 `scripts/validate_daily.py`，以 Python stdlib 驗證單日正式教材。
- 驗證範圍包含必要 HTML 區塊、共用 script、`article.mp3`、逐句 `sNN.mp3`、句子編號連續性、Context Recall 與 `vocabulary/sentences.json` 對齊、`ability_map.json` session、今日新字與 `learning.json` 對齊、Speaking Bridge 不使用今日新字、首頁連結。
- 更新 `.ai/daily-english-learning/SKILL.md`，要求未來 commit / push 前先執行 `python3 scripts/validate_daily.py [日期]`。
- 更新 `LEARNING_SYSTEM_ROADMAP.md`，將 P2 產出驗證自動化多數項目標記完成。
- 驗證：`python3 scripts/validate_daily.py 2026-07-07` 通過，70 checks，0 warnings，0 errors。

---
## 2026-07-07 — 句子 / 情境 SRS MVP

- 新增 `vocabulary/sentences.json`，以 Day 72 的 8 題 Context Recall 作為句子 SRS 初始資料。
- 新增 `assets/sentence-srs.js`，沿用 GitHub Contents API 與本機 `github_pat`，支援 `remembered` / `hinted` / `forgot` 三種自評更新規則。
- 更新 `daily/2026-07-07/index.html`，每題 Context Recall 加入 `data-sentence-id`、自評按鈕、進度與同步入口。
- 更新 `.ai/daily-english-learning/SKILL.md` 與 `LEARNING_SYSTEM_ROADMAP.md`，將句子 SRS 納入未來正式教材流程。
- 驗證：JS 語法、JSON parse、HTML parser、排程函式、HTTP 200、in-app browser 自評進度、未評完同步阻擋、390px 手機寬度無水平 overflow。未實際執行 GitHub 寫入。

---
## 2026-07-07 — Context Recall 情境提取初版

- 更新 `daily/2026-07-07/index.html`，在 Speaking Bridge 後、Learning Tips 前新增 `Context Recall` 區塊。
- Day 72 補入 8 題情境中翻英，分為 Lv.1 有提示、Lv.2 無提示、Lv.3 自由應答。
- 更新 `.ai/daily-english-learning/SKILL.md`，未來正式教材每篇至少產出 6 題，建議 8–10 題 Context Recall。
- 更新 `LEARNING_SYSTEM_ROADMAP.md`，新增 P1 情境提取訓練完成項。
- 驗證：HTML parser、Context Recall 題數 / 答案數檢查、template marker 檢查、in-app browser 翻牌互動、390px 手機寬度無水平 overflow。

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

---
## 2026-06-30 — Day 67 正式教材產出

- 先 `git fetch origin main`，確認遠端多了 `SRS update: review quiz 2026-06-29` 後，再 `git pull --ff-only origin main` 同步最新 `vocabulary/learning.json`。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-06-30/`，標題為 `The Blue Receipt · Episode 9`。
- 新增單字：`paper`、`date`、`tomorrow`；文章融入複習字：`result`、`history`、`match`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、25 個單句音檔存在、Review Quiz 3 題、Speaking Bridge 4 題、本機 HTTP 200。

---
## 2026-06-29 — Day 66 正式教材產出

- 先 `git fetch --all --prune` 同步遠端狀態，確認本地 `HEAD` 與 `origin/main` 一致後再生成今日教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-06-29/`，標題為 `The Blue Receipt · Episode 8`。
- 新增單字：`result`、`history`、`match`；文章融入複習字：`folder`、`photo`、`record`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、25 個單句音檔存在、Review Quiz 65 題、Speaking Bridge 4 題、本機 HTTP 200。

---
## 2026-06-26 — Day 65 正式教材產出

- 先以遠端最新 SRS commit 為底，再合併今天新增單字重算 review，今天共 32 個到期複習字，且無逾期字。
- 延續 serial story continuity，新增 `daily/2026-06-26/`，標題為 `The Blue Receipt · Episode 7`。
- 今日新字：`storage`、`folder`、`record`；文章融入複習字：`locked`、`hallway`、`basement`。
- Speaking Bridge 使用 `arrow`、`photo`、`poster`、`post`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s22.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、22 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-25 — Day 64 正式教材產出

- 先同步遠端 SRS；第一次 `pull` 因 repo 設定失敗，改用 `git merge --ff-only FETCH_HEAD` 補到最新遠端狀態。
- 依最新 `vocabulary/learning.json` 重算 review，今天共 9 個到期複習字。
- 延續 serial story continuity，新增 `daily/2026-06-25/`，標題為 `The Blue Receipt · Episode 6`。
- 今日新字：`locked`、`hallway`、`basement`；文章融入複習字：`arrow`、`poster`、`photo`。
- Speaking Bridge 使用 `post`、`search`、`title`、`front`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s21.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、21 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-24 — Day 63 正式教材產出

- 先同步遠端 SRS；同步後以最新 `vocabulary/learning.json` 重算 review，今天共 3 個到期複習字。
- 延續 serial story continuity，新增 `daily/2026-06-24/`，標題為 `The Blue Receipt · Episode 5`。
- 今日新字：`arrow`、`poster`、`photo`；文章融入複習字：`search`、`post`、`title`。
- Speaking Bridge 使用 `front`、`ride`、`saved`、`listed`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s21.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、21 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-23 — Day 62 正式教材產出

- 先同步遠端 SRS；同步過程中第一次 `git fetch` 出現 remote ref 鎖衝突，但後續 `git pull --ff-only` 已成功更新到最新 `vocabulary/learning.json`。
- 延續 serial story continuity，新增 `daily/2026-06-23/`，標題為 `The Blue Receipt · Episode 4`。
- 今日新字：`search`、`post`、`title`；文章融入複習字：`front`、`saved`、`ride`。
- Review Quiz / Review Words 依最新 `learning.json` 生成，共納入 4 個到期複習字。
- Speaking Bridge 使用 `listed`、`block`、`nearby`、`warning`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s22.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、22 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-22 — Day 61 正式教材產出

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，避免用過期 SRS 生成 review。
- 延續 serial story continuity，新增 `daily/2026-06-22/`，標題為 `The Blue Receipt · Episode 3`。
- 今日新字：`front`、`saved`、`ride`；文章融入複習字：`warning`、`nearby`、`block`。
- Review Quiz / Review Words 依最新 `learning.json` 生成，共納入 50 個到期複習字。
- Speaking Bridge 使用 `block`、`listed`、`nearby`、`warning`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s20.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、20 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-17 — Day 60 連載小說 Episode 2

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，避免用過期 SRS 生成今日 review。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-06-17/`，標題為 `The Blue Receipt · Episode 2`。
- 新增單字：`listed`、`nearby`、`block`；文章融入複習字：`bottom`、`printed`、`warning`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s17.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、17 個單句音檔存在、Review Quiz 3 題、首頁條目存在、本機 HTTP 200。

---
## 2026-06-16 — Day 59 連載小說模式啟動

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，確保 review 區塊使用最新 SRS。
- 建立 `.ai/serial-story/` 文件：`SERIES_BIBLE.md`、`SEASON_1_OUTLINE.md`、`STYLE_GUIDE.md`、`CONTINUITY_LOG.md`。
- 更新 `AGENTS.md`、`.ai/daily-english-learning/SKILL.md`、`.ai/DECISIONS.md`，將每日文章主體改為連載小說模式，下方練習與 SRS 複習維持原樣。
- 新增 `daily/2026-06-16/`，標題為 `The Blue Receipt · Episode 1`。
- 新增單字：`bottom`、`printed`、`warning`；文章融入複習字：`window`、`Wi-Fi code`、`outlet`、`refill`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s18.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、18 個單句音檔存在、Review Quiz 3 題、首頁條目存在、本機 HTTP 200。

---
## 2026-06-15 — Day 58 今日英文練習產出

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，確保 review 區塊使用最新 SRS。
- 依 `profile.json.lastTopic = travel` 產出 `daily` 主題，新增 `daily/2026-06-15/`，標題為 `Reading a Cafe Wi-Fi Sign`。
- 新增單字：`Wi-Fi code`、`outlet`、`refill`；文章融入複習字：`busy`、`message`、`card`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s18.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`。
- 驗證：句子編號連續、18 個單句音檔存在、Review Quiz 24 題、首頁條目存在、本機 HTTP 200。

---
## 2026-06-12 — Day 57 今日英文練習產出

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，避免用過期 SRS 生成 review。
- 依 `profile.json.lastTopic = daily` 產出 `travel` 主題，新增 `daily/2026-06-12/`，標題為 `Reading a Passport Control Sign`。
- 新增單字：`passport control`、`visa`、`stamp`；文章融入複習字：`hall`、`wrong`、`number`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s20.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`。
- 驗證：句子編號連續、20 個單句音檔存在、Review Quiz 36 題、首頁條目存在、本機 HTTP 200。

---
## 2026-06-10 — Day 56 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = travel` 產出 daily 主題。
- 新增 `daily/2026-06-10/`，主題 `Reading a Lunch Combo Sign`，包含完整 HTML、`article.mp3` 與 `s01.mp3` 到 `s18.mp3`。
- 新增單字：`combo`、`sauce`、`allergy`；文章融入複習字：`errand`、`payment`、`section`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：HTML 區塊完整、句子編號連續、18 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-09 — Day 55 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = daily` 產出 travel 主題。
- 新增 `daily/2026-06-09/`，主題 `Reading the Shuttle Zone Sign`，包含完整 HTML、`article.mp3` 與 `s01.mp3` 到 `s18.mp3`。
- 新增單字：`terminal`、`zone`、`direction`；文章融入複習字：`shuttle`、`staff`、`ready`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：HTML 區塊完整、句子編號連續、18 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-08 — Day 54 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = travel` 產出 daily 主題。
- 新增 `daily/2026-06-08/`，主題 `Reloading a Bus Card`，包含完整 HTML、`article.mp3` 與 `s01.mp3` 到 `s18.mp3`。
- 新增單字：`reload`、`balance`、`payment`；文章融入複習字：`queue`、`minute`、`ready`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：HTML 區塊完整、句子編號連續、18 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-05 — Day 53 正式教材產出

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`
- 依 `profile.json.lastTopic = daily` 產出 travel 主題，新增 `daily/2026-06-05/`，標題為 `Checking the Baggage Claim Screen`
- 今日新字：`claim`、`belt`、`hall`；文章融入複習字：`late`、`wrong`、`staff`
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`
