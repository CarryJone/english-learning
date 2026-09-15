# 專案當前狀態

> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-09-15
> 更新者：Agent

## 目前目標
- 維持靜態網站架構，將每日教材發展成以真實任務、可重用語塊、主動提取與 SRS 為核心的個人英文訓練系統。

## 目前進度
- [x] `The Blue Receipt` 已於 2026-07-14 Day 76 封存；正式內容為 `mission-based`，不可自動續寫 Episode 19。
- [x] Day 77–119 已完成四十三篇任務型教材；最新為 `daily/2026-09-15/` 的 `Splitting a Dinner Bill with a Service Charge`（M2，旅行開口日）。自然口語規則、四聲線與 Survival Lines 自 Day 117 起為常態流程。
- [x] 正式教材格式：角色／聲線以 `assets/voices.json` 為準（narrator=Jenny、traveler=Aria、staff=Guy、companion=Brian，一篇最多 4 個且一個 role 只能代表一個人）、正文不顯示角色前綴、主音檔 1:45–2:30、每天正好 3 個新字、2–3 個目標語塊貫穿 Article / Key Phrases / Role-play / Context Recall。
- [x] 主播放器支援 `0.75× / 1× / 1.25×`；Day 112 起可切換視覺句子重音。Mission、資訊輸入、Role-play、Context Recall、能力地圖、單字／句子 SRS 與音檔流程均已接通；未新增 Collocation SRS。
- [x] 2026-09-10 的長期決策（自然口語三規則＋口語片語、角色聲線契約、音檔 105–150 秒、Survival Lines）已寫入 `.ai/DECISIONS.md`；細節以 SKILL 3a.1 / 3a.2 / 3h.1 為準。
- [x] Survival Lines：`vocabulary/core-phrases.json` 34 句（第一批 18 句啟用中，第二批 16 句 `activateOn` 2026-10-01 自動加入），選句用 `scripts/pick_core_phrases.py`，音檔在 `assets/core/` 不需每天重生。
- [x] 模組近期採逐日輪替：Day 115 M2 → 116 M3 → 117 M1 → 118 M4 → 119 M2；下一篇依序可排 M3 `Problems & Repair`。

## 驗證狀態
- [x] Day 119（2026-09-15）通過 **97 checks** / 0 warnings / 0 errors；主音檔 137.57 秒、36 句 / 256 字、37 個 MP3 均可讀。
- [x] Day 119 實測：對話 **89%**、含縮寫句 **47%**、最長旁白連續 **1**；四聲線（staff＝服務生、companion＝同行朋友）；375px 無橫向溢位、console 0 errors、42 個音檔（含核心句）回 200。
- [x] Survival Lines 輪替正常：Day 119 換成 pay-by-card / say-again / speak-slowly / walking-distance / what-do-you-mean。Day 118 那批已標記使用但尚未同步 SRS（rc 仍為 0），代表學習者當天未作答該區。
- 每日驗證明細見 `.ai/WORKLOG.md`，本檔只保留最近狀態。

## 目前 Blocker
- 無。

## 已知問題
- Day 112 及更早的每日頁在 390px 下，Review Words 表格仍會造成約 13px 橫向溢位（共用 CSS 既有問題）。Day 113 起在當日頁加 `.review-table` 窄螢幕規則規避，尚未回頭修正舊頁。
- `validate_daily.py` 檢查「今日新字 `nextReview` = 建立日 +1」，學習者複習後日期會往後推，因此**任何頁面只能在建立當天通過驗證**。既有設計問題，尚未處理。
- 首頁學習記錄缺 `daily/2026-07-28/`（Day 85 `Reporting a Damaged Suitcase`）：118 筆連結對應 119 個資料夾。既有問題，尚未處理。
- 每日頁產生器（build_html / tts / update_data / core_block）只存在各 session 的 scratchpad，不在 repo；每個新 session 需重建或沿用前一輪暫存檔。

## 下一步
- 產出後優先收集「縮寫聽不聽得出來」與「聽力挑戰句第一次有沒有聽懂」兩項回饋。
- 句間停頓參數（0.05 / 0.12 / 0.25 秒）待使用者聽過後拍板；定案前不得調整，定案後再寫入 SKILL。
- 若聽力仍低於約六成，優先減少資訊密度與陌生搭配，不直接降低自然 A2 語速。
- 到期量波動大（Day 118 有 43 題、Day 119 只有 3 題）；若再出現單日 50 題以上，再評估 Active Recall 是否需要分批或分頁 UI。
- Speaking Bridge：同 reviewCount 層級中優先選尚未入選過的字，其次補「明天就離開 2–7 天視窗」的字；rc 較低的字即使前一天剛入選仍優先，Lv.2 必須換新情境。若要改成硬性「不得連續入選」，需先更新 SKILL。
- 到期字若與當天題材不合，依 SKILL「不要為了故事連貫硬塞」只融入自然的 2–3 個，其餘照常進 Active Recall 與 Review Words。
- 每篇維持 2–3 個目標語塊（至少 1 個開口、1 個資訊判讀，至少 1 個跨情境）；每日頁必須通過 `python3 scripts/validate_daily.py [日期]`。
- 可評估（需使用者同意）：把產生器腳本收進 repo `scripts/`，並補上首頁缺漏的 Day 85。

## 活躍工作區
- `daily/2026-09-15/`、`index.html`、`profile.json`、`ability_map.json`
- `vocabulary/learning.json`、`vocabulary/sentences.json`、`vocabulary/core-phrases.json`
- `.ai/daily-english-learning/SKILL.md`、`assets/voices.json`、`scripts/pick_core_phrases.py`、`scripts/validate_daily.py`
