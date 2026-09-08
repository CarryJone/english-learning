# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-09-08
> 更新者：Agent

## 目前目標
- 維持靜態網站架構，將每日教材發展成以真實任務、可重用語塊、主動提取與 SRS 為核心的個人英文訓練系統。

## 目前進度
- [x] `The Blue Receipt` 已於 2026-07-14 Day 76 封存；正式內容為 `mission-based`，不可自動續寫 Episode 19。
- [x] Day 77–114 已完成三十八篇任務型教材；最新為 `daily/2026-09-08/` 的 `Booking a Dinner Table After Reading Reviews`。
- [x] 正式教材格式已穩定：三聲線（narrator=Jenny、traveler=Aria、staff=Guy）、正文不顯示角色前綴、主音檔 1:45–2:15、每天正好 3 個新字、2–3 個目標語塊貫穿 Article / Key Phrases / Role-play / Context Recall。
- [x] 主播放器支援 `0.75× / 1× / 1.25×`；Day 112 起頁面提供可切換的視覺句子重音，逐句播放會標亮目前句子。
- [x] Mission、英文資訊輸入、Role-play、Context Recall、能力地圖、單字 / 句子 SRS 與音檔流程均已接通；未新增 Collocation SRS。
- [x] Day 110 起主音檔加入句間停頓試行：同聲線約 0.05 秒、換人約 0.12 秒、階段切換約 0.25 秒；逐句音檔不加停頓，參數尚未寫入正式 SKILL。

## 驗證狀態
- [x] Day 114 通過 `python3 scripts/validate_daily.py 2026-09-08`：84 checks、0 warnings、0 errors；主音檔 132.34 秒，35 句 / 274 字、每句最多 10 字，36 個 MP3 均存在且可讀。
- [x] Day 114 包含 3 個新字、3 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge 與 10 回合 Role-play；375px 手機寬度無橫向溢位、console 0 errors、首頁最新一筆為 Day 114。
- [x] Day 113（2026-09-07）先前同樣通過 84 checks；主音檔 129.63 秒、35 句 / 285 字、60 題到期 Active Recall。
- 更早的每日驗證紀錄已移至 `.ai/WORKLOG.md`，本檔只保留最近兩天。

## 目前 Blocker
- 無。

## 已知問題
- Day 112 及更早的每日頁在 390px 下，Review Words 表格仍會造成約 13px 橫向溢位（共用 CSS 的既有問題）。Day 113 已在當日頁加入只作用於 `.review-table` 的窄螢幕欄寬規則規避，尚未回頭修正舊頁或共用模板。

## 下一步
- 先看 Day 113、114 的理解、停頓與視覺重音回饋；若聽力仍低於約六成，優先再減少資訊密度與陌生搭配，不直接降低自然 A2 語速。
- 到期量在 Day 113 曾達 60 題、Day 114 只剩 3 題，落差很大；若之後再出現單日 50 題以上，再評估 Active Recall 是否需要分批或分頁 UI。
- Speaking Bridge 候選池目前偏小，`pedal` / `brake` / `helmet` 已連兩天入選（Lv.2 情境每天重寫）；若使用者覺得重複，可討論是否改為「同一字最多連續入選一次」。
- 依實際聆聽回饋決定是否把停頓參數正式寫入 `.ai/daily-english-learning/SKILL.md`。
- 每篇維持 2–3 個目標語塊，至少 1 個支援開口、1 個支援資訊判讀，且至少 1 個換人物、地點或目的做跨情境提取。
- 每日頁必須通過 `python3 scripts/validate_daily.py [日期]`。

## 活躍工作區
- `daily/2026-09-08/`
- `index.html`
- `profile.json`
- `vocabulary/learning.json`
- `vocabulary/sentences.json`
- `ability_map.json`
- `.ai/daily-english-learning/SKILL.md`
- `scripts/validate_daily.py`
