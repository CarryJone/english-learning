# 工作日誌

> 用途：記錄已發生的近期工作事件，最新紀錄放最上方。
> 注意：本檔不是開發規則、不是待辦清單、不是規格來源；不要依本檔決定實作方式。
> 維護：超過 30 筆時，建議歸檔到 `.ai/archive/WORKLOG_YYYY_MM.md`。

---
## 2026-09-10 — 教材口語自然度規則與角色聲線契約

- 使用者要求評估「產出的文章是否為日常對話會用到的英文，還是比較像學習課文」。實測最近六天 206 句：旁白佔 57%（其中 43 句只是在唸畫面上的字）、含縮寫的句子 0%、34 個問句中 `Could I/you` 佔 35%。判定為偏學習課文。
- 使用者確認 A（縮寫）、B（對話比例）、C（工作人員語域）三項全做，規則寫入 `.ai/daily-english-learning/SKILL.md` 新增的 3a.1，並同步 Step 2.5、Step 7b 與 `AGENTS.md`；2026-09-11 起生效。
- `scripts/validate_daily.py` 新增 `validate_natural_speech()`：對話句 <60% 與含縮寫句 <15% 直接報錯，旁白連續 >3 句發警告。以 `NATURAL_SPEECH_START_DATE = 2026-09-11` 為閘門，已實測舊頁面不受影響。
- 在對話中產出兩版示範文章供使用者審閱，未寫入任何 `daily/` 頁面。第一版仍有殘留課文感：`as soon as possible` 被硬塞進司機台詞、為了塞複習字 `amount` 造出假動作、0 個短回應與 0 個 back-channel。第二版修掉後短語單位 7→12、社交潤滑句 3→9、書面語殘留 2→0。
- 發現並記錄一個規則漏洞：部分單字天生屬書面語域（例如 `reply`），放在螢幕文字與旅客問句自然，放進服務人員嘴裡就假。修法是換位置，不是拿掉該字。
- **使用者指出示範文章中朋友與司機共用 `staff`＝Guy，同一個聲音演兩個人。** 確認屬實，是引入朋友角色時造成的缺陷。
- 新增 `assets/voices.json` 作為角色／聲線唯一事實來源，新增第四角色 `companion`（同行朋友）＝`en-US-BrianNeural`；使用者聽過 Brian / Roger / Eric / Emma 四個候選後選定 Brian。
- 防止後續 session 亂用的三層機制：① `assets/voices.json` 單一來源，SKILL 的 TTS 範例改為從該檔讀取、不再寫死；② 驗證腳本從該檔讀角色白名單，自創角色名稱直接報錯；③ 頁面 `<head>` 必須宣告 `<meta name="voice-map">`，驗證腳本與 JSON 逐項交叉比對。已實測可擋下「漏宣告角色」「聲線用錯」「缺 meta」三種錯誤。
- 使用者同意時長放寬，`article.mp3` 正式範圍由 105–135 秒改為 **105–150 秒**，SKILL、`AGENTS.md`、驗證腳本三處同步。
- 順帶修掉自己引入的 bug：對話比例原本只計 `traveler` + `staff`，`companion` 未計入，導致比例由 83% 誤報為 69%。
- 把 Day 110 起實際在用的句間停頓（同聲線 0.05 / 換人 0.12 / 階段切換 0.25 秒）記入 SKILL Step 5，並標明尚未定案、後續 session 不得自行調整，避免規格與實際產出脫節。
- 發現既有問題（非本次造成）：驗證腳本檢查「今日新字 `nextReview` = 建立日 +1」，但複習後 SRS 會把日期往後推，因此舊頁面隔天以後重跑必定失敗。已記入 `PROJECT_STATE.md` 已知問題，未處理。
- 使用者提出三項口語化建議並附實戰對話劇本。評估後：`get off work` / `drop it off` 採納（且 `get off` 已教過，是既有片語的延伸）；語氣詞採納；`cab` 建議降為辨識字（`taxi` 國際通用）；**`grab it back` 不採納**——`grab` 帶「搶回」語感，領取失物的道地說法是 `pick it up` / `get it back`，使用者自己的劇本裡寫的也是 `pick it up`。
- 使用者的兩階段劇本（電話聯絡 → 現場領回）暴露出前一版規則的漏洞：原本寫「若出現第二個服務方，該篇不得使用 companion」，但那樣兩個服務方仍會共用 `staff`＝Guy，等同未解決「同一個聲音演兩個人」。
- 依使用者指示先做兩項：① `companion` 定義由「同行者（朋友）」放寬為「**本篇第二個說話者**」，可以是同行朋友或第二個場景的另一位服務人員；出現第二個服務方時必須用 companion，不可共用 staff；若同時需要朋友與第二服務方（5 個說話者）則須重構情境。② 新增 SKILL 3a.1 規則 D「動詞優先選日常口語片語」，附 6 組對照表與「不得為了口語選少見俚語」的但書。
- 四份文件（`assets/voices.json`、SKILL 3a.1／3a.2／3c／Step 7b、`AGENTS.md`、`.ai/DECISIONS.md`）已同步，實測無舊敘述殘留。DECISIONS 的同日條目直接標註修正原因，保留為何改的脈絡。
- 使用者暫緩的三項：Role-play 獨立規則（多句回合、兩個場景）、語氣詞加密、地區變體處理原則（`cab`）。
- 使用者提出「每天一句高頻日常句、重複出現加深記憶」的想法。實測 116 篇文章後發現這個效果**已經存在但是意外產生的**：SKILL 規定每篇要有 repair 句，導致 `say that again` 出現 16 篇（09-07／09-09／09-10 連三天），但 `What do you mean?` 只 1 篇、`Here you go`／`How are you` 各 0 篇——有效果，但分配極不均。
- 使用者選擇做成獨立練習區塊而非放進文章，並補充 12 句（餐廳／住宿／方向／應急）。評估後採納 10 句、`Can I have the menu` 升級為框架句 `Can I have ..., please?`（一格換六種用法）、`I'd like to check in` 補 `I have a reservation under ...`；**`Turn left / Go straight` 不採納**——那是聽的不是說的，放進產出練習會錯位，改成 `Is it left or right?`。
- 新增 `Survival Lines` 區塊（Speaking Bridge 之後、Role-play 之前）：中文情境 → 倒數 5 秒 → 顯示答案並自動播音 → 三段自評 → 同步 SRS。倒數可切 3／5／8 秒，預設 5 秒（不用影片建議的 3 秒：A2 從零產出整句需要更久，3 秒會每題都失敗）。
- 資料與資產：`vocabulary/core-phrases.json`（34 句，第一批 18 句立即生效、第二批 16 句 `activateOn` 2026-10-01 自動加入輪替）、`assets/core/*.mp3`（41 個變化，Aria 聲線，一次性生成）、`assets/core-drill.js`（170 行）、`scripts/pick_core_phrases.py`（選句 CLI，避免邏輯只存在於 session）。
- SRS 直接複用 `assets/sentence-srs.js` 引擎，只換 `filePath` 與間隔 `[1,2,4,7,14,30,60]`（反射句要比一般句子更常回來），沒有另寫一套。
- 驗證腳本新增 `validate_core_phrases()`：Survival Lines 區塊必須存在、`data-core-ids` 不重複、句子必須存在於 JSON、不可使用未到 `activateOn` 的第二批句子、當天 `lastUsedOn` 必須已更新。四種錯誤情境實測皆正確攔截。
- 瀏覽器實測（375px）：倒數→揭示→評分→下一句→同步鈕解鎖全流程正常，音檔回 200，console 0 errors，無橫向溢位；`applySentenceResults` 對 remembered／forgot 產生的間隔正確。
- 驗證：voice-map 交叉比對實測「司機=staff／櫃檯=companion」PASS、「兩個服務方共用 Guy」報錯；Day 116 仍 PASS。
- 驗證：Day 115、116 於規則變更後仍 PASS；`assets/voices.json` JSON 合法；SKILL 內嵌 TTS 範例程式通過 `ast.parse`；四種 voice-map 錯誤情境行為符合預期。本次未產出每日教材，未修改任何 `daily/` 頁面。

