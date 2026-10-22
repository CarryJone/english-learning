# 2026-10-13 任務完成交接

> 用途：接手參考；不是開發規則。

- Day 132 已完成；32 句／291 字、70 到期字、3 Bridge、10 Context Recall、5 核心句。
- 使用者要求不用帳號，已切換本機 Kokoro；環境 .venv-tts、模型 .tts-cache 均不進版控。
- 生成命令：`.venv-tts/bin/python scripts/generate_daily_kokoro.py YYYY-MM-DD`。安裝步驟：scripts/KOKORO.md。
- assets/voices.json：defaultProvider=kokoro；角色聲線在 kokoroVoice，speed=0.8。edge voice 保留給歷史頁，核心句音檔不重生。
- Kokoro speed=0.9 實測 96 秒，0.8 為 111.496 秒；句間停頓保持 0.05／0.12／0.25 秒。
- 98 checks／0 warnings／0 errors；4 個 provider 回歸測試；33 MP3 解碼、純文字／角色對照、完整 SRS 覆蓋通過。
- 375／390px 無橫向溢位；核心句倒數、播放速度切換正常；console 0 errors。
- audio-manifest.json 記錄聲線、模型 hash、純文字與時長；移除 pending JSON。
- edge_tts 7.2.7／7.2.8 仍 HTTP 403；網路與聲線清單正常，校時重試失敗。上游 10-10 討論 #489 症狀相同。
- 原有 test/ 未碰；PROJECT_STATE 原有使用者變更保留，不併入本次提交。

- 後續使用者要求停頓多一點：句間改 0.15／0.25／0.4 秒，設定在 providers.kokoro.pauses；語速不變。重新生成後全文 115.598 秒，98 checks、33 MP3 解碼通過。

## 2026-10-14 Day 133 完成
- Using the Hotel Laundry Room：cycle／basket／iron；10 到期字、10 Context Recall、5 核心句；2–7 天前無字，Bridge 明確顯示提示，未使用昨天新字。
- 32 句／291 字，主音檔 127.489 秒，沿用 Kokoro speed 0.8 與 0.15／0.25／0.4 停頓；98 checks、33 MP3 解碼／文字對照、JS 語法、375／390px 無溢位、核心句倒數／播放器通過。

## 2026-10-15 Day 134 完成
- Getting a Replacement for a Faulty Hotel Iron：faulty／cord／heat；3 到期字、3 Bridge（10-13 coach／curb／shelter）、10 Context Recall、5 核心句。
- 32 句／290 字，全文 124.528 秒；Kokoro speed 0.8、停頓 0.15／0.25／0.4 不變。98 checks、33 MP3 解碼／純文字對照、JS 語法、375／390px 版面、倒數與播放器通過。
- Day 134 提交／推送：先前 auto-review 拒絕學習資料上傳；使用者已在本輪明確要求「上傳git」，授權今日教材、學習紀錄與語音規則上傳 CarryJone/english-learning。

- 2026-10-15 新指示：每次先試 edge_tts，失敗才用 Kokoro；defaultProvider=edge／fallbackProviders=[kokoro]，AGENTS／SKILL 已同步。規則隨本輪提交上傳；不是新增自動切換器。原方案今日 Hello 與校時重試仍 403；另以今天三角色台詞重測，三角色皆 HTTP 403。今日教材音檔未替換。

## 2026-10-16 Day 135 完成
- Choosing an Easy City Walk Online：flat／steep／pace；8 到期字、4 Bridge（iron／cycle／basket／coach）、10 Context Recall、5 核心句。先同步遠端 SRS 48a7aa4。
- 今日文章三角色 edge_tts 7.2.8 測試皆 403，依規則用 Kokoro；32 句／290 字，全文 124.948 秒，speed 0.8 與 0.15／0.25／0.4 停頓不變。
- 98 checks、33 MP3 解碼／文字與聲線對照、JS 語法、375／390px 無溢位、核心句倒數與播放速度通過。

## 2026-10-19 Day 136 完成
- Finding My Train Carriage and Reserved Seat：carriage／reserved／rack；24 到期字、4 Bridge（flat／steep／pace／shelter）、10 Context Recall、5 核心句。先同步 SRS 583daaa。
- 當日三角色 edge_tts 7.2.8 皆 HTTP 403，改用 Kokoro；32 句／290 字，全文 117.256 秒，speed 0.8，停頓 0.15／0.25／0.4。edge_tts 現已安裝到 .venv-tts，避免依賴會消失的 /tmp runtime。
- 98 checks、33 MP3 解碼／純文字與聲線對照、JS 語法、375／390px 無溢位、倒數與播放速度通過。
- 暫存 build 腳本已清空，本輪從現有正式 HTML 重建內容生成；音檔腳本仍使用 repo scripts/generate_daily_kokoro.py。
- Day 136 上傳授權：使用者已回覆「上傳git」，明確同意今日教材與 profile／SRS 上傳 CarryJone/english-learning；先前 auto-review 的授權阻塞已取得使用者確認。

## 2026-10-20 Day 137 完成
- Buying and Wrapping a Fragile Gift：gift／wrap／fragile；21 到期字、4 Bridge（faulty／flat／steep／pace）、10 Context Recall、5 核心句。同步 SRS 3d1c45d。
- edge_tts 7.2.8 以今日三角色台詞測試皆 403，使用 Kokoro；32 句／289 字、122.982 秒，原 speed 0.8 與停頓不變。
- 98 checks、33 MP3 解碼／文字與聲線對照、JS 語法、375／390px 版面、倒數與播放器通過。

## 2026-10-21 Day 138 完成
- Returning a Damaged Gift and Asking for a Refund：crack／chipped／unused；6 到期字、4 Bridge（faulty／carriage／reserved／rack）、10 Context Recall、5 核心句。先同步遠端 SRS 41d7fa6。
- edge_tts 7.2.8 三角色測試仍 403，使用 Kokoro；32 句／290 字、118.730 秒。speed 0.8 與停頓 0.15／0.25／0.4 不變。
- 98 checks、33 MP3 解碼／文字與聲線對照、JS 語法、375／390px 無溢位、倒數與播放速度通過。Bridge 優先 faulty（rc0），再選 rc1 中尚未入選的三個字，未用 rc2 字排擠較不熟的字。

## 2026-10-22 Day 139 完成
- M4 Saving My Airport Bus Ticket for Offline Use：32 句／276 字、117.778 秒，20 到期字全部收錄、gift/wrap/fragile/faulty 四組 Bridge、10 Context Recall、5 核心句。
- 已先同步 origin/main 最新 SRS（6519142）。今日 edge_tts 7.2.8 三角色均 403，整篇與逐句統一 Kokoro，沿用 speed=0.8 與 0.15／0.25／0.4 秒停頓。
- 98 checks／0 warnings／0 errors、33 MP3 解碼、manifest 文字／角色／聲線、JS 語法通過；375／390px 無溢位、核心句倒數與 0.75 倍速正常，console 0 errors。
- 模擬票券服務的截圖允許範圍已註明，不能推廣到所有票券。原有 test/ 與 PROJECT_STATE 使用者變更不納入提交。
