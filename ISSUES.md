# 問題追蹤紀錄

## 🔴 [OPEN] 排程任務未自動產出每日學習材料

**發現日期：** 2026-03-13
**影響範圍：** Day 1–4 均為手動產出，排程從未成功自動執行
**嚴重程度：** 高（核心功能失效）

---

### 問題描述

`daily-english-learning` 排程任務設定為每週一到五 07:09 AM 執行，但連續 3 天未能自動產出學習材料：

| 日期 | 預期行為 | 實際行為 |
|------|----------|----------|
| 2026-03-11 (二) | 07:09 自動產出 Day 2 | 09:34 手動 commit |
| 2026-03-12 (三) | 07:09 自動產出 Day 3 | 09:53 手動 commit |
| 2026-03-13 (四) | 07:09 自動產出 Day 4 | **完全未產出** |

---

### 調查發現

#### 1. Debug Log 分析
- 所有 debug log 最新時間戳為 **2026-03-12 17:47**（我們手動工作的最後時間）
- 今天 2026-03-13 早上 **沒有任何 debug log**，代表 Claude Code **未在 07:09 執行**
- March 11 的 session log（`104da752`）顯示 `Loaded 0 unique skills`，表示 Skill 系統在那次 session 中**未載入排程任務**

#### 2. Git Commit 時間落差
- Day 2 commit 在 09:34（比排程晚 2.5 小時）
- Day 3 commit 在 09:53（比排程晚 2.5 小時）
- 規律性的時間落差說明：Mac 在 07:09 時處於**睡眠狀態**，等使用者手動開啟 Claude Code 後，部分任務可能透過 catchup 機制補跑，但成功率不穩定

#### 3. 今日完全失敗的額外原因
- 使用者開啟 Claude Code 時，直接進入已有的對話 session（本次對話）
- 排程的 catchup 任務與手動 session 可能衝突，導致 daily-english-learning 任務完全被跳過

#### 4. 排程設定確認
```
taskId: daily-english-learning
cron: 0 7 * * 1-5  ← 正確
enabled: true  ← 正確
lastRunAt: 2026-03-12T23:09:25.229Z  ← 07:09 Taipei（dispatcher 記錄，非實際執行時間）
jitterSeconds: 564  ← 約 +9 分鐘
```

---

### 根本原因

**主因：Mac 在排程時間（07:09 AM）處於睡眠狀態**

Claude Code 排程任務需要 app 在背景持續執行。Mac 睡眠 → Claude Code 停止 → 排程無法觸發。

**次因：Catchup 機制不可靠**

- Days 2–3 的 catchup 時機不確定（可能是手動開啟後補跑，也可能是使用者直接手動操作）
- 今天的 catchup 完全未觸發（原因：使用者直接進入手動 session）

---

### 解決方案（待評估）

#### 方案 A：調整排程時間（推薦短期）
將排程改為使用者通常已在使用電腦的時間，如 **09:00 AM**，避免 Mac 睡眠問題。

```bash
# 修改指令：
# 將 cron 從 "0 7 * * 1-5" 改為 "0 9 * * 1-5"
```

**優點：** 實作簡單，成功率高
**缺點：** 不再是「起床就有內容」的體驗

#### 方案 B：Mac 喚醒排程（launchd）
用 macOS 的 `launchd` 在 07:05 喚醒電腦，確保 Claude Code 有機會執行。

```xml
<!-- ~/Library/LaunchAgents/com.user.wake.plist -->
<key>StartCalendarInterval</key>
<array>
  <dict>
    <key>Hour</key><integer>7</integer>
    <key>Minute</key><integer>5</integer>
    <key>Weekday</key><integer>1-5</integer>
  </dict>
</array>
```

**優點：** 保持 07:09 時間，無需改變排程
**缺點：** 需要系統層設定，Mac 需接電源才能從睡眠喚醒

#### 方案 C：手動觸發備援（最穩定）
保留排程，另外在 SKILL.md 新增一個手動執行的 `/today` 指令，讓使用者每天早上確認排程是否成功，若否可一鍵觸發。

---

### 暫時解決方案（今日）

今天需要手動執行排程任務來產出 Day 4 學習材料。

```
/today  # 或直接在 Claude Code 中執行 daily-english-learning 任務
```

---

### 後續追蹤

- [ ] 決定採用哪個解決方案
- [ ] 實作選定的解決方案
- [ ] 觀察 3 天確認是否穩定自動執行
- [ ] 考慮加入執行結果通知（成功/失敗 → Discord 或其他管道）

---

## 📝 歷史紀錄

| 日期 | 事件 |
|------|------|
| 2026-03-10 | Day 1 手動建立（系統剛設置） |
| 2026-03-11 | Day 2 手動建立，發現排程未自動執行 |
| 2026-03-12 | Day 3 手動建立，確認排程問題持續 |
| 2026-03-13 | 調查排因，建立此追蹤文件 |