## 2026-09-10 — Day 116 正式教材產出

- 先 `git fetch` 再 `git pull --ff-only`，同步遠端 `SRS update: review quiz 2026-09-09`，才依最新 `vocabulary/learning.json` 生成今日複習內容；今日到期舊單字 12 個。
- 新增 `daily/2026-09-10/`，主題為 `Getting Back a Phone Left in a Taxi`；今日新字：`lost`、`contact`、`reply`。
- 本週能力平衡補上「整合任務」這一格：先用朋友的手機讀叫車 app 的 Lost item help 頁（四個步驟、24 小時回覆、$15 歸還費、失物招領處 9–18 點），再照步驟回報並與司機通話；司機今晚無法送回造成一次資訊改變，改約失物招領處。
- 今日目標語塊：`I left my ... in ...`（開口）、`lost and found`（資訊判讀）、`get it back`（處理後續）；三者都出現在 Article、Key Phrases、Role-play 的「你」回合與 Context Recall，前兩者各有一題跨情境轉移（背包忘在火車上、行李箱送錯飯店）。
- 能力標記以 `onlineReading` + `travelSpeaking` 為 primary，`dailyResponse`、`publicEnglish` 為次要；`profile.json.currentModule` 由 `Hotels, Food & Shopping` 轉到 `Problems & Repair`（M3）。
- 今日 12 個到期字集中在舊主題（飯店冷氣 noise / maintenance / fan、單車 pedal / brake / helmet、購物 stock / tight / sale），與計程車失物情境不合。依 SKILL「不要為了故事連貫硬塞」只自然融入 `amount` 與 `tight`（時間很趕的用法），其餘 10 個仍照常進 Active Recall 與 Review Words。
- Speaking Bridge 取 `review`、`book`、`cancel`（2 天前，尚未入選過）與 `helmet`（7 天前，明天離開 2–7 天視窗）。九個候選 reviewCount 同為 1，沿用 Day 115 的做法：同層級優先選沒練過的字，再補即將離開視窗的字。
- 音檔沿用三聲線與句間停頓試行（同聲線 0.05 秒、換人 0.12 秒、階段切換 0.25 秒）；主音檔 127.95 秒、35 句 / 281 字、每句最多 10 字。
- 驗證：`python3 scripts/validate_daily.py 2026-09-10` 84 checks / 0 warnings / 0 errors；本機 HTTP server 上 375px 無橫向溢位、console 0 errors、`article.mp3` 與 `s01.mp3`–`s35.mp3` 均回 200、單字 / 複習字 / 片語彈窗查詢全部命中、首頁最新一筆為 Day 116。

