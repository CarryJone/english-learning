# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-09-11
> 更新者：Agent

## 目前目標
- 維持靜態網站架構，將每日教材發展成以真實任務、可重用語塊、主動提取與 SRS 為核心的個人英文訓練系統。

## 目前進度
- [x] `The Blue Receipt` 已於 2026-07-14 Day 76 封存；正式內容為 `mission-based`，不可自動續寫 Episode 19。
- [x] Day 77–117 已完成四十一篇任務型教材；最新為 `daily/2026-09-11/` 的 `Making a Tight Connection in Hong Kong`，是**首篇同時套用自然口語規則、四聲線與 Survival Lines** 的教材。
- [x] 正式教材格式：角色／聲線以 `assets/voices.json` 為準（narrator=Jenny、traveler=Aria、staff=Guy、companion=Brian，一篇最多 4 個且一個 role 只能代表一個人）、正文不顯示角色前綴、主音檔 1:45–2:30、每天正好 3 個新字、2–3 個目標語塊貫穿 Article / Key Phrases / Role-play / Context Recall。
- [x] 主播放器支援 `0.75× / 1× / 1.25×`；Day 112 起可切換視覺句子重音。Mission、資訊輸入、Role-play、Context Recall、能力地圖、單字／句子 SRS 與音檔流程均已接通；未新增 Collocation SRS。
- [x] Day 110 起主音檔加入句間停頓試行：同聲線約 0.05 秒、換人約 0.12 秒、階段切換約 0.25 秒；逐句音檔不加停頓。2026-09-10 已把現行參數記入 SKILL Step 5 並標明「尚未定案、後續 session 不得自行調整」，仍待使用者拍板。
- [x] 2026-09-10 依使用者評估「文章偏學習課文而非真實口語」，導入自然口語規則（SKILL 3a.1）：① 全篇口語縮寫；② 對話句 ≥60%、旁白 ≤40% 且不得逐條唸 input snippet；③ staff 用真實服務業口語，每篇 1 處聽力挑戰句後接 repair 與 10 字內重述。2026-09-11 起生效。
- [x] 2026-09-10 建立 `assets/voices.json` 作為角色／聲線唯一事實來源，新增第四聲線 `companion`（Brian）＝**本篇第二個說話者**（同行朋友，或第二個場景的另一位服務人員）；`article.mp3` 範圍放寬為 105–150 秒。同日另加規則：動詞優先選日常口語片語（`get off work` / `drop off` / `pick up`），不用標準單動詞。
- [x] 2026-09-10 新增 `Survival Lines` 核心句訓練區塊（2026-09-11 起生效）：`vocabulary/core-phrases.json` 收 34 句旅行核心句（第一批 18 句立即啟用，第二批 16 句 `activateOn` 設 2026-10-01 自動加入），每天抽 5 句做倒數反射練習；音檔 41 個一次性存於 `assets/core/`，不需每天重生。選句用 `scripts/pick_core_phrases.py`。
- [x] 上述兩項已寫入 `.ai/DECISIONS.md`（2026-09-10）作為長期決策；規則細節以 SKILL 3a.1 / 3a.2 為準。

## 驗證狀態
- [x] Day 117（2026-09-11）通過 **97 checks** / 0 warnings / 0 errors（新規則帶來 13 項新檢查）；主音檔 139.51 秒、36 句 / 273 字、37 個 MP3 均可讀。
- [x] Day 117 實測新規則全數達標：對話 **77%**（門檻 60%）、含縮寫句 **55%**（門檻 15%）、最長旁白連續 **3**（上限 3）、四聲線（narrator / traveler / staff＝轉機櫃檯 / companion＝登機門地勤）。
- [x] Day 117 的 Survival Lines 實測：倒數→揭示→評分→同步鈕解鎖全流程正常、核心句音檔 200、框架句正確取用第 1 個變化；375px 無橫向溢位、console 0 errors。
- 每日驗證明細見 `.ai/WORKLOG.md`，本檔只保留最近狀態。

## 目前 Blocker
- 無。

## 已知問題
- Day 112 及更早的每日頁在 390px 下，Review Words 表格仍會造成約 13px 橫向溢位（共用 CSS 的既有問題）。Day 113 已在當日頁加入只作用於 `.review-table` 的窄螢幕欄寬規則規避，尚未回頭修正舊頁或共用模板。
- `validate_daily.py` 檢查「今日新字的 `nextReview` = 建立日 +1」，但學習者複習後 SRS 會把日期往後推，因此**任何頁面只能在建立當天通過驗證**，隔幾天重跑必定失敗（例：Day 113 的 insert / medium / space）。屬既有設計問題，與 2026-09-10 的規則變更無關，尚未處理。

## 下一步
- Day 117 起照自然口語規則產出；產出後優先收集「縮寫聽不聽得出來」與「聽力挑戰句第一次有沒有聽懂」兩項回饋。
- 句間停頓參數（0.05 / 0.12 / 0.25 秒）待使用者聽過後拍板；定案前不得調整。
- 先看 Day 113–116 的理解與視覺重音回饋；若聽力仍低於約六成，優先再減少資訊密度與陌生搭配，不直接降低自然 A2 語速。
- 到期量波動大（Day 113 有 60 題、Day 114 只有 3 題、Day 115 與 116 各 12 題）；若之後再出現單日 50 題以上，再評估 Active Recall 是否需要分批或分頁 UI。
- Speaking Bridge 候選 reviewCount 常常全部同分。Day 115 起的做法是：同層級中優先選尚未入選過的字，其次補「明天就離開 2–7 天視窗」的字。仍符合 SKILL 的 reviewCount 優先規則；若要改成硬性「同一字不得連續入選」，需先更新 SKILL。
- 到期字常整批來自同一個舊主題（例如 Day 116 的 12 個到期字集中在飯店冷氣、單車、購物）。當它們與當天新題材不合時，依 SKILL「不要為了故事連貫硬塞」只融入自然的 2–3 個，其餘仍照常進 Active Recall 與 Review Words。
- 依實際聆聽回饋決定是否把停頓參數正式寫入 `.ai/daily-english-learning/SKILL.md`。
- 每篇維持 2–3 個目標語塊，至少 1 個支援開口、1 個支援資訊判讀，且至少 1 個換人物、地點或目的做跨情境提取。
- 每日頁必須通過 `python3 scripts/validate_daily.py [日期]`。

## 活躍工作區
- `daily/2026-09-11/`
- `index.html`
- `profile.json`
- `vocabulary/learning.json`
- `vocabulary/sentences.json`
- `ability_map.json`
- `.ai/daily-english-learning/SKILL.md`
- `assets/voices.json`
- `vocabulary/core-phrases.json`
- `scripts/pick_core_phrases.py`
- `scripts/validate_daily.py`
