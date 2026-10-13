# 本機 Kokoro 音檔生成

2026-10-13 使用者要求改用不用帳號的語音方案。新每日教材預設使用 Kokoro；靜態網站與 MP3 播放方式不變。下載完成後，生成過程不需連網、帳號或 API key。

## 首次設定

Python 3.10–3.13、ffmpeg；本機目前 `.venv-tts` 為 Python 3.12。

```sh
python3.12 -m venv .venv-tts
.venv-tts/bin/python -m pip install kokoro-onnx==0.6.1 soundfile
mkdir -p .tts-cache
curl -fL -o .tts-cache/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/kokoro-v1.0.onnx
curl -fL -o .tts-cache/voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/voices-v1.0.bin
```

環境、模型已在 `.gitignore`，不提交大型模型。模型來源：thewh1teagle/kokoro-onnx 官方 README；模型 Apache-2.0、引擎 MIT。

## 每日使用

1. 依正式 SKILL 產出 HTML 與學習資料。
2. `<meta name="audio-provider" content="kokoro">`；`voice-map` 使用 `assets/voices.json` 的 `kokoroVoice`。沒有 provider meta 的歷史頁依 edge 設定驗證。
3. 執行：

```sh
.venv-tts/bin/python scripts/generate_daily_kokoro.py YYYY-MM-DD
python3 scripts/validate_daily.py YYYY-MM-DD
```

生成器直接讀 HTML 的逐句文字／speaker，產生 s01…sNN.mp3、article.mp3 與 audio-manifest.json。角色聲線、speed=0.8、模型路徑均來自 voices.json，不在脚本寫死。2026-10-13 使用者要求加長句間停頓，改用同角色 0.15／換人 0.25／段落切換 0.4 秒（providers.kokoro.pauses），全文時長仍必須 105–150 秒；若不合格優先調整內容，不為通過而改弱驗證。

## 聲線與歷史資產

- narrator：af_sarah；traveler：af_heart；staff：am_michael；companion：am_fenrir。
- Microsoft 聲線仍保留在 roles.voice；Kokoro 在 roles.kokoroVoice。同一 role 每篇只能代表一人。
- 舊每日音檔、共用 Survival Lines 不重生，仍是原聲線；不要更改它們的 voice-map。
- Kokoro 官方指出短句可能有發音／韻律弱點。實際生成後須檢查並試聽，不能以檔案存在取代聲音品質驗收。
