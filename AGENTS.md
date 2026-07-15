# AGENTS.md — english-learning 專案規則

## 專案性質

- 這個專案的主 runtime 是靜態網站。
- 不要把它當成需要 build 的 Node / Python app。
- 可執行入口以靜態 HTML 與本機 HTTP server 為主。

## 英文學習材料產出規則

- 只要需求涉及「每日英文學習材料」、「英文練習頁」、「正式學習內容產出」，第一步必讀：
  - `.ai/daily-english-learning/SKILL.md`
- 自 2026-07-15 起，正式每日內容預設採「任務型情境英文」模式；文章主體要服務真實出遊溝通與英文網路查資料，不再自動產出連載小說。
- `The Blue Receipt` 第一季已於 Episode 18 封存。除非使用者明確要求回顧或續寫小說，否則不要讀取或更新：
  - `.ai/serial-story/SERIES_BIBLE.md`
  - `.ai/serial-story/SEASON_1_OUTLINE.md`
  - `.ai/serial-story/STYLE_GUIDE.md`
  - `.ai/serial-story/CONTINUITY_LOG.md`
- 任務型教材每篇必須有一個可驗收的 real-life mission、一份短英文資訊輸入、一段可開口的 Role-play，以及中文情境到英文的主動提取。
- 任務型教材的每週平衡為：旅行開口 3 天、英文資訊判讀 2 天、整合任務 1 天、SRS 與模擬複習 1 天；每日仍可同時帶入另一個能力。
- 正式學習結構維持原樣並新增 Mission、Role-play；Article、New Words、Key Phrases、Quiz、Active Recall Quiz、Speaking Bridge、Context Recall、Learning Tips、Review Words、完整音檔與逐句播放都不可省略。
- `New Words` 負責先學；`Active Recall Quiz` 負責複習前面已學過且依 SRS 到期的單字。不可用只列出今日新字的獨立區塊取代 Active Recall Quiz。
- 正式產出必須依上面那份 SKILL 的流程執行，不可自行簡化成 demo。
- 正式產出的核心目標不是「每天有一篇英文」，而是讓學習者逐步更能：
  - 在旅行中開口、聽懂、應對
  - 在網路上看懂英文標題、提示、教學內容與搜尋結果
- `profile.json.lastTopic` 在新模式固定為 `mission`，不再使用 `daily / travel` 二選一硬輪替；內容依每週任務平衡與最近訓練能力安排。
- 任務題材應主動分散到交通、問路、旅館、點餐、購物、付款、改票、求助、搜尋結果、教學步驟、評論與規則，不可長期停留在同質故事或居家情境。
- 每篇資訊輸入必須讓學習者找出至少 2 個可驗收資訊，例如時間、地點、價格、限制、下一步或所需條件。
- 文章、片語、單字應優先選高頻、口語、能立即套用的日常英文，不要為了湊題材或湊單字而犧牲自然度。
- 每日內容至少要讓學習者明確帶走：
  - 1 句旅行或外出時可直接套用的句子
  - 1 個查資料時看得懂或搜得到的關鍵說法 / 片語
- 若某篇文章雖然簡單，但做完後難以回答「這能幫學習者在哪個真實場景更會用英文」，視為題材命中率不足，下一篇應主動修正。
- 若使用者要求「先看成果」，預設理解為：
  - 要看正式格式成果
  - 不是隨意設計的簡化版頁面
- 若真的只要 demo / 草稿，必須是使用者明確指定。

## 正式產物最低要求

- 正式學習材料至少要包含：
  - `index.html`
  - `article.mp3`
  - `s01.mp3` 到 `sNN.mp3`
- HTML 結構必須包含完整區塊：
  - Article
  - New Words
  - Key Phrases
  - Quiz
  - Active Recall Quiz
  - Speaking Bridge
  - Context Recall
  - Mission
  - Role-play
  - Learning Tips
  - Review Words
- 不可省略音檔。
- 不可省略逐句播放結構。

## 資料來源優先順序

- 正式內容規格：以
  `.ai/daily-english-learning/SKILL.md`
  為準。
- 複習資料現況：以
  `vocabulary/learning.json`
  為準。
- 學習者狀態：以
  `profile.json`
  為準。
- 若 `daily/*.html` 與 `vocabulary/learning.json` 衝突：
  - 以 `learning.json` 現況為 source of truth
  - 不要直接照抄舊 daily 頁內容

## Review / Bridge 規則

- 只要要產出「今天」的正式教材，開始規劃前先同步最新 SRS 資料：
  - 先 `git fetch`，並確認本地 `vocabulary/learning.json` 已包含遠端最新提交
  - 若遠端有較新的 SRS 更新，先同步到本地後，再生成當天的 Review Quiz、Review Words、Speaking Bridge
- 不可用過期的本地 `learning.json` 直接產出當天教材，否則會讓 review 單字重複或狀態錯誤。
- Review Quiz、Review Words、Speaking Bridge 都必須從 `vocabulary/learning.json` 即時生成。
- 不要直接複製既有某一天頁面中的 review 內容。
- Speaking Bridge 不可使用今天剛新增的新單字，應依正式 SKILL 規則從 2–7 天前的單字中挑選。
- Speaking Bridge 的新情境若可選，優先偏向旅行口說、外出互動、資訊確認，而不是再次回到居家整理情境。
- 正式 SKILL 模板已搬到專案內 `.ai/daily-english-learning/SKILL.md`，後續以這份本地模板為主。

## 連載小說記憶規則（僅限使用者明確要求續寫時）

- 只有使用者明確要求產出連載 episode 時，才必須更新 `.ai/serial-story/CONTINUITY_LOG.md`。
- 若新增穩定設定、角色或故事規則，優先更新 `.ai/serial-story/SERIES_BIBLE.md` 或 `.ai/serial-story/STYLE_GUIDE.md`。
- 若只是每日事件、伏筆、下一集接點，寫入 `CONTINUITY_LOG.md`，不要塞進 `AGENTS.md`。
- 若使用者要求調整小說方向，先討論並更新 serial story 文件，再產出新 episode。

## 驗證與音檔

- 音檔生成使用 `edge_tts` 時，若失敗，優先檢查：
  - `edge_tts` 是否可 import
  - 網路是否被 sandbox 擋住
  - 是否需要提升權限執行
- 若要驗證本機 HTTP server，可注意 sandbox 對 localhost / loopback 可能有限制。

## 補充

- 本專案目前沒有 `README.md`，不要假設 repo 內已有完整操作說明。
- `SESSION_LEARNINGS_2026-04-02.md` 是歷史背景筆記，可能包含已過時路徑；正式規則一律以本檔與 `.ai/daily-english-learning/SKILL.md` 為準。
