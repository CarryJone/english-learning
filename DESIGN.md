# Daily English 學習系統設計文件

> 給下一次啟動 AI session 的說明：這份文件記錄了整個系統的設計思路與決策過程，方便你快速了解背景、避免走回頭路。

---

## 系統架構概覽

```
english-learning/
├── index.html                    # 首頁（學習記錄清單）
├── profile.json                  # 學習者個人資料與進度
├── vocabulary/
│   └── learning.json             # 所有學過的單字 + SRS 狀態
├── daily/
│   ├── 2026-03-10/index.html     # Day 1 學習頁
│   ├── 2026-03-11/index.html     # Day 2 學習頁
│   └── 2026-03-12/index.html     # Day 3 學習頁
└── DESIGN.md                     # 本文件
```

**排程任務（Claude Code Scheduled Task）：**
- 路徑：`~/.claude/scheduled-tasks/daily-english-learning/SKILL.md`
- 執行時間：平日早上 7:09 AM（Asia/Taipei）
- Mac 喚醒設定：`sudo pmset repeat wakeorpoweron MTWRF 06:50:00`

**GitHub Pages：**
- URL：https://CarryJone.github.io/english-learning
- Repo：https://github.com/CarryJone/english-learning

---

## 學習者資訊（profile.json）

- 程度：A2（目標 B1）
- 母語：繁體中文
- 學習動機：看懂英文網路文章（教學、討論）、旅遊溝通
- 主題偏好：日常生活 / 旅遊（每天輪替）
- 創建：2026-03-10

---

## 核心設計決策

### 1. 每天新單字數量：3 個（重要！）

**決策**：從原本 6-8 個 → 5-6 個 → 最終定為 **3 個**

**原因（SRS 累積數學）**：
- 5 詞/天 × SRS 平均複習倍數 ≈ 需要 8 次複習/天
- 如果每天只複習 3-5 個，會造成積壓，大量單字長期沒有複習機會
- 3 詞/天 × 約 1.58 複習倍數 ≈ 4-5 次複習/天，可負擔

### 2. 複習策略：所有到期單字全部複習（不設上限）

**決策**：不再限制「只複習 3-5 個」，**到期的單字全部出現**

**原因**：搭配新單字減少（3個/天），即使有多個到期單字，總量依然可管理。設上限只會讓積壓越來越多。

### 3. SRS（Spaced Repetition System）間隔表

| reviewCount | 下次複習間隔 |
|-------------|------------|
| 0（初次加入） | +1 天 |
| 1 | +3 天 |
| 2 | +7 天 |
| 3 | +14 天 |
| 4 | +30 天 |
| 5 | +60 天 |
| 6 | +90 天 |
| ≥ 7 | **已掌握，不再出現** |

**答錯規則**：`reviewCount = 0`，`nextReview = 明天`（重新開始）

### 4. 主動回憶測驗（Active Recall Quiz）

**決策**：加入「看中文意思，選英文」的四選一選擇題，在 Review Words 區塊前出現

**科學依據**：Testing Effect / Active Recall — 主動從記憶中提取比被動閱讀更有效。Karpicke & Roediger (2008) 研究顯示測驗效應可提升 50% 以上長期記憶保留率。

**設計細節**：
- 題型：顯示中文意思 → 選正確英文（4選1）
- 干擾選項：從已學單字中隨機選3個，盡量選詞性相近的
- 選項順序：隨機排列（正確答案不固定位置）

### 5. GitHub API 同步（SRS 更新機制）

**問題**：GitHub Pages 是靜態網站，瀏覽器無法直接寫入伺服器端的 `learning.json`

**解決方案**：瀏覽器端透過 GitHub Contents API 讀取並更新 `learning.json`
- API endpoint：`PUT https://api.github.com/repos/CarryJone/english-learning/contents/vocabulary/learning.json`
- 需要 GitHub Personal Access Token（repo write 權限）
- Token 儲存在瀏覽器 localStorage（`github_pat`）— 首次使用時 prompt 輸入

**流程**：
1. 使用者完成 Active Recall Quiz，點擊「提交」
2. 瀏覽器讀取 GitHub 上的 learning.json（取得 SHA）
3. 根據答對/答錯，更新每個單字的 `reviewCount`、`nextReview`、`lastReviewedDate`
4. PUT 回 GitHub（會觸發 commit）
5. 隔天早上排程任務讀取已更新的 learning.json

### 6. 多次練習保護（防止 SRS 污染）

**問題**：如果一天練習多次，`reviewCount` 會被反覆 +1，破壞 SRS 精確度

**解決方案（雙重保護）**：
- `lastReviewedDate` 欄位：JS 比對 `lastReviewedDate === today` 則跳過更新
- localStorage `rq_done_YYYY-MM-DD`：同一天第二次點提交，顯示「額外練習，不更新記錄」

### 7. 閱讀理解率目標：~80% 熟悉詞彙

**問題**：初期文章有 6-7 成看不懂，閱讀效果差，學習受阻（Krashen i+1 理論要求 ~95% 可理解）

