# AGENTS.md — english-learning 專案規則

## 專案性質

- 這個專案的主 runtime 是靜態網站。
- 不要把它當成需要 build 的 Node / Python app。
- 可執行入口以靜態 HTML 與本機 HTTP server 為主。

## 英文學習材料產出規則

- 只要需求涉及「每日英文學習材料」、「英文練習頁」、「正式學習內容產出」，第一步必讀：
  - `.ai/daily-english-learning/SKILL.md`
- 正式產出必須依上面那份 SKILL 的流程執行，不可自行簡化成 demo。
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

- Review Quiz、Review Words、Speaking Bridge 都必須從 `vocabulary/learning.json` 即時生成。
- 不要直接複製既有某一天頁面中的 review 內容。
- Speaking Bridge 不可使用今天剛新增的新單字，應依正式 SKILL 規則從 2–7 天前的單字中挑選。
- 正式 SKILL 模板已搬到專案內 `.ai/daily-english-learning/SKILL.md`，後續以這份本地模板為主。

## 驗證與音檔

- 音檔生成使用 `edge_tts` 時，若失敗，優先檢查：
  - `edge_tts` 是否可 import
  - 網路是否被 sandbox 擋住
  - 是否需要提升權限執行
- 若要驗證本機 HTTP server，可注意 sandbox 對 localhost / loopback 可能有限制。

## 補充

- 本專案目前沒有 `README.md`，不要假設 repo 內已有完整操作說明。
- 今天的背景筆記可參考：
  - `SESSION_LEARNINGS_2026-04-02.md`
