#!/bin/bash

# 取得所有有 index.html 的日期資料夾（由新到舊）
DATES_RAW=$(ls -r /Users/mds-macm3pro/english-learning/daily/ 2>/dev/null \
  | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' \
  | while read d; do
      [ -f "/Users/mds-macm3pro/english-learning/daily/$d/index.html" ] && echo "$d"
    done)

if [ -z "$DATES_RAW" ]; then
  osascript -e 'display alert "找不到任何學習記錄" message "請先執行每日學習排程" as warning'
  exit 1
fi

TODAY=$(date +%Y-%m-%d)

# 第一筆加上「今天」標記
DATES_LABELED=$(echo "$DATES_RAW" | awk -v today="$TODAY" '
  NR==1 && $0==today { print $0 " （今天）"; next }
  { print }
')

# 組成 AppleScript list 格式
DATES_AS=$(echo "$DATES_LABELED" | awk '{printf "\"%s\", ", $0}' | sed 's/, $//')

# 顯示原生選擇視窗
SELECTED=$(osascript <<EOF
set dateList to {$DATES_AS}
set chosen to choose from list dateList ¬
  with prompt "選擇要開啟哪一天的學習內容：" ¬
  default items {item 1 of dateList} ¬
  with title "📖 Daily English"
if chosen is false then return ""
return item 1 of chosen
EOF
)

# 取消就結束
[ -z "$SELECTED" ] && exit 0

# 去掉「（今天）」標記，取出純日期
DATE_KEY=$(echo "$SELECTED" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')

# 如果 8080 port 已在跑，先關掉
lsof -ti:8080 | xargs kill -9 2>/dev/null

# 背景啟動 HTTP server
cd /Users/mds-macm3pro/english-learning
python3 -m http.server 8080 &>/dev/null &

sleep 0.8

# 開啟選擇的日期
open "http://localhost:8080/daily/$DATE_KEY/"
