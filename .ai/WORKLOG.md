# 工作日誌

> 用途：記錄已發生的近期工作事件，最新紀錄放最上方。
> 注意：本檔不是開發規則、不是待辦清單、不是規格來源；不要依本檔決定實作方式。
> 維護：超過 30 筆時，建議歸檔到 `.ai/archive/WORKLOG_YYYY_MM.md`。

---
## 2026-08-28 — Day 108 正式教材產出

- 先執行 `git fetch origin`，確認遠端有 2026-08-27 的 SRS 更新後以 fast-forward 同步；同步後今天共有 24 個到期複習字。
- 新增 `daily/2026-08-28/`，主題為 `Checking a Wrong Price at an Airport Gift Shop`；今日新字：`discount`、`offer`、`amount`。
- 文章以 airport shop page、offer sign、price tag 與 cashier conversation 為英文輸入；任務是找出特價期限、20% 折扣、含稅與三十天退換條件，並在錯誤標價時確認最後金額。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔；文章融入到期複習字 `late`、`wrong`、`change`。
- 文章使用旁白、旅客、工作人員三聲線，36 句 / 257 字；主音檔實測 130.75 秒，另有 36 個逐句音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-08-28` 通過 84 checks、0 warnings、0 errors；JSON、JavaScript syntax、內容 / SRS 對齊與 `git diff --check` 均通過；未修改既有未追蹤的 `test/`。

---
## 2026-08-27 — Day 107 正式教材產出

- 先 `git fetch origin`，以 fast-forward 同步遠端最新 SRS；同步後今天共有 19 個到期複習字。
- 新增 `daily/2026-08-27/`，主題為 `Ordering a Safe Café Meal with a Food Allergy`；今日新字：`dairy`、`dish`、`side`。
- 文章以手機咖啡廳菜單、過敏提示與點餐對話為英文輸入；任務是確認無乳製品、附餐與價格，並在雞肉飯碗售罄後改選豆腐飯碗。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、10 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔。
- 文章使用旁白、旅客、工作人員三聲線，36 句 / 274 字；主音檔實測 126.98 秒。
- 驗證：`python3 scripts/validate_daily.py 2026-08-27` 通過 84 checks、0 warnings、0 errors；JSON、JavaScript syntax、`git diff --check` 與內容對齊檢查通過；未修改既有未追蹤的 `test/`。

---
## 2026-08-26 — Day 106 正式教材產出

- 先 `git fetch origin` 確認遠端沒有較新的 SRS 更新；依 `vocabulary/learning.json` 產生今天 15 個到期複習字。
- 新增 `daily/2026-08-26/`，主題為 `Taking the Right City Bus During a Road Detour`；今日新字：`bus`、`detour`、`opposite`。
- 文章以 map result、bus detour notice 與 driver conversation 為英文輸入；任務是找到臨時站牌、確認 Bus Twelve，並在 Museum Square 下車。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、8 回合 Role-play、Ability Map、句子 SRS 與首頁入口；Speaking Bridge 使用 `train`、`depart`、`airport`、`eligible`，未使用今日新字。
- 文章使用旁白、旅客、工作人員三聲線，34 句 / 268 字；完成主音檔與 34 個逐句音檔，對調聲線後主音檔實測 117.50 秒。
- 依使用者回饋對調聲線：旁白改用 Jenny、旅客（我的台詞）改用 Aria，工作人員維持 Guy；重新生成今天的旁白與旅客逐句音檔及完整主音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-08-26` 通過 84 checks、0 warnings、0 errors；JSON、JavaScript syntax、`git diff --check` 與內容對齊檢查通過；未修改既有未追蹤的 `test/`。

## 2026-08-25 — Day 105 正式教材產出

