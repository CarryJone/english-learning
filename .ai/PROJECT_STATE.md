# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-07-24
> 更新者：Agent

## 目前目標
- 維持靜態網站架構，將每日教材發展成以真實任務、可重用語塊、主動提取與 SRS 為核心的個人英文訓練系統。

## 目前進度
- [x] `The Blue Receipt` 已於 2026-07-14 Day 76 封存；正式內容已切換為 `mission-based`，不可自動續寫 Episode 19。
- [x] Mission、英文資訊輸入、Role-play、Context Recall、能力地圖、單字 / 句子 SRS 與音檔流程均已接通。
- [x] Day 77–83 已完成七篇正式任務型教材；最新為 `daily/2026-07-24/` 的 `Checking a Store Return Policy`。
- [x] Day 81–83 正在進行 7 篇語塊深化試行（3/7）；Day 83 目標語塊為 `return policy`、`exchange this for a larger size`、`out of stock`。
- [x] 目標語塊已貫穿 Article、Key Phrases、Role-play 的 `You` 回合與 Context Recall，並以機場商店、鞋店與手機店做跨情境提取。
- [x] Active Recall Quiz、Speaking Bridge、`vocabulary/learning.json` 與 `vocabulary/sentences.json` 保持 source-of-truth 與既有 SRS 邊界；未新增 Collocation SRS。

## 驗證狀態
- [x] Day 83 通過 `python3 scripts/validate_daily.py 2026-07-24`：79 checks、0 warnings、0 errors。
- [x] Day 83 包含 3 個新字、9 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge、9 回合 Role-play 與 15 個非空音檔。
- [x] JSON 解析、內嵌 JavaScript 語法、`git diff --check` 與 MP3 格式均已通過；文章 14 句、120 字，最長句 11 字。
- [x] 今日 3 個目標語塊已分布在 Article、Key Phrases、Role-play 的 You 回合與 Context Recall，並以機場商店、鞋店與手機店做跨情境提取。

## 目前 Blocker
- 無。

## 下一步
- 產出 Day 84 前先同步最新 SRS，進行語塊深化試行第 4/7 篇，並依本週能力平衡選擇下一個旅行開口或英文資訊判讀任務。
- 每篇維持 2–3 個目標語塊，至少 1 個支援開口、1 個支援資訊判讀，且至少 1 個要換人物、地點或目的做跨情境提取。
- Q2 預設測自然搭配 / 情境用法；Active Recall 納入所有到期舊字；Speaking Bridge 只選 2–7 天前且不可使用今日新字。
- 每日頁必須通過 `python3 scripts/validate_daily.py [日期]`；試行 7 篇後再依回饋與卡點評估是否需要 UI、資料欄位或 Collocation SRS。

## 活躍工作區
- `daily/2026-07-24/`
- `index.html`
- `profile.json`
- `vocabulary/learning.json`
- `vocabulary/sentences.json`
- `ability_map.json`
- `.ai/daily-english-learning/SKILL.md`
