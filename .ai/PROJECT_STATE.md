# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-08-11
> 更新者：Agent

## 目前目標
- 維持靜態網站架構，將每日教材發展成以真實任務、可重用語塊、主動提取與 SRS 為核心的個人英文訓練系統。

## 目前進度
- [x] `The Blue Receipt` 已於 2026-07-14 Day 76 封存；正式內容已切換為 `mission-based`，不可自動續寫 Episode 19。
- [x] Mission、英文資訊輸入、Role-play、Context Recall、能力地圖、單字 / 句子 SRS 與音檔流程均已接通。
- [x] Day 77–95 已完成十九篇正式任務型教材；最新為 `daily/2026-08-11/` 的 `Taking a Harbor Ferry After a Pier Change`。
- [x] Day 91 是第一篇兩分鐘雙聲線教材：正文不顯示 `Staff:` / `Me:`，以 `traveler` / `staff` metadata 分別套用 Jenny 與 Guy。
- [x] Day 91 主播放器已加入跨裝置 `0.75× / 1× / 1.25×` 速度控制，完整文章與逐句播放共用同一速度；正式教材模板已同步。
- [x] Day 95 目標語塊 `round-trip ticket`、`Which pier does it leave from?`、`Could you show me on the map?` 已貫穿 Article、Key Phrases、Role-play 的「你」回合與 Context Recall。
- [x] Active Recall Quiz、Speaking Bridge、`vocabulary/learning.json` 與 `vocabulary/sentences.json` 保持 source-of-truth 與既有 SRS 邊界；未新增 Collocation SRS。
- [x] 使用者已確認後續教材統一採出國旅遊情境；Article 改以第一人稱現場任務為預設，真實資訊與 Staff 說法維持自然語氣。
- [x] 使用者已將後續主音檔改為約 2 分鐘；正式範圍定為 1:45–2:15，文章約 250–290 字、28–36 句，維持 A2 語速與每天 3 個新字。
- [x] 使用者回饋 Day 93 閱讀約懂七成，但聽力超過一半聽不懂；Day 94 先以 250 字、36 句、每句最多 9 字、控制式重複降低聽力負荷，不變更正式語速。

## 驗證狀態
- [x] Day 94 通過 `python3 scripts/validate_daily.py 2026-08-10`：84 checks、0 warnings、0 errors；主音檔 119.8 秒，36 句 / 250 字，37 個 MP3 均存在且可讀。
- [x] Day 94 包含 3 個新字、42 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge 與 8 回合 Role-play；390×844 手機版無橫向溢位，雙聲線、逐句播放、速度控制、測驗與首頁連結均已實測，console 0 errors。
- [x] Day 95 通過 `python3 scripts/validate_daily.py 2026-08-11`：84 checks、0 warnings、0 errors；主音檔 127.1 秒，36 句 / 254 字、每句最多 8 字，37 個 MP3 均存在且可讀。
- [x] Day 95 包含 3 個新字、15 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge 與 8 回合 Role-play；390×844 手機版無橫向溢位，速度按鈕可見且 0.75× 實際生效，console 0 errors。

## 目前 Blocker
- 無。

## 下一步
- 下一篇先看 Day 95 的理解回饋；若聽力仍低於約六成，優先再減少資訊密度與陌生搭配，不直接降低自然 A2 語速。
- 每篇維持 2–3 個目標語塊，至少 1 個支援開口、1 個支援資訊判讀，且至少 1 個要換人物、地點或目的做跨情境提取。
- Q2 預設測自然搭配 / 情境用法；Active Recall 納入所有到期舊字；Speaking Bridge 只選 2–7 天前且不可使用今日新字。
- 每日頁必須通過 `python3 scripts/validate_daily.py [日期]`；持續依回饋與卡點評估是否需要 UI、資料欄位或 Collocation SRS。

## 活躍工作區
- `daily/2026-08-11/`
- `index.html`
- `profile.json`
- `vocabulary/learning.json`
- `vocabulary/sentences.json`
- `ability_map.json`
- `.ai/daily-english-learning/SKILL.md`
- `scripts/validate_daily.py`