**解決方案**：
- 文章整體用 A2 常見詞彙為主（約 80% 已熟悉），避免大量生詞同時出現
- 每天只加入 3 個新單字，降低新詞密度
- 文章中融入 2-3 個複習單字（紫色底線，`review-word` class），讓學習者在真實語境中再次接觸

### 8. 複習單字融入文章（上下文記憶）

**決策**：每天的文章中自然融入 2-3 個到期複習單字

**設計**：
- 複習單字：紫色底線（`.review-word` class）
- 今日新單字：橘色底線（`.vocab-word` class）
- 片語：綠色底線（`.phrase-chunk` class）
- 點擊後彈出 popup，顯示例句，需點擊才顯示中文翻譯（active recall）

---

## learning.json 單字格式

```json
{
  "word": "routine",
  "partOfSpeech": "n.",
  "chineseMeaning": "日常慣例",
  "exampleSentence": "I try to keep a healthy morning routine.",
  "dateAdded": "2026-03-11",
  "reviewCount": 1,
  "nextReview": "2026-03-15",
  "lastReviewedDate": null
}
```

- `reviewCount`：已成功複習次數（答對才 +1，答錯歸零）
- `nextReview`：下次應該複習的日期
- `lastReviewedDate`：最後一次作答的日期（null = 從未作答）；用於防止同天多次更新 SRS

**archived 判斷**：`reviewCount >= 7` 的單字視為「已掌握」，排程任務和 Quiz 都不再顯示。不需要額外的 `archived` 欄位，直接用 reviewCount 判斷。

---

## 技術細節

### 語音生成（edge-tts）

```python
edge_tts.Communicate(text, voice="en-US-JennyNeural", rate="-10%")
```

每天生成：
- `article.mp3`：整篇文章朗讀
- `s01.mp3` ~ `sNN.mp3`：逐句朗讀（對應 HTML 中的 `data-idx`）

### Popup 定位（position: fixed）

**重要**：Popup 使用 `position: fixed`，座標基於 viewport，**不需要加 `window.scrollX/scrollY`**。

```javascript
function positionPopup(el) {
  const r = el.getBoundingClientRect(); // viewport 座標
  let left = r.left;
  let top = r.bottom + 8;
  if (left + pw > window.innerWidth - 12) left = window.innerWidth - pw - 12;
  if (left < 12) left = 12;
  if (r.bottom + ph + 8 > window.innerHeight) top = r.top - ph - 8;
  if (top < 8) top = 8;
  // 不要加 scrollX/scrollY！
}
```

### GitHub API UTF-8 base64 編解碼

**解碼**（GitHub → JSON）：
```javascript
const raw = atob(fileData.content.replace(/\n/g, ''));
const rawBytes = new Uint8Array(raw.length);
for (let i = 0; i < raw.length; i++) rawBytes[i] = raw.charCodeAt(i);
const vocab = JSON.parse(new TextDecoder('utf-8').decode(rawBytes));
```

**編碼**（JSON → GitHub）：
```javascript
const newBytes = new TextEncoder().encode(JSON.stringify(vocab, null, 2));
let binary = '';
newBytes.forEach(b => binary += String.fromCharCode(b));
const encoded = btoa(binary);
```

### Mac 喚醒設定

```bash
sudo pmset repeat wakeorpoweron MTWRF 06:50:00
```

原因：Mac 螢幕關閉後會睡眠，排程任務發送 tool call 後系統沒有回應，導致任務失敗。設定 6:50 AM 提前喚醒，確保 7:09 AM 任務正常執行。

---

## 已知問題與解決記錄

1. **2026-03-12 排程未執行**：Mac 睡眠導致 tool call 失敗 → 已設定 pmset wake alarm

2. **Popup 位置偏移（尤其手機）**：position:fixed 不需要加 scrollX/scrollY → 已修正所有 daily HTML 及 SKILL.md 模板

3. **Session log 存在錯誤路徑**：session log 存在 CreditCard 專案目錄而非 english-learning，屬 cosmetic 問題，不影響功能

---

## GitHub PAT 設定說明

1. 前往 https://github.com/settings/tokens → Generate new token (classic)
2. 勾選 `repo` 權限
3. 複製 token
4. 開啟任意一天的學習頁面，點擊「提交答案」
5. 第一次會 prompt 輸入 token，輸入後會儲存在 localStorage
6. 後續不需要再輸入

**安全提醒**：
- Token 只存在瀏覽器 localStorage，不會上傳到 GitHub
- 考慮將 repo 設為 private，避免學習記錄公開

---

## 待辦事項（截至 2026-03-12）

- [x] Day 1-3 學習內容（Airport / City Worker / Hotel）
- [x] 設定 Mac pmset 喚醒
- [x] 修正 popup 定位 bug
- [x] 文章融入複習單字（review-word class）
- [x] 每天新單字 3 個
- [x] 不設複習上限（所有到期單字）
- [x] Active Recall Quiz 卡片
- [x] GitHub API SRS 同步
- [x] lastReviewedDate 欄位（多次練習保護）
- [x] SRS archived 規則（reviewCount >= 7）
- [ ] 將 repo 設為 private（可選）
- [ ] 考慮 reviewCount 逾期懲罰（長時間未複習是否降低間隔）