## 2026-09-09 — Day 115 正式教材產出

- 先 `git fetch` 再 `git pull --ff-only`，同步遠端 `SRS update: review quiz 2026-09-08`，才依最新 `vocabulary/learning.json` 生成今日複習內容；今日到期舊單字 12 個（9 個小說時期 rc=4 舊字加上昨日 3 個新字）。
- 新增 `daily/2026-09-09/`，主題為 `Buying a Warm Jacket After the Weather Turns Cold`；今日新字：`stock`、`tight`、`sale`。
- 任務是旅途變冷後在戶外用品店買外套：從吊牌與店內告示找出 $49、試衣間一次三件、14 天憑收據退換與「特價品不退不換」，再開口試穿；大號深藍缺貨造成一次資訊改變，改問其他顏色。
- 今日目標語塊：`try it on`（開口）、`out of stock`（資訊判讀）、`Do you have it in ...?`（提出替代方案）；三者都出現在 Article、Key Phrases、Role-play 的「你」回合與 Context Recall，後兩者各有一題跨情境轉移（紀念品店問顏色、網路商店確認缺貨）。
- 文章融入複習字 `bring`、`final`、`instead`，三個都能自然落在退換規則與換顏色的句子裡。
- 能力標記以 `travelSpeaking` + `dailyResponse` 為 primary（`dailyResponse` 久未當主要能力），`publicEnglish`、`onlineReading` 為次要；`profile.json.currentModule` 由 `Travel Research & Instructions` 轉到 `Hotels, Food & Shopping`（M2）。
- Speaking Bridge 取 `insert`、`medium`、`space`（2 天前，rc=1，尚未入選過）與 `brake`（6 天前，rc=1，明天離開 2–7 天視窗）。六個候選 reviewCount 同為 1，故在同層級中優先選尚未練過的字，藉此避開連三天重複 `pedal` / `brake` / `helmet`。
- 音檔沿用三聲線與句間停頓試行（同聲線 0.05 秒、換人 0.12 秒、階段切換 0.25 秒）；主音檔 124.92 秒、35 句 / 273 字、每句最多 11 字。
- 驗證：`python3 scripts/validate_daily.py 2026-09-09` 84 checks / 0 warnings / 0 errors；本機 HTTP server 上 375px 無橫向溢位、console 0 errors、`article.mp3` 與 `s01.mp3`–`s35.mp3` 均回 200、單字 / 複習字 / 片語彈窗查詢全部命中、首頁最新一筆為 Day 115。

## 2026-09-08 — Day 114 正式教材產出

- 先 `git fetch` 再 `git pull --ff-only`，同步遠端 `SRS update: review quiz 2026-09-07`（昨天 60 題 Active Recall 已作答並更新間隔），才依最新 `vocabulary/learning.json` 生成今日複習內容。
- 今日到期舊單字只剩 3 個（`insert`、`medium`、`space`，皆為昨日新字），Active Recall 與 Review Words 都是 3 題。
- 新增 `daily/2026-09-08/`，主題為 `Booking a Dinner Table After Reading Reviews`；今日新字：`review`、`book`、`cancel`。
- 任務是用手機讀地圖搜尋結果、三則評論與訂位規則頁，找出 15 分鐘保留、三小時前免費取消與「早點訂 / 指定室內座位」建議，再打電話訂位；七點半訂滿與室內座位時段不同各造成一次資訊改變。
- 今日目標語塊：`book a table`（開口）、`free cancellation`（資訊判讀）、`Could I change it to ...?`（處理資訊改變）；三者都出現在 Article、Key Phrases、Role-play 的「你」回合與 Context Recall，後兩者各有一題跨情境轉移（機場接送改時間、訂房頁確認免費取消）。
- 能力標記以 `onlineReading` + `travelSpeaking` 為 primary，`dailyResponse`、`publicEnglish` 為次要；`profile.json.currentModule` 由 `Transport & Getting Around` 轉到 `Travel Research & Instructions`（M4）。
- 文章只融入 `medium`、`space` 兩個複習字；`insert` 在餐廳訂位情境找不到自然用法，依 SKILL「不要為了故事連貫硬塞」的規則不強行放入，該字仍出現在 Active Recall 與 Review Words。
- Speaking Bridge 取 `pedal`、`brake`、`helmet`（rc=1，最不熟）與 `signal`（7 天前，明天就離開 2–7 天視窗）；前三個與昨天重疊，Lv.2 情境全部改寫成新的人物、地點與目的。
- 修正產生器缺陷：複習單字彈窗字典（`const REVIEW`）原本寫死前一天的字，改成從當日文章的 `review-word` 標記自動擷取，並在缺字時直接中止產出。此缺陷只影響本次產出流程，昨日頁面內容未受影響。
- 音檔沿用三聲線與句間停頓試行（同聲線 0.05 秒、換人 0.12 秒、階段切換 0.25 秒）；主音檔 132.34 秒、35 句 / 274 字、每句最多 10 字。
- 驗證：`python3 scripts/validate_daily.py 2026-09-08` 84 checks / 0 warnings / 0 errors；本機 HTTP server 上 375px 無橫向溢位、console 0 errors、`article.mp3` 與 `s01.mp3`–`s35.mp3` 均回 200、單字 / 複習字 / 片語彈窗查詢全部命中、首頁最新一筆為 Day 114。

