# English Learning System Roadmap

> 用途：記錄此專案接下來要調整的學習系統方向、優先級與驗收重點。
> 注意：本檔是產品與系統改善計畫，不是每日教材格式規則；正式每日教材規格仍以 `AGENTS.md` 與 `.ai/daily-english-learning/SKILL.md` 為準。
> 最後更新：2026-07-07

## 核心判斷

- 不重新開發完整新系統。
- 沿用目前靜態網站、每日教材、SRS、連載故事與音檔產線。
- 將目前系統從「每日教材產生器」升級成「個人英文訓練作業系統」。
- 優先增加總控視角、複習閉環、能力地圖與驗證自動化。

## 使用者學習型態對應

使用者偏好系統理解、拆解卡點、看見回饋與持續優化。因此系統應提供：

- 清楚的每日目標。
- 可理解的複習規則。
- 看得見的進度與卡點。
- 穩定但可調整的訓練流程。
- 能累積複利的資料紀錄。
- 每週回顧與下一步調整。

## 需要調整的項目

### P0：入口與可視化

- [x] 首頁加入學習儀表板。
- [x] 首頁即時讀取 `profile.json` 與 `vocabulary/learning.json`。
- [x] 顯示累計天數、總單字、已掌握、今日到期、逾期、目前連載進度。
- [x] 首頁加入今日訓練路線。
- [x] 修正首頁今日日期使用 UTC 的風險，改用本機日期。

### P1：複習中心

- [x] 新增獨立 Review Center 頁面。
- [x] 顯示今日到期單字、逾期單字、未來 7 天複習量。
- [x] 讓使用者不用進入單日教材，也能完成當天 SRS 複習。
- [x] 將 Review Quiz 的同步邏輯整理成可共用模組。

### P1：能力地圖

- [x] 新增能力主線資料結構：
  - `travelSpeaking`
  - `publicEnglish`
  - `onlineReading`
  - `dailyResponse`
- [x] 每日教材標記主要訓練能力。
- [x] 首頁顯示本週各能力是否有被訓練到。

### P1：情境提取訓練

- [x] 每日教材加入 `Context Recall` 區塊，訓練中文情境 → 英文輸出。
- [x] 每篇至少 6 題，建議 8–10 題。
- [x] 題型分層：Lv.1 有提示、Lv.2 無提示、Lv.3 自由應答。
- [x] Day 72 已補入 8 題情境中翻英。

### P1：卡點與難度回饋

- [x] 每日教材結尾加入簡短回饋區：
  - 難度：太簡單 / 剛好 / 太難
  - 今日卡點：單字 / 聽力 / 口說 / 文章理解 / 句型
  - 今日最有用一句
- [x] 新增 `practice_log.json` 或等效資料來源。
  - 目前採 `localStorage` 過渡版，key 為 `english_learning_feedback_v1`，共用模組為 `assets/feedback.js`。
  - 原因：本專案是靜態網站，瀏覽器端不能直接寫回 repo 內的 JSON。
- [ ] 後續教材產出時讀取最近回饋，調整難度與題型。
  - 待補：若要讓產出 agent 穩定讀到瀏覽器回饋，需要新增匯出 / 同步機制，例如下載 JSON、GitHub API 同步或未來後端。

### P2：資料模型擴充

- [x] 保留 `vocabulary/learning.json` 作為單字 SRS source of truth。
- [ ] 新增片語資料來源，例如 `vocabulary/phrases.json`。
- [x] 新增實用句資料來源，例如 `vocabulary/sentences.json`。
- [x] 將高價值 survival sentence 納入間隔複習。
  - 初版已新增 `assets/sentence-srs.js`，可將 Context Recall 自評結果同步回 GitHub-backed `vocabulary/sentences.json`。
- [ ] 將 Speaking Bridge 從單字擴充到片語與句型。

### P2：產出驗證自動化

- [x] 新增每日教材驗證腳本。
  - 入口：`python3 scripts/validate_daily.py YYYY-MM-DD`
- [x] 檢查必要 HTML 區塊是否完整。
- [x] 檢查 `article.mp3` 與 `sNN.mp3` 是否存在。
- [x] 檢查句子編號是否連續。
- [x] 檢查今日新字是否沒有重複。
- [x] 檢查 Speaking Bridge 是否沒有使用今日新字。
- [x] 檢查能力地圖 session 與 `vocabulary/sentences.json` 是否和每日頁對齊。
- [ ] 檢查連載模式是否更新 `CONTINUITY_LOG.md`。

### P2：技術債整理

- [ ] 將每日頁面共用 CSS 抽成共享檔案。
- [ ] 將每日頁面共用 JS 抽成共享檔案。
- [ ] 保持既有 daily 頁可用，不做大規模歷史重寫。
- [ ] 新產出的 daily 頁先使用新版共享資源。

### P3：自動化與同步穩定性

- [ ] 重新評估排程任務失敗問題。
- [ ] 保留手動觸發備援。
- [ ] 新增產出後檢查與失敗提示。
- [ ] 若 GitHub API token 同步仍不穩，評估替代同步方式。

### P3：完整新 app 評估條件

只有當下列需求明確出現時，才考慮重開成完整 app：

- 多裝置同步。
- 登入帳號。
- 後端資料庫。
- 語音辨識與發音評分。
- AI 即時互動出題。
- 大量跨頁資料查詢與分析。

## 第一輪實作範圍

本輪先做 P0：

- 文件化完整調整清單。
- 首頁升級為儀表板入口。
- 顯示今日訓練路線。
- 使用現有 JSON 即時計算學習狀態。
- 不改每日教材格式。
- 不改 SRS source of truth。
- 不新增後端。

## 驗收標準

- 首頁可正常載入。
- 今日按鈕使用本機日期。
- 儀表板在 HTTP server 下可讀取 JSON 並顯示數字。
- 若 JSON 讀取失敗，首頁仍可使用且顯示保守提示。
- 既有學習記錄列表仍可點擊。
- 今日學習頁連結不受影響。
