# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-07-15
> 更新者：Agent

## 目前目標
- 將既有每日英文教材系統維持為靜態網站，升級成以真實任務、主動提取與 SRS 為核心的個人英文訓練系統。

## 目前進度
- [x] 已完成 2026-07-14 Day 76；`The Blue Receipt · Episode 18` 已作為第一季結尾封存。
- [x] `profile.json` 已切換為 `contentMode: mission-based`、`lastTopic: mission`，並保留小說封存資訊。
- [x] `.ai/daily-english-learning/SKILL.md` 已改為任務型每日規格：Mission、英文資訊輸入、Role-play、Context Recall 跨情境提取。
- [x] `AGENTS.md`、首頁儀表板與 `scripts/validate_daily.py` 已同步新模式；歷史小說頁仍保留相容性。
- [x] `.ai/serial-story/` 已明確標記封存；一般每日產出不可讀取或更新，除非使用者明確要求小說工作。
- [x] 既有 `vocabulary/learning.json`、`vocabulary/sentences.json`、音檔與 GitHub SRS 同步流程維持不變。
- [x] `test/2026-07-15/` 已完成任務型測試頁，包含從最新 SRS 預覽的 12 題 Active Recall Quiz、8 題 Context Recall、Role-play 與 20 個音檔；頁面只存本機測試狀態。
- [x] 已確認單字複習沿用既有 Active Recall Quiz：複習前面已學且到期的單字，不另設今日新字提取區塊。
- [x] 已完成 2026-07-15 Day 77 正式教材 `Finding the Right Bus`：3 個新字、12 題 SRS Active Recall、8 題 Context Recall、Role-play、19 個逐句音檔與首頁入口。

## 驗證狀態
- [x] `python3 scripts/validate_daily.py 2026-07-14` 在新驗證器下通過歷史格式相容檢查。
- [x] Day 77 任務型正式教材已通過 `validate_daily.py`：73 checks、0 warnings、0 errors。

## 目前 Blocker
- 無。

## 下一步
- 產出 Day 78：先同步最新 SRS，再依能力輪替安排旅行或英文資訊查詢任務。
- Day 78 必須包含 Mission、Role-play 至少 4 回合、Context Recall 至少 8 題，並通過 `validate_daily.py`。
- 新頁面需讓 Active Recall Quiz 從最新 SRS 動態載入所有到期單字；文章句子編號可保留資料順序，但不應在畫面顯示編號。
- 每週維持旅行開口 3 天、英文資訊判讀 2 天、整合任務 1 天、SRS／模擬複習 1 天。
- 不要從 `Remember` 線索續寫 Episode 19，也不要開第二季。

## 活躍工作區
- `daily/2026-07-14/`（最後一篇小說歷史教材）
- `daily/2026-07-15/`（第一篇任務型正式教材）
- `index.html`
- `profile.json`
- `vocabulary/learning.json`
- `vocabulary/sentences.json`
- `ability_map.json`
- `.ai/daily-english-learning/SKILL.md`
- `test/2026-07-15/`