## 2026-09-07 — Day 113 正式教材產出

- 先 `git fetch` 再 `git pull --ff-only`，同步遠端 `SRS update: review quiz 2026-09-03`，才依最新 `vocabulary/learning.json` 生成今日複習內容；今日納入 60 個到期舊單字（含 `efficient` 等逾期字），排除今天新字。
- 新增 `daily/2026-09-07/`，主題為 `Storing Bags in a Station Locker Before a Day Trip`；今日新字：`insert`、`medium`、`space`。
- 任務是讀懂車站置物櫃告示（大／中／小櫃價格、最晚取件時間、只收零錢、寄物處位置與營業時間），大型櫃全滿時改到人工寄物處寄放兩件行李；文章融入複習字 `locker`、`exact`、`hours`。
- 今日目標語塊：`Is there any space ...?`（開口）、`exact change`（資訊判讀）、`drop off`（替代方案）；三者都出現在 Article、Key Phrases、Role-play 的「你」回合與 Context Recall，其中 space 與 drop off 各有一題跨情境轉移。
- 能力標記以 `publicEnglish` + `travelSpeaking` 為 primary（`publicEnglish` 自 Day 106 後首次回到主要能力），`onlineReading`、`dailyResponse` 為次要。
- 音檔沿用三聲線與句間停頓試行（同聲線 0.05 秒、換人 0.12 秒、階段切換 0.25 秒）；主音檔 129.63 秒、35 句 / 285 字、每句最多 10 字。
- 因今日到期字達 60 個且含較長單字，Review Words 表格在 390px 會橫向溢位約 53px；已在今日頁 CSS 加入只作用於 `.review-table` 的窄螢幕欄寬規則，共用 CSS 與其他日頁面未變動。
- 順帶量到 Day 112（2026-09-03）在 390px 下同一表格也有約 13px 橫向溢位，屬既有問題，本次未修改舊頁。
- `ability_map.json`、`vocabulary/sentences.json` 改以文字插入方式更新，維持原檔既有的行內陣列排版，避免整檔重排產生無關 diff。
- 驗證：`python3 scripts/validate_daily.py 2026-09-07` 84 checks / 0 warnings / 0 errors；本機 HTTP server 上 375 與 390px 皆無橫向溢位、console 0 errors、`article.mp3` 與 `s01.mp3`–`s35.mp3` 均回 200、首頁最新一筆為 Day 113。

## 2026-09-03 — Day 112 正式教材產出

- 先執行 `git fetch origin`，發現遠端有 2026-09-02 的 SRS 更新，已以 fast-forward 同步後再生成今天的複習內容；今日納入 18 個到期舊單字，排除今天新字。
- 新增 `daily/2026-09-03/`，主題為 `Checking a City Bike Before a Museum Ride`；今日新字：`pedal`、`brake`、`helmet`。
- 文章以城市單車租借 app、站點公告與服務台對話為英文輸入；任務是找出通票價格、騎乘時間、押金與歸還時間，檢查車況，並在第一台車需要維修時要求替代單車。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、10 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔；文章使用 `narrator`、`traveler`、`staff` 三聲線。
- 依先前討論的第一階段方案，在今日頁面加入視覺句子重音切換與逐句播放標亮；新字表顯示 `PED-al`、`BRAKE`、`HEL-met`，沒有改動語音的自然重音合成。
- 主音檔延續句間停頓試行：同聲線約 0.05 秒、換人約 0.12 秒、段落切換約 0.25 秒；逐句 MP3 未加入額外停頓。
- 文章 34 句 / 280 字；主音檔實測 123.72 秒，另有 34 個逐句音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-09-03` 通過 84 checks、0 warnings、0 errors；JSON parse、inline JavaScript syntax、頁面互動、內容 / SRS 對齊與 `git diff --check` 均通過；未修改既有未追蹤的 `test/`。

---

## 2026-09-02 — Day 111 正式教材產出

- 先執行 `git fetch origin`，發現遠端有 2026-09-01 的 SRS 更新，已以 fast-forward 同步後再生成今天的複習內容；今日共有 15 個到期複習字。
- 新增 `daily/2026-09-02/`，主題為 `Finding Cold Medicine at a Travel Pharmacy`；今日新字：`cough`、`symptom`、`tablet`。
- 文章以藥局網頁公告與藥師對話為英文輸入；任務是找出營業時間、成人藥品供應與標示提醒，描述症狀，並在錠劑缺貨時詢問替代方案。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、10 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔；文章使用 `narrator`、`traveler`、`staff` 三聲線。
- 主音檔延續句間停頓試行：同聲線約 0.05 秒、換人約 0.12 秒、段落切換約 0.25 秒；逐句 MP3 未加入額外停頓。
- 文章 32 句 / 267 字；主音檔實測 124.70 秒，另有 32 個逐句音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-09-02` 通過 84 checks、0 warnings、0 errors；JSON parse、inline JavaScript syntax、目標語塊覆蓋與 `git diff --check` 均通過；未修改既有未追蹤的 `test/`。

---

## 2026-09-01 — Day 110 正式教材產出

