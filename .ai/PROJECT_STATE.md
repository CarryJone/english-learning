# 專案當前狀態
> 用途：短期狀態與下一步接手資訊。
> 注意：本檔不是開發規則；正式規則請看專案 `AGENTS.md`、`.ai/DECISIONS.md` 或指定的 `SKILL.md`。
> 最後更新：2026-10-29
## 目前目標
- 維持靜態網站架構，將每日教材發展成以真實任務、可重用語塊、主動提取與 SRS 為核心的個人英文訓練系統。
## 目前進度
- [x] Day 142（2026-10-29）完成 Getting Help When My Hotel Key Card Doesn’t Work（M3）；32 句／290 字、114.218 秒；20 到期字、4 Bridge、10 Context Recall、5 核心句。edge 三角色權限重試後皆 403，使用 Kokoro；98 checks／0 warnings／0 errors，33 MP3 解碼、文字／聲線與 JS 通過；375／390px 無溢位、倒數／速度／測驗正常，console 0 errors。
- [x] Day 141（2026-10-28）完成 Checking My Hotel Breakfast and Getting It to Go（M2）；32 句／292 字、124.428 秒；7 到期字、4 Bridge、10 Context Recall、5 核心句。edge 三角色權限重試後皆 403，使用 Kokoro；98 checks／0 warnings／0 errors，33 MP3 解碼、文字／聲線與 JS 驗證通過；375／390px 無溢位、倒數／速度／測驗正常，console 0 errors。
- [x] Day 140（2026-10-27）完成 Checking a Taxi Fare and Confirming My Hotel Drop-off（M1）；32 句／290 字、116.139 秒；64 到期字、4 Bridge、10 Context Recall、5 核心句。edge_tts 三角色皆 403，整篇使用 Kokoro，保留既定停頓；98 checks／0 warnings／0 errors、33 MP3 解碼與文字／聲線對照、JS 通過；375／390px 無溢位，倒數／速度／測驗操作正常、console 0 errors。
- [x] Day 139（2026-10-22）完成 Saving My Airport Bus Ticket for Offline Use（M4）；32 句／276 字、117.778 秒；20 到期字、4 Bridge、10 Context Recall、5 核心句。edge_tts 三角色皆 403，使用 Kokoro；98 checks／0 warnings／0 errors、33 MP3 解碼／文字與聲線對照／JS 通過，375／390px 無溢位、倒數／播放速度正常、console 0 errors。
- [x] Day 138（2026-10-21）完成 Returning a Damaged Gift and Asking for a Refund（M3）；32 句／290 字、118.730 秒；6 到期字、4 Bridge、10 Context Recall、5 核心句。edge_tts 三角色皆 403，使用 Kokoro；98 checks／0 warnings／0 errors、33 MP3 解碼／文字與聲線對照／JS 通過，375／390px 無溢位、倒數／播放速度正常、console 0 errors。
- [x] Day 137（2026-10-20）完成 Buying and Wrapping a Fragile Gift（M2）；32 句／289 字、122.982 秒；21 到期字、4 Bridge、10 Context Recall、5 核心句。edge_tts 7.2.8 三角色皆 403，改用 Kokoro；98 checks／0 warnings／0 errors、33 MP3 解碼／文字與聲線對照／JS 通過；375／390px 無溢位、倒數／播放速度正常、console 0 errors。
- [x] `The Blue Receipt` 已於 2026-07-14 Day 76 封存；正式內容為 `mission-based`，不可自動續寫 Episode 19。
- [x] Day 77–142 已完成六十六篇任務型教材；自然口語規則、多聲線與 Survival Lines 自 Day 117 起為常態流程。
- [x] 正式教材格式：角色／聲線以 `assets/voices.json` 為準（新頁依 kokoroVoice（af_sarah／af_heart／am_michael／am_fenrir）；歷史 edge 聲線保留，一篇最多 4 個且一個 role 只能代表一個人）、正文不顯示角色前綴、主音檔 1:45–2:30、每天正好 3 個新字、2–3 個目標語塊貫穿 Article / Key Phrases / Role-play / Context Recall。
- [x] 主播放器支援 `0.75× / 1× / 1.25×`；Day 112 起可切換視覺句子重音。Mission、資訊輸入、Role-play、Context Recall、能力地圖、單字／句子 SRS 與音檔流程均已接通；未新增 Collocation SRS。
- [x] 2026-09-10 的長期決策（自然口語三規則＋口語片語、角色聲線契約、音檔 105–150 秒、Survival Lines）已寫入 `.ai/DECISIONS.md`；細節以 SKILL 3a.1 / 3a.2 / 3h.1 為準。
- [x] Survival Lines：`vocabulary/core-phrases.json` 34 句（34 句自 2026-10-01 全數啟用，第二批 16 句已自動加入），選句用 `scripts/pick_core_phrases.py`，音檔在 `assets/core/` 不需每天重生。
- [x] 模組輪替最新狀態：Day 123 M4 → Day 124–125 M2 → Day 126 M3 → Day 127 M4；Day 128 M1 → Day 129 M2 → Day 130 M3 → Day 131 M4 `Travel Research & Instructions`。
## 驗證狀態
- [x] Survival Lines：09-15 與 09-17 有同步（09-17：could-you-help / didnt-catch / do-you-speak-english 皆 remembered），09-16 未同步。Day 122 換成 how-much / how-spell / id-like-this-one / pay-by-card / say-again。
- [x] 使用者回饋句子太黏：Kokoro 停頓已改為同角色 0.15／換人 0.25／段落 0.4 秒；語速 0.8 不變，98 checks 與 33 MP3 解碼通過。
## 目前 Blocker：無；Day 142 完成；提交紀錄以 git log 為準。
## 已知問題
- Day 112 及更早的每日頁在 390px 下，Review Words 表格仍會造成約 13px 橫向溢位（共用 CSS 既有問題）。Day 113 起在當日頁加 `.review-table` 窄螢幕規則規避，尚未回頭修正舊頁。
- Day 120 起把該規則的欄寬由 26/15/37/22% 調成 30/17/31/22%、縮小左右內距：19 個複習字時「詞性」欄原本會把 `adv./adj.` 拆成一字一行、長單字斷在字中間。只影響 Day 120 之後（以前一天頁面為模板）的新頁。
- `validate_daily.py` 檢查「今日新字 `nextReview` = 建立日 +1」，學習者複習後日期會往後推，因此**任何頁面只能在建立當天通過驗證**。既有設計問題，尚未處理。
- 首頁學習記錄缺 `daily/2026-07-28/`（Day 85 `Reporting a Damaged Suitcase`）：121 筆連結對應 122 個資料夾。既有問題，尚未處理。
## 下一步
- 2026-10-15 使用者指定每次先試 edge_tts，失敗才用 Kokoro；voices.json、AGENTS、正式 SKILL 已同步。今日重測仍 403，教材繼續使用已驗證的 Kokoro 音檔。
- **2026-09-18 學習者回饋**：同一篇重複跟讀、聽到很熟，但隔兩天再聽幾乎完全聽不懂，覺得失落。對照 SRS：單字 Active Recall 近 9 次 177/178 答對，卡點在聽力解碼（縮寫、連音、語速），不是字彙。已提出兩案待使用者決定：① 新增「聽力回聽」區塊（抽 2–7 天前原音先盲聽再看字，納入間隔複習）；② 主音檔句間停頓出學習版。決定前不改 SKILL。
- Kokoro 句間停頓已依使用者回饋確定為 0.15／0.25／0.4 秒，voices.json 與正式 SKILL 已同步。
- 若聽力仍低於約六成，優先減少資訊密度與陌生搭配，不直接降低自然 A2 語速。
- 到期量波動大：Day 118 有 43 題、Day 119 只有 3 題、Day 120 有 19 題、Day 121 有 14 題、Day 122 有 10 題；Day 126 升至 66 題並已全數收錄。依正式 SKILL 不可省略到期字，後續評估 Active Recall 的呈現方式。
- Speaking Bridge：同 reviewCount 層級中優先選尚未入選過的字，其次補「明天就離開 2–7 天視窗」的字；rc 較低的字即使前一天剛入選仍優先，Lv.2 必須換新情境。若要改成硬性「不得連續入選」，需先更新 SKILL。
- 到期字若與當天題材不合，依 SKILL「不要為了故事連貫硬塞」只融入自然的 2–3 個，其餘照常進 Active Recall 與 Review Words。
- 每篇維持 2–3 個目標語塊（至少 1 個開口、1 個資訊判讀，至少 1 個跨情境）；每日頁必須通過 `python3 scripts/validate_daily.py [日期]`。
- Kokoro 音檔產生器已收進 scripts/；首頁缺漏的 Day 85 仍待補。
## 活躍工作區
- 本機音檔：scripts/generate_daily_kokoro.py、scripts/KOKORO.md；設定 assets/voices.json。環境 .venv-tts/、模型 .tts-cache/ 已 gitignore。新頁 audio-provider=kokoro，舊頁按 edge 驗證。
- `daily/2026-10-29/`、`index.html`、`profile.json`、`ability_map.json`
- `vocabulary/learning.json`、`vocabulary/sentences.json`、`vocabulary/core-phrases.json`
- `.ai/daily-english-learning/SKILL.md`、`assets/voices.json`、`scripts/pick_core_phrases.py`、`scripts/validate_daily.py`
