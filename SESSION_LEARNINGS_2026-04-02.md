# 2026-04-02 實測記錄

## 目的

記錄今天在這個專案中實測、產出 test 成品、修正錯誤時學到的事，避免下次重犯。

## 今天確認到的事

- 這個專案的主 runtime 是靜態網站，不是需要 build 的 Node 或 Python 應用。
- 真正的正式產出手冊不在 repo 內，而在：
  - `/Users/mds-macm3pro/.claude/scheduled-tasks/daily-english-learning/SKILL.md`
- 若要做「正式學習材料」，必須依上面那份 SKILL 的 Step 0 到 Step 5 走，不能自行簡化成 demo。
- 正式產物必須包含：
  - `index.html`
  - `article.mp3`
  - `s01.mp3` 到 `sNN.mp3`
  - 完整區塊：Article、New Words、Key Phrases、Quiz、Active Recall Quiz、Speaking Bridge、Learning Tips、Review Words
- Review Quiz 與 Review Words 的來源應以 `vocabulary/learning.json` 現況為準，不應直接照抄某一天的既有 `daily/*/index.html`。
- `daily/2026-04-02/index.html` 和目前 `vocabulary/learning.json` 已存在不同步情況，因此：
  - 若要重生內容或做 test 版，應以 `learning.json` 為 source of truth
  - 不應把舊頁內容直接當成現在的正確狀態
- `edge_tts` 可以在本機使用，但在 sandbox 內連外會失敗；生成 MP3 時需要可用的網路權限。
- 在 sandbox 內做 localhost 驗證時，可能出現 loopback 受限；若要驗證本機 server，可能需要提升權限或改變驗證方式。

## 今天犯的錯

### 1. 沒先讀正式產出手冊

我一開始沒有先讀 `daily-english-learning/SKILL.md`，就直接做了一份 `test/english-practice-demo.html`。

結果：
- 內容格式和正式產物完全不同
- 沒有音檔
- 沒有逐句播放
- 沒有 Active Recall Quiz / Review Words / Speaking Bridge 的正式結構

### 2. 把「先看成果」誤解成「可隨意做 demo」

使用者要的是「照正式手冊產出一份完整可驗收的英文學習檔案」，不是隨意做一份預覽頁。

結果：
- 成果不符合專案脈絡
- 使用者看到後會覺得和正式系統完全不同

### 3. 一開始沒有先確認音檔是否必做

正式手冊明確要求 `article.mp3` 和 `s01.mp3` 到 `sNN.mp3`，但我第一次產出時完全沒做音檔。

這是明確漏步，不是小差異。

### 4. 差點直接沿用舊 daily 頁內容

在修正過程中，一度先拿 `daily/2026-04-02/index.html` 當骨架複製到 `test/`。

這個做法只能當版型骨架，不能直接當資料來源，因為：
- 頁面裡的 review 資料可能已落後
- `learning.json` 才是目前狀態

### 5. 對「資料來源優先順序」不夠嚴格

今天再次確認：
- 正式內容規格：以 `SKILL.md` 為準
- 複習資料現況：以 `vocabulary/learning.json` 為準
- `README.md` 目前不存在，不能假設 repo 內有正式說明文件

## 今天最後採取的正確做法

- 讀取 `profile.json`
- 讀取 `vocabulary/learning.json`
- 讀取正式產出手冊 `daily-english-learning/SKILL.md`
- 在 `test/2026-04-02-full/` 內產生完整測試版成果
- 生成：
  - `index.html`
  - `article.mp3`
  - `s01.mp3` 到 `s19.mp3`
- 驗收完成後，依使用者要求把 `test/` 整個刪除

## 下次執行規則

- 只要需求涉及「英文學習材料產出」，第一步先讀：
  - `/Users/mds-macm3pro/.claude/scheduled-tasks/daily-english-learning/SKILL.md`
- 若使用者要「先看成果」，也要先確認是：
  - 正式格式成果
  - 還是純 demo / 草稿
- 沒有得到明確允許前，不要自行降級成 demo。
- 凡是涉及 review 區塊、Active Recall Quiz、Speaking Bridge，都要以 `vocabulary/learning.json` 當前資料生成。
- 音檔是正式產物的一部分，不能省略。
- 若生成音檔失敗，要優先檢查：
  - `edge_tts` 是否可 import
  - 網路是否被 sandbox 擋住
  - 是否需要提升權限執行

## 補充

- 今天所有 test 成品已依使用者要求刪除。
- 目前工作樹為乾淨狀態。