- 先執行 `git fetch origin`，發現遠端有 2026-08-31 的 SRS 更新，已用 fast-forward 同步後再生成今天的複習內容；今日共有 7 個到期複習字。
- 新增 `daily/2026-09-01/`，主題為 `Connecting to Airport Wi-Fi Before Activating an eSIM`；今日新字：`connect`、`signal`、`restart`。
- 文章以 airport website instructions 與 help-desk conversation 為英文輸入；任務是找出 Airport_Guest、三十分鐘 guest access、更新代碼，並在弱訊號或登入失敗時完成修復。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、10 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔；文章使用旁白、旅客、工作人員三聲線。
- 主音檔首次試行句間停頓：同聲線約 0.05 秒、換人約 0.12 秒、段落切換約 0.25 秒；逐句 MP3 未加入額外停頓。
- 文章 34 句 / 271 字；主音檔實測 129.67 秒，另有 34 個逐句音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-09-01` 通過 84 checks、0 warnings、0 errors；JSON parse、inline JavaScript syntax、目標語塊覆蓋與 `git diff --check` 均通過；未修改既有未追蹤的 `test/`。

---

## 2026-08-31 — Day 109 正式教材產出

- 先執行 `git fetch origin`，以 fast-forward 同步遠端 2026-08-28 的 SRS 更新；依最新 `vocabulary/learning.json` 產生 52 個到期複習字。
- 新增 `daily/2026-08-31/`，主題為 `Requesting a Late Checkout Before a Late Flight`；今日新字：`extend`、`charge`、`noon`。
- 文章以 hotel app notice 與 front-desk conversation 為英文輸入；任務是讀懂退房時間、申請期限與費用，並在飯店客滿時改用寄放行李方案。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、10 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔；文章使用 `narrator`、`traveler`、`staff` 三聲線。
- 文章 36 句 / 273 字；主音檔實測 132.69 秒，另有 36 個逐句音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-08-31` 通過 84 checks、0 warnings、0 errors；內容 / SRS 對齊與 `git diff --check` 均通過；未修改既有未追蹤的 `test/`。

---

## 2026-08-28 — Day 108 正式教材產出

- 先執行 `git fetch origin`，確認遠端有 2026-08-27 的 SRS 更新後以 fast-forward 同步；同步後今天共有 24 個到期複習字。
- 新增 `daily/2026-08-28/`，主題為 `Checking a Wrong Price at an Airport Gift Shop`；今日新字：`discount`、`offer`、`amount`。
- 文章以 airport shop page、offer sign、price tag 與 cashier conversation 為英文輸入；任務是找出特價期限、20% 折扣、含稅與三十天退換條件，並在錯誤標價時確認最後金額。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔；文章融入到期複習字 `late`、`wrong`、`change`。
- 文章使用旁白、旅客、工作人員三聲線，36 句 / 257 字；主音檔實測 130.75 秒，另有 36 個逐句音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-08-28` 通過 84 checks、0 warnings、0 errors；JSON、JavaScript syntax、內容 / SRS 對齊與 `git diff --check` 均通過；未修改既有未追蹤的 `test/`。

---

## 2026-08-27 — Day 107 正式教材產出

- 先 `git fetch origin`，以 fast-forward 同步遠端最新 SRS；同步後今天共有 19 個到期複習字。
- 新增 `daily/2026-08-27/`，主題為 `Ordering a Safe Café Meal with a Food Allergy`；今日新字：`dairy`、`dish`、`side`。
- 文章以手機咖啡廳菜單、過敏提示與點餐對話為英文輸入；任務是確認無乳製品、附餐與價格，並在雞肉飯碗售罄後改選豆腐飯碗。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、10 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔。
- 文章使用旁白、旅客、工作人員三聲線，36 句 / 274 字；主音檔實測 126.98 秒。
- 驗證：`python3 scripts/validate_daily.py 2026-08-27` 通過 84 checks、0 warnings、0 errors；JSON、JavaScript syntax、`git diff --check` 與內容對齊檢查通過；未修改既有未追蹤的 `test/`。

---

## 2026-08-26 — Day 106 正式教材產出

- 先 `git fetch origin` 確認遠端沒有較新的 SRS 更新；依 `vocabulary/learning.json` 產生今天 15 個到期複習字。
- 新增 `daily/2026-08-26/`，主題為 `Taking the Right City Bus During a Road Detour`；今日新字：`bus`、`detour`、`opposite`。
- 文章以 map result、bus detour notice 與 driver conversation 為英文輸入；任務是找到臨時站牌、確認 Bus Twelve，並在 Museum Square 下車。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、8 回合 Role-play、Ability Map、句子 SRS 與首頁入口；Speaking Bridge 使用 `train`、`depart`、`airport`、`eligible`，未使用今日新字。
- 文章使用旁白、旅客、工作人員三聲線，34 句 / 268 字；完成主音檔與 34 個逐句音檔，對調聲線後主音檔實測 117.50 秒。
- 依使用者回饋對調聲線：旁白改用 Jenny、旅客（我的台詞）改用 Aria，工作人員維持 Guy；重新生成今天的旁白與旅客逐句音檔及完整主音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-08-26` 通過 84 checks、0 warnings、0 errors；JSON、JavaScript syntax、`git diff --check` 與內容對齊檢查通過；未修改既有未追蹤的 `test/`。

## 2026-08-25 — Day 105 正式教材產出