- 先 `git fetch origin` 並以 fast-forward 同步遠端最新 SRS；依同步後的 `vocabulary/learning.json` 產生今天 5 個到期複習字。
- 新增 `daily/2026-08-25/`，主題為 `Finding the Hotel After a Station Exit Change`；今日新字：`directions`、`walk`、`cross`。
- 文章以 station notice、map result 與 information-desk conversation 為英文輸入；任務是出口變更後找到飯店側門，融入 `notice`、`miss`、`fountain` 等路線字。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔。
- 先以三聲線重新生成音檔：`narrator` 使用 Aria、`traveler` 使用 Jenny、`staff` 使用 Guy，並在頁面加入聲線提示。
- 依回饋再修正 Article：拿掉 `I ask`、`She says` 等報導式包裝，讓旁白、旅客台詞與工作人員台詞各自成句，再重新生成三聲線音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-08-25` 通過 84 checks、0 warnings、0 errors；主音檔 119.78 秒，34 句 / 262 字、35 個 MP3 均存在且可讀；未修改既有未追蹤的 `test/`。

---
## 2026-08-24 — Day 104 正式教材產出

- 先 `git fetch origin`，以 fast-forward 同步遠端 2026-08-21 的最新單字 SRS，再依最新 `vocabulary/learning.json` 生成今日複習內容。
- 新增 `daily/2026-08-24/`，主題為 `Finding the Right Airport Train After a Platform Change`；今日新字：`train`、`depart`、`airport`。
- 文章以車站 departure screen、station notice 與工作人員對話為英文輸入；融入 `station`、`screen`、`line`、`notice`、`delayed`、`valid` 等到期字。
- Active Recall Quiz 納入全部 39 個到期字；Speaking Bridge 使用 2–7 天前的 `fuel`、`damage`、`deposit`、`eligible`；完成 10 題 Context Recall 與 8 回合 Role-play。
- 完成 Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s34.mp3`；主音檔實測 121.97 秒。
- 驗證：`python3 scripts/validate_daily.py 2026-08-24` 通過 84 checks、0 warnings、0 errors；JSON parse、JavaScript syntax、`git diff --check` 與內容對齊檢查通過。

---
## 2026-08-19 — Day 101 正式教材產出

- 先 `git fetch origin` 並以 fast-forward 同步 2026-08-18 最新單字 SRS，再依最新 `vocabulary/learning.json` 產生複習內容。
- 新增 `daily/2026-08-19/`，主題為 `Finding the Walking Tour Meeting Point`；今日新字：`meeting point`、`fountain`、`tour`。
- Active Recall Quiz 納入全部 11 個到期字；Speaking Bridge 使用 `carousel`、`describe`、`handle`、`noise`；完成 10 題 Context Recall 與 8 回合 Role-play。
- 完成 Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s32.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-08-19` 通過 84 checks、0 warnings、0 errors；主音檔 118.25 秒，32 句 / 257 字；390×844 手機版無橫向溢位，首頁前三筆為 Day 101、100、99，音檔可載入。

---
## 2026-08-18 — Day 100 正式教材與首頁清單修復

- 先 `git fetch origin` 並以 fast-forward 同步 2026-08-17 最新單字 SRS，再依最新 `vocabulary/learning.json` 產生複習內容。
- 新增 `daily/2026-08-18/`，主題為 `Checking Carry-on Liquid Rules Before Security`；今日新字：`liquid`、`container`、`limit`。
- Active Recall Quiz 納入全部 3 個到期字；Speaking Bridge 使用 `contain`、`sensitive`、`delayed`、`deck`；完成 10 題 Context Recall 與 8 回合 Role-play。
- 修正首頁學習記錄容器錯位：Day 99 原本落在 Day 66 後方，現已將全部日期統一放回 `#day-list`，依日期新到舊排序。
- 驗證：`python3 scripts/validate_daily.py 2026-08-18` 通過 84 checks、0 warnings、0 errors；主音檔 117.94 秒，31 句 / 251 字；390×844 手機版首頁與教材均無橫向溢位，首頁前三筆為 Day 100、99、98。

---
## 2026-08-17 — Day 99 正式教材產出

