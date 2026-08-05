# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-08-05
> 更新者：Agent

## 目前目標
- 維持靜態網站架構，將每日教材發展成以真實任務、可重用語塊、主動提取與 SRS 為核心的個人英文訓練系統。

## 目前進度
- [x] `The Blue Receipt` 已於 2026-07-14 Day 76 封存；正式內容已切換為 `mission-based`，不可自動續寫 Episode 19。
- [x] Mission、英文資訊輸入、Role-play、Context Recall、能力地圖、單字 / 句子 SRS 與音檔流程均已接通。
- [x] Day 77–91 已完成十五篇正式任務型教材；最新為 `daily/2026-08-05/` 的 `Buying Mobile Data at the Airport`。
- [x] Day 91 是第一篇兩分鐘雙聲線教材：正文不顯示 `Staff:` / `Me:`，以 `traveler` / `staff` metadata 分別套用 Jenny 與 Guy。
- [x] Day 91 主播放器已加入跨裝置 `0.75× / 1× / 1.25×` 速度控制，完整文章與逐句播放共用同一速度；正式教材模板已同步。
- [x] Day 91 目標語塊 `free setup`、`How much is it altogether?`、`Could you check it?` 已貫穿 Article、Key Phrases、Role-play 的「你」回合與 Context Recall。
- [x] Active Recall Quiz、Speaking Bridge、`vocabulary/learning.json` 與 `vocabulary/sentences.json` 保持 source-of-truth 與既有 SRS 邊界；未新增 Collocation SRS。
- [x] 使用者已確認後續教材統一採出國旅遊情境；Article 改以第一人稱現場任務為預設，真實資訊與 Staff 說法維持自然語氣。
- [x] 使用者已將後續主音檔改為約 2 分鐘；正式範圍定為 1:45–2:15，文章約 250–290 字、28–36 句，維持 A2 語速與每天 3 個新字。

## 驗證狀態
- [x] Day 90 通過 `python3 scripts/validate_daily.py 2026-08-04`：80 checks、0 warnings、0 errors；主音檔 177.2 秒，44 句 / 399 字，45 個 MP3 均存在且可讀。
- [x] Day 91 通過 `python3 scripts/validate_daily.py 2026-08-05`：84 checks、0 warnings、0 errors；主音檔 126.1 秒，34 句 / 251 字，35 個 MP3 均存在且可讀。
- [x] Day 91 包含 3 個新字、19 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge 與 10 回合 Role-play；桌面／手機瀏覽器畫面與逐句播放均已驗證。
- [x] 播放速度控制已在 390px 手機 viewport 驗證無橫向溢位；`0.75×` / `1.25×` 實際播放行為、按鈕狀態與瀏覽器 console 均通過。

## 目前 Blocker
- 無。

## 下一步
- 下一篇先同步最新 SRS，再依每週能力平衡安排出國旅遊口語或旅行資訊任務；Article 對話不顯示角色前綴並使用雙聲線，主音檔需通過 1:45–2:15 驗收，播放器保留跨裝置速度控制。
- 每篇維持 2–3 個目標語塊，至少 1 個支援開口、1 個支援資訊判讀，且至少 1 個要換人物、地點或目的做跨情境提取。
- Q2 預設測自然搭配 / 情境用法；Active Recall 納入所有到期舊字；Speaking Bridge 只選 2–7 天前且不可使用今日新字。
- 每日頁必須通過 `python3 scripts/validate_daily.py [日期]`；試行 7 篇後再依回饋與卡點評估是否需要 UI、資料欄位或 Collocation SRS。

## 活躍工作區
- `daily/2026-08-05/`
- `index.html`
- `profile.json`
- `vocabulary/learning.json`
- `vocabulary/sentences.json`
- `ability_map.json`
- `.ai/daily-english-learning/SKILL.md`
- `scripts/validate_daily.py`
