# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-08-04
> 更新者：Agent

## 目前目標
- 維持靜態網站架構，將每日教材發展成以真實任務、可重用語塊、主動提取與 SRS 為核心的個人英文訓練系統。

## 目前進度
- [x] `The Blue Receipt` 已於 2026-07-14 Day 76 封存；正式內容已切換為 `mission-based`，不可自動續寫 Episode 19。
- [x] Mission、英文資訊輸入、Role-play、Context Recall、能力地圖、單字 / 句子 SRS 與音檔流程均已接通。
- [x] Day 77–90 已完成十四篇正式任務型教材；最新為 `daily/2026-08-04/` 的 `Choosing an Airport Ride After a Stop Change`。
- [x] Day 90 是第一篇三分鐘規格教材：第一人稱比較機場火車與接駁車，並處理 Stop 6 改為 Stop 8 / Door 4 的資訊變更。
- [x] Day 90 目標語塊 `compare the options`、`How long does it take?`、`Where does it leave from?` 已貫穿 Article、Key Phrases、Role-play 的 `You` 回合與 Context Recall。
- [x] Active Recall Quiz、Speaking Bridge、`vocabulary/learning.json` 與 `vocabulary/sentences.json` 保持 source-of-truth 與既有 SRS 邊界；未新增 Collocation SRS。
- [x] 使用者已確認後續教材統一採出國旅遊情境；Article 改以第一人稱現場任務為預設，真實資訊與 Staff 說法維持自然語氣。
- [x] 使用者已確認主音檔由約 1 分鐘延長為約 3 分鐘；正式範圍定為 2:45–3:15，維持 A2 語速、每天 3 個新字，靠三段式任務與控制式重複增加有效內容。

## 驗證狀態
- [x] Day 89 通過 `python3 scripts/validate_daily.py 2026-08-03`：79 checks、0 warnings、0 errors；包含 3 個新字、46 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge、12 回合 Role-play 與 17 個非空音檔。
- [x] 已量測最近 8 篇 `article.mp3` 為 49.8–63.2 秒，確認現行 90–140 字規格確實約 1 分鐘；正式內容規格已改為約 390–430 字，並新增 165–195 秒驗收門檻。
- [x] Day 90 通過 `python3 scripts/validate_daily.py 2026-08-04`：80 checks、0 warnings、0 errors；主音檔 177.2 秒，44 句 / 399 字，45 個 MP3 均存在且可讀。
- [x] Day 90 包含 3 個新字、9 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge 與 10 回合 Role-play；首頁及 SRS / 能力資料均已同步。

## 目前 Blocker
- 無。

## 下一步
- 下一篇先同步最新 SRS，再依每週能力平衡安排出國旅遊開口或旅行資訊判讀任務；Article 使用第一人稱三段式現場任務，實際主音檔需通過 2:45–3:15 驗收。
- 每篇維持 2–3 個目標語塊，至少 1 個支援開口、1 個支援資訊判讀，且至少 1 個要換人物、地點或目的做跨情境提取。
- Q2 預設測自然搭配 / 情境用法；Active Recall 納入所有到期舊字；Speaking Bridge 只選 2–7 天前且不可使用今日新字。
- 每日頁必須通過 `python3 scripts/validate_daily.py [日期]`；試行 7 篇後再依回饋與卡點評估是否需要 UI、資料欄位或 Collocation SRS。

## 活躍工作區
- `daily/2026-08-04/`
- `index.html`
- `profile.json`
- `vocabulary/learning.json`
- `vocabulary/sentences.json`
- `ability_map.json`
- `.ai/daily-english-learning/SKILL.md`
- `scripts/validate_daily.py`