- 先 `git fetch origin` 並以 fast-forward 同步遠端最新 SRS；依同步後的 `vocabulary/learning.json` 產生今天 5 個到期複習字。
- 新增 `daily/2026-08-25/`，主題為 `Finding the Hotel After a Station Exit Change`；今日新字：`directions`、`walk`、`cross`。
- 文章以 station notice、map result 與 information-desk conversation 為英文輸入；任務是出口變更後找到飯店側門，融入 `notice`、`miss`、`fountain` 等路線字。
- 完成 10 題 Context Recall、4 組 Speaking Bridge、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及完整文章與逐句音檔。
- 先以三聲線重新生成音檔：`narrator` 使用 Aria、`traveler` 使用 Jenny、`staff` 使用 Guy，並在頁面加入聲線提示。
- 依回饋再修正 Article：拿掉 `I ask`、`She says` 等報導式包裝，讓旁白、旅客台詞與工作人員台詞各自成句，再重新生成三聲線音檔。
- 驗證：`python3 scripts/validate_daily.py 2026-08-25` 通過 84 checks、0 warnings、0 errors；主音檔 119.78 秒，34 句 / 262 字、35 個 MP3 均存在且可讀；未修改既有未追蹤的 `test/`。

---

## 2026-08-24 — Day 104 正式教材產出

- 先 `git fetch origin`，以 fast-forward 同步遠端 2026-08-21 的最新單字 SRS，再依最新 `vocabulary/learning.json` 生成今日複習內容。
- 新增 `daily/2026-08-24/`，主題為 `Finding the Right Airport Train After a Platform Change`；今日新字：`train`、`depart`、`airport`。
- 文章以車站 departure screen、station notice 與工作人員對話為英文輸入；融入 `station`、`screen`、`line`、`notice`、`delayed`、`valid` 等到期字。
- Active Recall Quiz 納入全部 39 個到期字；Speaking Bridge 使用 2–7 天前的 `fuel`、`damage`、`deposit`、`eligible`；完成 10 題 Context Recall 與 8 回合 Role-play。
- 完成 Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s34.mp3`；主音檔實測 121.97 秒。
- 驗證：`python3 scripts/validate_daily.py 2026-08-24` 通過 84 checks、0 warnings、0 errors；JSON parse、JavaScript syntax、`git diff --check` 與內容對齊檢查通過。

---

## 2026-08-19 — Day 101 正式教材產出

- 先 `git fetch origin` 並以 fast-forward 同步 2026-08-18 最新單字 SRS，再依最新 `vocabulary/learning.json` 產生複習內容。
- 新增 `daily/2026-08-19/`，主題為 `Finding the Walking Tour Meeting Point`；今日新字：`meeting point`、`fountain`、`tour`。
- Active Recall Quiz 納入全部 11 個到期字；Speaking Bridge 使用 `carousel`、`describe`、`handle`、`noise`；完成 10 題 Context Recall 與 8 回合 Role-play。
- 完成 Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s32.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-08-19` 通過 84 checks、0 warnings、0 errors；主音檔 118.25 秒，32 句 / 257 字；390×844 手機版無橫向溢位，首頁前三筆為 Day 101、100、99，音檔可載入。

---

## 2026-08-18 — Day 100 正式教材與首頁清單修復

- 先 `git fetch origin` 並以 fast-forward 同步 2026-08-17 最新單字 SRS，再依最新 `vocabulary/learning.json` 產生複習內容。
- 新增 `daily/2026-08-18/`，主題為 `Checking Carry-on Liquid Rules Before Security`；今日新字：`liquid`、`container`、`limit`。
- Active Recall Quiz 納入全部 3 個到期字；Speaking Bridge 使用 `contain`、`sensitive`、`delayed`、`deck`；完成 10 題 Context Recall 與 8 回合 Role-play。
- 修正首頁學習記錄容器錯位：Day 99 原本落在 Day 66 後方，現已將全部日期統一放回 `#day-list`，依日期新到舊排序。
- 驗證：`python3 scripts/validate_daily.py 2026-08-18` 通過 84 checks、0 warnings、0 errors；主音檔 117.94 秒，31 句 / 251 字；390×844 手機版首頁與教材均無橫向溢位，首頁前三筆為 Day 100、99、98。

---

## 2026-08-17 — Day 99 正式教材產出

- 先 `git fetch origin`，以 fast-forward 同步遠端最新單字 SRS，再依最新 `vocabulary/learning.json` 產生複習內容。
- 新增 `daily/2026-08-17/`，主題為 `Reporting a Missing Suitcase at Baggage Claim`；今日新字：`carousel`、`describe`、`handle`。
- 文章融入到期複習字 `passenger`、`nearby`、`delayed`；Active Recall Quiz 納入全部 37 個到期字；Speaking Bridge 使用 `noise`、`maintenance`、`fan`、`delayed`。
- 完成 10 題 Context Recall、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s36.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-08-17` 通過 84 checks、0 warnings、0 errors；主音檔 130.56 秒；390×844 手機版無橫向溢位，0.75× 與逐句播放正常，console 0 errors。

---

## 2026-08-03 — Day 89 正式教材產出

- 先執行 `git fetch origin`，確認本地 `HEAD` 與 `origin/main` 同步，使用最新的 `vocabulary/learning.json` 生成複習內容。
- 新增 `daily/2026-08-03/`，主題為 `Handling a Stuck Hotel Laundry Machine`；今日新字：`stuck`、`repair`、`working`。
- 文章融入到期複習字 `option`、`choice`、`reception`；Active Recall Quiz 納入全部 46 個到期字；Speaking Bridge 使用 `expired`、`reset`、`item`、`damaged`。
- 完成 10 題 Context Recall、12 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s16.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-08-03` 通過 79 checks、0 warnings、0 errors；JSON parse、句子字數、目標語塊分布與 `git diff --check` 亦完成檢查。

