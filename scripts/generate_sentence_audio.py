#!/usr/bin/env python3
"""Generate MP3 files for the reusable everyday-sentence page."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

import edge_tts


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        type=Path,
        default=PROJECT_ROOT / "sentences" / "data.json",
        help="Sentence JSON file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "sentences",
        help="Directory where the audio files are stored.",
    )
    parser.add_argument("--voice", default="en-US-JennyNeural")
    parser.add_argument("--rate", default="-5%")
    parser.add_argument(
        "--only-missing",
        action="store_true",
        help="Keep existing MP3 files and generate only missing files.",
    )
    return parser.parse_args()


async def generate_audio(text: str, destination: Path, voice: str, rate: str) -> None:
    communicator = edge_tts.Communicate(text, voice=voice, rate=rate)
    await communicator.save(str(destination))


async def main() -> None:
    args = parse_args()
    data_path = args.data if args.data.is_absolute() else PROJECT_ROOT / args.data
    output_dir = args.output if args.output.is_absolute() else PROJECT_ROOT / args.output
    entries = json.loads(data_path.read_text(encoding="utf-8"))
    output_dir.mkdir(parents=True, exist_ok=True)

    for index, entry in enumerate(entries, start=1):
        filename = entry.get("audio") or f"s{index:02d}.mp3"
        destination = output_dir / filename
        if args.only_missing and destination.exists() and destination.stat().st_size > 0:
            print(f"skip {filename}")
            continue
        await generate_audio(entry["en"], destination, args.voice, args.rate)
        print(f"generated {filename}: {entry['en']}")


if __name__ == "__main__":
    asyncio.run(main())
