#!/usr/bin/env python3
"""Validate one daily English lesson page and its data links.

This project is a static site, so the validator uses only Python stdlib and
checks files as committed on disk. It intentionally avoids browser-only checks.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


REQUIRED_CARD_TITLES = [
    "Ability Focus",
    "Article",
    "New Words",
    "Key Phrases",
    "Quiz",
    "Active Recall Quiz",
    "Speaking Bridge",
    "Context Recall",
    "Learning Tips",
    "Daily Feedback",
    "Review Words",
]

REQUIRED_SCRIPT_SUFFIXES = [
    "assets/srs.js",
    "assets/sentence-srs.js",
    "assets/feedback.js",
]

MISSION_MODE_START_DATE = "2026-07-15"

ALLOWED_ABILITIES = {
    "travelSpeaking",
    "publicEnglish",
    "onlineReading",
    "dailyResponse",
}


@dataclass
class ParsedDailyPage:
    title_text: str = ""
    card_titles: list[str] = field(default_factory=list)
    sentence_indices: list[int] = field(default_factory=list)
    vocab_words: list[str] = field(default_factory=list)
    bridge_words: list[str] = field(default_factory=list)
    context_ids: list[str] = field(default_factory=list)
    context_rate_ratings: list[str] = field(default_factory=list)
    rq_items: int = 0
    roleplay_turns: int = 0
    script_srcs: list[str] = field(default_factory=list)


class DailyHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.page = ParsedDailyPage()
        self._stack: list[dict[str, Any]] = []

    @staticmethod
    def _classes(attrs: dict[str, str]) -> set[str]:
        return set(attrs.get("class", "").split())

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = {key: value or "" for key, value in attrs_list}
        classes = self._classes(attrs)
        capture = None

        if tag == "script" and attrs.get("src"):
            self.page.script_srcs.append(attrs["src"])

        if "sent" in classes and attrs.get("data-idx"):
            try:
                self.page.sentence_indices.append(int(attrs["data-idx"]))
            except ValueError:
                self.page.sentence_indices.append(-1)

        if "vocab-word" in classes and attrs.get("data-word"):
            self.page.vocab_words.append(attrs["data-word"].strip().lower())

        if "context-item" in classes and attrs.get("data-sentence-id"):
            self.page.context_ids.append(attrs["data-sentence-id"].strip())

        if "context-rate-btn" in classes and attrs.get("data-rating"):
            self.page.context_rate_ratings.append(attrs["data-rating"].strip())

        if "rq-item" in classes:
            self.page.rq_items += 1

        if "roleplay-turn" in classes:
            self.page.roleplay_turns += 1

        if "card-title" in classes:
            capture = "card-title"
        elif "bridge-word" in classes:
            capture = "bridge-word"
        elif tag == "h1":
            capture = "h1"

        self._stack.append({"tag": tag, "capture": capture, "text": []})

    def handle_endtag(self, tag: str) -> None:
        if not self._stack:
            return

        node = self._stack.pop()
        text = " ".join("".join(node["text"]).split())
        if node["capture"] == "card-title" and text:
            self.page.card_titles.append(text)
        elif node["capture"] == "bridge-word" and text:
            self.page.bridge_words.append(text.strip().lower())
        elif node["capture"] == "h1" and text:
            self.page.title_text = text

        if self._stack and text:
            self._stack[-1]["text"].append(text)

    def handle_data(self, data: str) -> None:
        if self._stack:
            self._stack[-1]["text"].append(data)


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.passed: list[str] = []

    def check(self, condition: bool, ok: str, fail: str) -> None:
        if condition:
            self.passed.append(ok)
        else:
            self.errors.append(fail)

    def warn(self, condition: bool, message: str) -> None:
        if not condition:
            self.warnings.append(message)


def load_json(path: Path, validation: Validation) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        validation.errors.append(f"missing JSON file: {path}")
    except json.JSONDecodeError as exc:
        validation.errors.append(f"invalid JSON in {path}: {exc}")
    return None


def parse_daily_page(path: Path) -> ParsedDailyPage:
    parser = DailyHTMLParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.page


def ymd_plus_one(ymd: str) -> str:
    return (datetime.strptime(ymd, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title).strip()


def validate_required_sections(page: ParsedDailyPage, date: str, validation: Validation) -> None:
    joined_titles = "\n".join(page.card_titles)
    required_titles = list(REQUIRED_CARD_TITLES)
    if date >= MISSION_MODE_START_DATE:
        required_titles.extend(["Mission", "Role-play"])

    for required in required_titles:
        validation.check(
            required in joined_titles,
            f"section present: {required}",
            f"missing required section/card title: {required}",
        )


def validate_scripts(root: Path, page: ParsedDailyPage, validation: Validation) -> None:
    for suffix in REQUIRED_SCRIPT_SUFFIXES:
        matched = [src for src in page.script_srcs if src.replace("../", "").endswith(suffix)]
        validation.check(
            bool(matched),
            f"script referenced: {suffix}",
            f"missing script reference ending with {suffix}",
        )
        validation.check(
            (root / suffix).exists(),
            f"script file exists: {suffix}",
            f"missing script file: {suffix}",
        )


def validate_audio(day_dir: Path, page: ParsedDailyPage, validation: Validation) -> None:
    article = day_dir / "article.mp3"
    validation.check(
        article.exists() and article.stat().st_size > 0,
        "article.mp3 exists and is non-empty",
        "missing or empty article.mp3",
    )

    indices = page.sentence_indices
    validation.check(bool(indices), "sentence spans exist", "no .sent data-idx sentence spans found")
    if not indices:
        return

    expected = list(range(1, max(indices) + 1))
    validation.check(
        indices == expected,
        f"sentence indices are continuous 1..{max(indices)}",
        f"sentence indices are not continuous: {indices[:10]}...",
    )

    missing_audio = []
    empty_audio = []
    for idx in expected:
        path = day_dir / f"s{idx:02d}.mp3"
        if not path.exists():
            missing_audio.append(path.name)
        elif path.stat().st_size <= 0:
            empty_audio.append(path.name)
    validation.check(not missing_audio, "all sentence mp3 files exist", f"missing sentence audio files: {missing_audio}")
    validation.check(not empty_audio, "all sentence mp3 files are non-empty", f"empty sentence audio files: {empty_audio}")

    extra_audio = sorted(path.name for path in day_dir.glob("s*.mp3") if re.fullmatch(r"s\d+\.mp3", path.name))
    expected_names = [f"s{idx:02d}.mp3" for idx in expected]
    validation.check(
        extra_audio == expected_names,
        "sentence mp3 file set matches sentence indices",
        f"sentence mp3 set mismatch: expected {expected_names}, found {extra_audio}",
    )


def validate_context_sentences(root: Path, date: str, page: ParsedDailyPage, validation: Validation) -> None:
    context_ids = page.context_ids
    minimum_context_items = 8 if date >= MISSION_MODE_START_DATE else 6
    validation.check(
        len(context_ids) >= minimum_context_items,
        f"Context Recall has {len(context_ids)} items",
        f"Context Recall has fewer than {minimum_context_items} items",
    )
    validation.check(len(context_ids) == len(set(context_ids)), "Context Recall ids are unique", "Context Recall ids contain duplicates")

    allowed_ratings = {"remembered", "hinted", "forgot"}
    expected_rating_count = len(context_ids) * len(allowed_ratings)
    validation.check(
        len(page.context_rate_ratings) == expected_rating_count,
        "Context Recall has 3 rating buttons per item",
        f"Context Recall rating button count mismatch: expected {expected_rating_count}, found {len(page.context_rate_ratings)}",
    )
    validation.check(
        set(page.context_rate_ratings).issubset(allowed_ratings),
        "Context Recall ratings are valid",
        f"invalid Context Recall ratings: {sorted(set(page.context_rate_ratings) - allowed_ratings)}",
    )
    if date >= MISSION_MODE_START_DATE:
        validation.check(
            page.roleplay_turns >= 4,
            f"Role-play has {page.roleplay_turns} turns",
            "Role-play has fewer than 4 turns",
        )

    store = load_json(root / "vocabulary" / "sentences.json", validation)
    if not store:
        return

    items = store.get("items", [])
    by_id = {item.get("id"): item for item in items if isinstance(item, dict)}
    missing = [item_id for item_id in context_ids if item_id not in by_id]
    validation.check(not missing, "all Context Recall ids exist in sentences.json", f"missing sentences.json items: {missing}")

    for item_id in context_ids:
        item = by_id.get(item_id)
        if not item:
            continue
        validation.check(
            item.get("sourceDate") == date,
            f"sentence sourceDate ok: {item_id}",
            f"sentence {item_id} has sourceDate {item.get('sourceDate')}, expected {date}",
        )
        validation.check(
            bool(item.get("zhPrompt")) and bool(item.get("answer")),
            f"sentence prompt/answer ok: {item_id}",
            f"sentence {item_id} missing zhPrompt or answer",
        )
        validation.check(
            item.get("nextReview") == ymd_plus_one(date),
            f"sentence nextReview ok: {item_id}",
            f"sentence {item_id} nextReview should start at {ymd_plus_one(date)}, found {item.get('nextReview')}",
        )


def validate_ability_map(root: Path, date: str, page: ParsedDailyPage, validation: Validation) -> None:
    data = load_json(root / "ability_map.json", validation)
    if not data:
        return

    sessions = data.get("sessions", [])
    matches = [session for session in sessions if session.get("date") == date]
    validation.check(bool(matches), "ability_map session exists for date", f"ability_map.json missing session for {date}")
    validation.check(len(matches) <= 1, "ability_map session is not duplicated", f"ability_map.json has duplicate sessions for {date}")
    if not matches:
        return

    session = matches[0]
    abilities = set(session.get("primary", [])) | set(session.get("secondary", []))
    validation.check(
        abilities.issubset(ALLOWED_ABILITIES),
        "ability ids are valid",
        f"invalid ability ids: {sorted(abilities - ALLOWED_ABILITIES)}",
    )
    validation.check(bool(session.get("primary")), "ability primary list is non-empty", "ability session primary list is empty")
    validation.check(bool(session.get("evidence")), "ability evidence is non-empty", "ability session evidence is empty")
    validation.check(
        session.get("url") == f"daily/{date}/",
        "ability session URL matches daily path",
        f"ability session URL mismatch: {session.get('url')}",
    )
    validation.warn(
        normalize_title(session.get("title", "")) in normalize_title(page.title_text),
        f"ability session title does not match page h1: {session.get('title')} vs {page.title_text}",
    )


def validate_vocabulary(root: Path, date: str, page: ParsedDailyPage, validation: Validation) -> None:
    vocab_words = sorted(set(word for word in page.vocab_words if word))
    validation.check(len(vocab_words) == 3, "page uses exactly 3 unique new vocab words", f"expected 3 unique vocab words, found {vocab_words}")

    data = load_json(root / "vocabulary" / "learning.json", validation)
    if not data:
        return

    words = data.get("words", [])
    by_word = {item.get("word", "").lower(): item for item in words if isinstance(item, dict)}
    missing = [word for word in vocab_words if word not in by_word]
    validation.check(not missing, "all page vocab words exist in learning.json", f"vocab words missing from learning.json: {missing}")

    for word in vocab_words:
        item = by_word.get(word)
        if not item:
            continue
        validation.check(
            item.get("dateAdded") == date,
            f"vocab dateAdded ok: {word}",
            f"vocab {word} dateAdded {item.get('dateAdded')}, expected {date}",
        )
        validation.check(
            item.get("nextReview") == ymd_plus_one(date),
            f"vocab nextReview ok: {word}",
            f"vocab {word} nextReview {item.get('nextReview')}, expected {ymd_plus_one(date)}",
        )

    bridge_words = sorted(set(word for word in page.bridge_words if word))
    overlap = sorted(set(vocab_words) & set(bridge_words))
    validation.check(not overlap, "Speaking Bridge does not use today's new vocab", f"Speaking Bridge uses today's new vocab: {overlap}")


def validate_homepage(root: Path, date: str, validation: Validation) -> None:
    index_path = root / "index.html"
    try:
        html = index_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        validation.errors.append("missing index.html")
        return

    href = f'href="daily/{date}/"'
    validation.check(href in html, "homepage links to daily page", f"homepage missing {href}")


def print_report(date: str, validation: Validation) -> None:
    status = "PASS" if not validation.errors else "FAIL"
    print(f"Daily validation {status}: {date}")
    print(f"passed: {len(validation.passed)}")
    print(f"warnings: {len(validation.warnings)}")
    print(f"errors: {len(validation.errors)}")

    if validation.errors:
        print("\nErrors:")
        for error in validation.errors:
            print(f"- {error}")

    if validation.warnings:
        print("\nWarnings:")
        for warning in validation.warnings:
            print(f"- {warning}")

    if not validation.errors:
        print("\nKey checks:")
        for item in validation.passed[:18]:
            print(f"- {item}")
        if len(validation.passed) > 18:
            print(f"- ... {len(validation.passed) - 18} more checks")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a daily English lesson.")
    parser.add_argument("date", help="Daily lesson date in YYYY-MM-DD format, e.g. 2026-07-07")
    parser.add_argument("--root", default=".", help="Project root, defaults to current directory")
    args = parser.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        print("date must be YYYY-MM-DD", file=sys.stderr)
        return 2

    root = Path(args.root).resolve()
    day_dir = root / "daily" / args.date
    html_path = day_dir / "index.html"
    validation = Validation()

    validation.check(day_dir.exists(), f"daily directory exists: {day_dir}", f"missing daily directory: {day_dir}")
    validation.check(html_path.exists(), f"daily index exists: {html_path}", f"missing daily index: {html_path}")
    if not html_path.exists():
        print_report(args.date, validation)
        return 1

    page = parse_daily_page(html_path)
    validate_required_sections(page, args.date, validation)
    validate_scripts(root, page, validation)
    validate_audio(day_dir, page, validation)
    validate_context_sentences(root, args.date, page, validation)
    validate_ability_map(root, args.date, page, validation)
    validate_vocabulary(root, args.date, page, validation)
    validate_homepage(root, args.date, validation)

    print_report(args.date, validation)
    return 0 if not validation.errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