---

## 2026-07-31 — Day 88 正式教材產出

- 先 `git fetch origin`，確認遠端有 2026-07-30 的 SRS 更新後，以 fast-forward 同步最新 `vocabulary/learning.json`。
- 新增 `daily/2026-07-31/`，主題為 `Fixing a Missing Café Item`；今日新字：`missing`、`item`、`remake`。
- 文章融入到期複習字 `replace`、`option`、`deliver`；Active Recall Quiz 納入同步後全部 15 個到期字；Speaking Bridge 使用 `damaged`、`baggage`、`miss`、`flexible`。
- 完成 10 題 Context Recall、10 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s14.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-07-31` 通過 79 checks、0 warnings、0 errors；JSON parse、目標語塊分布與音檔對齊亦完成檢查。

---

## 2026-07-30 — Day 87 正式教材產出

- 先 `git fetch origin`，確認遠端有 2026-07-29 的 SRS 更新後，以 `git pull --ff-only origin main` 同步最新 `vocabulary/learning.json`。
- 新增 `daily/2026-07-30/`，主題為 `Fixing a Hotel Key Card Problem`；今日新字：`expired`、`reset`、`access`。
- 文章融入到期複習字 `speaker`、`deliver`、`option`；Active Recall Quiz 納入同步後全部 15 個到期字；Speaking Bridge 使用 `damaged`、`baggage`、`label`、`larger`。
- 完成 10 題 Context Recall、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s14.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-07-30` 通過 79 checks、0 warnings、0 errors；句子皆不超過 12 字、JSON parse、SRS 對齊與 `git diff --check` 亦通過。

---

## 2026-07-22 — Day 81 正式教材產出

- 先同步遠端兩筆 2026-07-21 SRS 更新，再依最新 `vocabulary/learning.json` 產生今日複習內容。
- 新增 `daily/2026-07-22/`，主題為 `Checking Hotel Breakfast and Luggage`；今日新字為 `included`、`reception`、`store`。
- 開始語塊深化試行第 1/7 篇：`breakfast is included`、`Can I leave my luggage here?`、`I want to make sure` 貫穿 Article、Key Phrases、Role-play 與 Context Recall，並加入跨情境提取。
- 教材包含 19 題到期 Active Recall、10 題 Context Recall、4 組 Speaking Bridge、8 回合 Role-play、`article.mp3` 與 `s01.mp3` 到 `s14.mp3`。
- 同步更新首頁、`profile.json`、`vocabulary/learning.json`、`vocabulary/sentences.json`、`ability_map.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：`validate_daily.py` 通過 79 checks、0 warnings、0 errors；JSON、JavaScript、`git diff --check` 及本機 HTTP 頁面 / 音檔 200 皆通過。

---

## 2026-07-21 — 詞彙深度與語塊訓練規格

- 依使用者確認，將詞彙學習由孤立字義深化為自然搭配、可重用語塊、Role-play 產出與 Context Recall 跨情境提取。
- 更新 `AGENTS.md` 與 `.ai/daily-english-learning/SKILL.md`：每篇選 2–3 個目標語塊，區分主動產出與辨識理解，並保留既有 Active Recall、Speaking Bridge 與句子 SRS 邊界。
- 更新 `.ai/DECISIONS.md` 與 `.ai/PROJECT_STATE.md`，記錄 Day 81 起連續 7 篇試行方式、人工驗收項目與後續評估依據。
- 本次只調整規格與接手文件，未修改每日頁面、資料 schema、SRS runtime 或驗證器。

---

## 2026-07-16 — Day 78 任務型教材正式產出

- 先同步遠端最新 SRS；同步後今日共有 11 個到期複習字。
- 新增 daily/2026-07-16/，主題為 Choosing a Ferry Departure；今日新字：dock、boarding、option。
- Mission 以渡輪時刻表、票務提示與櫃檯對話為輸入，包含 8 回合 Role-play、10 題 Context Recall 與 4 個 2–7 天前單字的 Speaking Bridge。
- 同步更新首頁、profile.json、vocabulary/learning.json、vocabulary/sentences.json、ability_map.json；生成 article.mp3 與 s01.mp3 到 s16.mp3。
- 驗證：python3 scripts/validate_daily.py 2026-07-16 通過 79 checks，0 warnings，0 errors；JSON parse 與 git diff --check 亦通過。

---

## 2026-07-15 — Day 77 任務型教材正式產出

- 先 `git fetch origin` / `git pull --ff-only origin main`，同步最新 7/14 review quiz 與 sentence SRS 後生成今天教材。
- 新增 `daily/2026-07-15/`，主題為 `Finding the Right Bus`；今日新字：`museum`、`instead`、`passenger`。
- Active Recall Quiz 依最新 SRS 產出 12 個到期複習字；Speaking Bridge 使用前幾日單字；Context Recall 8 題、Role-play 8 回合與 Mission 均已接通。
- 生成 `article.mp3` 與 `s01.mp3` 到 `s19.mp3`，並更新首頁、`profile.json`、`vocabulary/learning.json`、`vocabulary/sentences.json`、`ability_map.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：`python3 scripts/validate_daily.py 2026-07-15` 通過 73 checks，0 warnings，0 errors。

