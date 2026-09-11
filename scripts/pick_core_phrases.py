#!/usr/bin/env python3
"""挑選每日 Survival Lines 核心句。

用法：
    python3 scripts/pick_core_phrases.py 2026-09-11            # 只預覽，不寫檔
    python3 scripts/pick_core_phrases.py 2026-09-11 --commit   # 標記 lastUsedOn / useCount 並寫回

輸出為 JSON 陣列 [{id, zh, en, audio}]，可直接填入頁面的 window.CORE_LINES。
選句規則見 .ai/daily-english-learning/SKILL.md 的 3h.1。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
STORE_PATH = PROJECT_ROOT / "vocabulary" / "core-phrases.json"
FAR_FUTURE = "9999-12-31"


def select(today: str, store: dict, count: int | None = None) -> list[dict]:
    count = count or store.get("dailyCount", 5)
    active = [item for item in store["items"] if item.get("activateOn", FAR_FUTURE) <= today]
    if not active:
        return []

    # 今天已經選過就回傳同一批，讓重新產生頁面是冪等的，不會重複累加 useCount。
    already = [item for item in active if item.get("lastUsedOn") == today]
    if already:
        return sorted(already, key=lambda item: item["id"])[:count]

    def sort_key(item: dict):
        due = 0 if (item.get("nextReview") or FAR_FUTURE) <= today else 1
        return (due, item.get("lastUsedOn") or "", item.get("useCount", 0), item["id"])

    return sorted(active, key=sort_key)[:count]


def variant_index(item: dict, today: str) -> int:
    """今天已選過就沿用當時的變化序號，否則依 useCount 輪替。"""
    if item.get("lastUsedOn") == today and item.get("lastVariant") is not None:
        return int(item["lastVariant"]) % len(item["variants"])
    return item.get("useCount", 0) % len(item["variants"])


def to_lines(picked: list[dict], store: dict, today: str) -> list[dict]:
    audio_dir = store.get("audioDir", "assets/core")
    lines = []
    for item in picked:
        variants = item["variants"]
        index = variant_index(item, today)
        variant = variants[index]
        lines.append(
            {
                "id": item["id"],
                "zh": variant["zh"],
                "en": variant["en"],
                "audio": f"../../{audio_dir}/{item['id']}-{index + 1:02d}.mp3",
            }
        )
    return lines


def mark_used(picked: list[dict], today: str) -> None:
    for item in picked:
        if item.get("lastUsedOn") == today:
            continue  # 已標記過，不重複累加
        item["lastVariant"] = variant_index(item, today)
        item["lastUsedOn"] = today
        item["useCount"] = item.get("useCount", 0) + 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("date", help="YYYY-MM-DD")
    parser.add_argument("--commit", action="store_true", help="寫回 lastUsedOn / useCount")
    parser.add_argument("--count", type=int, default=None, help="覆寫每日句數")
    args = parser.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        print("date must be YYYY-MM-DD", file=sys.stderr)
        return 2

    store = json.loads(STORE_PATH.read_text(encoding="utf-8"))
    picked = select(args.date, store, args.count)
    if not picked:
        print("no active core phrases for this date", file=sys.stderr)
        return 1

    lines = to_lines(picked, store, args.date)
    if args.commit:
        mark_used(picked, args.date)
        store["updatedAt"] = args.date
        STORE_PATH.write_text(json.dumps(store, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        active = sum(1 for i in store["items"] if i.get("activateOn", FAR_FUTURE) <= args.date)
        print(
            f"marked {len(picked)} phrases as used on {args.date} "
            f"({active}/{len(store['items'])} active)",
            file=sys.stderr,
        )

    print(json.dumps(lines, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
