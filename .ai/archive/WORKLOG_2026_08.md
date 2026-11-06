# 2026-08 工作紀錄歸檔

## 2026-08-03 — Day 89 正式教材產出

- 先執行 `git fetch origin`，確認本地 `HEAD` 與 `origin/main` 同步，使用最新的 `vocabulary/learning.json` 生成複習內容。
- 新增 `daily/2026-08-03/`，主題為 `Handling a Stuck Hotel Laundry Machine`；今日新字：`stuck`、`repair`、`working`。
- 文章融入到期複習字 `option`、`choice`、`reception`；Active Recall Quiz 納入全部 46 個到期字；Speaking Bridge 使用 `expired`、`reset`、`item`、`damaged`。
- 完成 10 題 Context Recall、12 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s16.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-08-03` 通過 79 checks、0 warnings、0 errors；JSON parse、句子字數、目標語塊分布與 `git diff --check` 亦完成檢查。

---

## 2026-08-17 — Day 99 正式教材產出

- 先 `git fetch origin`，以 fast-forward 同步遠端最新單字 SRS，再依最新 `vocabulary/learning.json` 產生複習內容。
- 新增 `daily/2026-08-17/`，主題為 `Reporting a Missing Suitcase at Baggage Claim`；今日新字：`carousel`、`describe`、`handle`。
- 文章融入到期複習字 `passenger`、`nearby`、`delayed`；Active Recall Quiz 納入全部 37 個到期字；Speaking Bridge 使用 `noise`、`maintenance`、`fan`、`delayed`。
- 完成 10 題 Context Recall、8 回合 Role-play、Ability Map、句子 SRS、首頁入口，以及 `article.mp3` 與 `s01.mp3` 到 `s36.mp3`。
- 驗證：`python3 scripts/validate_daily.py 2026-08-17` 通過 84 checks、0 warnings、0 errors；主音檔 130.56 秒；390×844 手機版無橫向溢位，0.75× 與逐句播放正常，console 0 errors。

---