- 先 `git fetch origin`，以 fast-forward 同步遠端最新單字 SRS，再依最新 `vocabulary/learning.json` 產生複習內容。
- 新增 `daily/2026-08-17/`，主題為 `Reporting a Missing Suitcase at Baggage Claim`；今日新字：`carousel`、`describe`、`handle`。
- 文章融入到期複習字 `passenger`、`nearby`、`delayed`；Active Recall Quiz 納入全部 37 個到期字；Speaking Bridge 使用 `noise`、`maintenance`、`fan`、`delayed`。
- 完成 10 題 Context Recall、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s36.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-08-17` 通過 84 checks、0 warnings、0 errors；主音檔 130.56 秒；390×844 手機版無橫向溢位，0.75× 與逐句播放正常，console 0 errors。

---
## 2026-08-03 — Day 89 正式教材產出

- 先執行 `git fetch origin`，確認本地 `HEAD` 與 `origin/main` 同步，使用最新的 `vocabulary/learning.json` 生成複習內容。
- 新增 `daily/2026-08-03/`，主題為 `Handling a Stuck Hotel Laundry Machine`；今日新字：`stuck`、`repair`、`working`。
- 文章融入到期複習字 `option`、`choice`、`reception`；Active Recall Quiz 納入全部 46 個到期字；Speaking Bridge 使用 `expired`、`reset`、`item`、`damaged`。
- 完成 10 題 Context Recall、12 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s16.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-08-03` 通過 79 checks、0 warnings、0 errors；JSON parse、句子字數、目標語塊分布與 `git diff --check` 亦完成檢查。

---
## 2026-07-31 — Day 88 正式教材產出

- 先 `git fetch origin`，確認遠端有 2026-07-30 的 SRS 更新後，以 fast-forward 同步最新 `vocabulary/learning.json`。
- 新增 `daily/2026-07-31/`，主題為 `Fixing a Missing Café Item`；今日新字：`missing`、`item`、`remake`。
- 文章融入到期複習字 `replace`、`option`、`deliver`；Active Recall Quiz 納入同步後全部 15 個到期字；Speaking Bridge 使用 `damaged`、`baggage`、`miss`、`flexible`。
- 完成 10 題 Context Recall、10 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s14.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-07-31` 通過 79 checks、0 warnings、0 errors；JSON parse、目標語塊分布與音檔對齊亦完成檢查。

---
## 2026-07-30 — Day 87 正式教材產出

- 先 `git fetch origin`，確認遠端有 2026-07-29 的 SRS 更新後，以 `git pull --ff-only origin main` 同步最新 `vocabulary/learning.json`。
- 新增 `daily/2026-07-30/`，主題為 `Fixing a Hotel Key Card Problem`；今日新字：`expired`、`reset`、`access`。
- 文章融入到期複習字 `speaker`、`deliver`、`option`；Active Recall Quiz 納入同步後全部 15 個到期字；Speaking Bridge 使用 `damaged`、`baggage`、`label`、`larger`。
- 完成 10 題 Context Recall、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s14.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-07-30` 通過 79 checks、0 warnings、0 errors；句子皆不超過 12 字、JSON parse、SRS 對齊與 `git diff --check` 亦通過。

---
## 2026-07-22 — Day 81 正式教材產出