---

## 2026-07-15 — 任務型測試版修正單字複習流程

- 將 `test/2026-07-15/` 的單字複習改為 Active Recall Quiz，載入遠端最新 SRS 的 12 個到期單字，使用中文意思、例句挖空與四選一。
- 依使用者回饋移除文章句子前的可見編號，保留逐句播放與句子資料順序。
- 更新 `AGENTS.md`、`.ai/daily-english-learning/SKILL.md` 與 `.ai/PROJECT_STATE.md`，確認單字複習沿用既有 Active Recall Quiz 與 SRS 流程。
- 驗證：HTML/JS 語法、HTTP 200、音檔與 `git diff --check` 通過。

---

## 2026-07-15 — 每日教材切換為任務型情境英文

- 依使用者確認，將 `The Blue Receipt` Episode 18 標記為第一季結尾，停止每日自動續寫小說。
- 更新 `.ai/daily-english-learning/SKILL.md`：新增 Mission、英文資訊輸入、Role-play、跨情境 Context Recall 與每週能力平衡規則。
- 同步更新 `AGENTS.md`、`profile.json`、首頁、`scripts/validate_daily.py`、`LEARNING_SYSTEM_ROADMAP.md` 與 `.ai/DECISIONS.md`。
- 封存 `.ai/serial-story/` 文件，保留既有小說資料，不重開完整 app。
- 驗證：舊 Episode 18 通過 70 checks；Python / JSON / 首頁 inline JS / `git diff --check` 通過；新日期的 Mission、Role-play transition guard 通過。

---

## 2026-07-13 — Day 75 正式教材產出

- 先 `git fetch origin` 並 `git pull --ff-only origin main`，同步 7/9 單字 SRS 與句子 SRS 遠端更新後再生成今天教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-13/`，標題為 `The Blue Receipt · Episode 17`。
- 今日新字：`key`、`unlock`、`final`；文章融入複習字：`platform`、`clerk`、`tomorrow`、`receipt`、`printed`、`voice`。
- Review Quiz / Review Words 依最新 `learning.json` 生成，共納入 43 個到期複習字。
- Speaking Bridge 使用 `proof`、`clerk`、`deliver`、`exact`；Context Recall 8 題同步寫入 `vocabulary/sentences.json`。
- 同步首頁、`profile.json`、`ability_map.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：`article.mp3` 與 `s01.mp3` 到 `s25.mp3` 已生成；`python3 scripts/validate_daily.py 2026-07-13` 通過，70 checks，0 warnings，0 errors。

---

## 2026-07-09 — Day 74 產出錯誤修復

- 同步遠端 `origin/main`，保留 2026-07-08 的 review quiz 與 sentence SRS 更新。
- 檢查前一輪失敗留下的 `daily/2026-07-09/`，確認內容錯置為 2026-07-08 / Episode 15 複製品。
- 將 `daily/2026-07-09/index.html` 修正為 Day 74、`The Blue Receipt · Episode 16`，主線為 Mina 帶著 report 到 front office。
- 今日新字：`proof`、`clerk`、`deliver`；文章融入複習字：`report`、`guard`、`record`。
- 重新產生 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，確保音檔對應 Episode 16。
- 更新首頁、`profile.json`、`vocabulary/learning.json`、`vocabulary/sentences.json`、`ability_map.json` 與 `.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：`python3 scripts/validate_daily.py 2026-07-09` 通過，70 checks，0 warnings，0 errors。

---

## 2026-07-08 — Day 73 正式教材產出

- 先 `git fetch origin`，確認遠端只比本地多 `vocabulary/sentences.json`，先同步句子 SRS 資料後再生成今天教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-08/`，標題為 `The Blue Receipt · Episode 15`。
- 今日新字：`office`、`report`、`guard`；文章正式揭露門後的人是 May Lin，主線進入收束段。
- Active Recall Quiz 依最新 `learning.json` 生成 5 個今日到期複習字；Speaking Bridge 使用 `voice`、`truth`、`folded`、`careful`。
- 補齊 `Ability Focus`、8 題 `Context Recall`、`vocabulary/sentences.json`、`ability_map.json`、首頁、`profile.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：`article.mp3` 與 `s01.mp3` 到 `s25.mp3` 已生成；`python3 scripts/validate_daily.py 2026-07-08` 通過；本機 HTTP `/` 與 `/daily/2026-07-08/` 回傳 200。

## 2026-07-07 — 每日教材驗證腳本

- 新增 `scripts/validate_daily.py`，以 Python stdlib 驗證單日正式教材。
- 驗證範圍包含必要 HTML 區塊、共用 script、`article.mp3`、逐句 `sNN.mp3`、句子編號連續性、Context Recall 與 `vocabulary/sentences.json` 對齊、`ability_map.json` session、今日新字與 `learning.json` 對齊、Speaking Bridge 不使用今日新字、首頁連結。
- 更新 `.ai/daily-english-learning/SKILL.md`，要求未來 commit / push 前先執行 `python3 scripts/validate_daily.py [日期]`。
- 更新 `LEARNING_SYSTEM_ROADMAP.md`，將 P2 產出驗證自動化多數項目標記完成。
- 驗證：`python3 scripts/validate_daily.py 2026-07-07` 通過，70 checks，0 warnings，0 errors。

---