- 先同步遠端兩筆 2026-07-21 SRS 更新，再依最新 `vocabulary/learning.json` 產生今日複習內容。
- 新增 `daily/2026-07-22/`，主題為 `Checking Hotel Breakfast and Luggage`；今日新字為 `included`、`reception`、`store`。
- 開始語塊深化試行第 1/7 篇：`breakfast is included`、`Can I leave my luggage here?`、`I want to make sure` 貫穿 Article、Key Phrases、Role-play 與 Context Recall，並加入跨情境提取。
- 教材包含 19 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge、8 回合 Role-play、`article.mp3` 與 `s01.mp3` 到 `s14.mp3`。
- 同步更新首頁、`profile.json`、`vocabulary/learning.json`、`vocabulary/sentences.json`、`ability_map.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：`validate_daily.py` 通過 79 checks、0 warnings、0 errors；JSON、JavaScript、`git diff --check` 及本機 HTTP 頁面 / 音檔 200 皆通過。

---
## 2026-07-21 — 詞彙深度與語塊訓練規格

- 依使用者確認，將詞彙學習由孤立字義深化為自然搭配、可重用語塊、Role-play 產出與 Context Recall 跨情境提取。
- 更新 `AGENTS.md` 與 `.ai/daily-english-learning/SKILL.md`：每篇選 2–3 個目標語塊，區分主動產出與辨識理解，並保留既有 Active Recall、Speaking Bridge 與句子 SRS 邊界。
- 更新 `.ai/DECISIONS.md` 與 `.ai/PROJECT_STATE.md`，記錄 Day 81 起連續 7 篇試行方式、人工驗收項目與後續評估依據。
- 本次只調整規格與接手文件，未修改每日頁面、資料 schema、SRS runtime 或驗證器。

---
## 2026-07-16 — Day 78 任務型教材正式產出

- 先同步遠端最新 SRS；同步後今日共有 11 個到期複習字。
- 新增 daily/2026-07-16/，主題為 Choosing a Ferry Departure；今日新字：dock、boarding、option。
- Mission 以渡輪時刻表、票務提示與櫃檯對話為輸入，包含 8 回合 Role-play、10 題 Context Recall 與 4 個 2–7 天前單字的 Speaking Bridge。
- 同步更新首頁、profile.json、vocabulary/learning.json、vocabulary/sentences.json、ability_map.json；生成 article.mp3 與 s01.mp3 到 s16.mp3。
- 驗證：python3 scripts/validate_daily.py 2026-07-16 通過 79 checks，0 warnings，0 errors；JSON parse 與 git diff --check 亦通過。

---
## 2026-07-15 — Day 77 任務型教材正式產出

- 先 `git fetch origin` / `git pull --ff-only origin main`，同步最新 7/14 review quiz 與 sentence SRS 後生成今天教材。
- 新增 `daily/2026-07-15/`，主題為 `Finding the Right Bus`；今日新字：`museum`、`instead`、`passenger`。
- Active Recall Quiz 依最新 SRS 產出 12 個到期複習字；Speaking Bridge 使用前幾日單字；Context Recall 8 題、Role-play 8 回合與 Mission 均已接通。
- 生成 `article.mp3` 與 `s01.mp3` 到 `s19.mp3`，並更新首頁、`profile.json`、`vocabulary/learning.json`、`vocabulary/sentences.json`、`ability_map.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：`python3 scripts/validate_daily.py 2026-07-15` 通過 73 checks，0 warnings，0 errors。

---
## 2026-07-15 — 任務型測試版修正單字複習流程

- 將 `test/2026-07-15/` 的單字複習改為 Active Recall Quiz，載入遠端最新 SRS 的 12 個到期單字，使用中文意思、例句挖空與四選一。
- 依使用者回饋移除文章句子前的可見編號，保留逐句播放與句子資料順序。
- 更新 `AGENTS.md`、`.ai/daily-english-learning/SKILL.md` 與 `.ai/PROJECT_STATE.md`，確認單字複習沿用既有 Active Recall Quiz 與 SRS 流程。
- 驗證：HTML/JS 語法、HTTP 200、音檔與 `git diff --check` 通過。

---
## 2026-07-15 — 每日教材切換為任務型情境英文

- 依使用者確認，將 `The Blue Receipt` Episode 18 標記為第一季結尾，停止每日自動續寫小說。
- 更新 `.ai/daily-english-learning/SKILL.md`：新增 Mission、英文資訊輸入、Role-play、跨情境 Context Recall 與每週能力平衡規則。
- 同步更新 `AGENTS.md`、`profile.json`、首頁、`scripts/validate_daily.py`、`LEARNING_SYSTEM_ROADMAP.md` 與 `.ai/DECISIONS.md`。
- 封存 `.ai/serial-story/` 文件，保留既有小說資料，不重開完整 app。
- 驗證：舊 Episode 18 通過 70 checks；Python / JSON / 首頁 inline JS / `git diff --check` 通過；新日期的 Mission、Role-play transition guard 通過。

---
## 2026-07-13 — Day 75 正式教材產出

- 先 `git fetch origin` 並 `git pull --ff-only origin main`，同步 7/9 單字 SRS 與句子 SRS 遠端更新後再生成今天教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-13/`，標題為 `The Blue Receipt · Episode 17`。
- 今日新字：`key`、`unlock`、`final`；文章融入複習字：`platform`、`clerk`、`tomorrow`、`receipt`、`printed`、`voice`。
- Review Quiz / Review Words 依最新 `learning.json` 生成，共納入 43 個到期複習字。
- Speaking Bridge 使用 `proof`、`clerk`、`deliver`、`exact`；Context Recall 8 題同步寫入 `vocabulary/sentences.json`。
- 同步首頁、`profile.json`、`ability_map.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：`article.mp3` 與 `s01.mp3` 到 `s25.mp3` 已生成；`python3 scripts/validate_daily.py 2026-07-13` 通過，70 checks，0 warnings，0 errors。

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
