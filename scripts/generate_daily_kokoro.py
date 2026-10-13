#!/usr/bin/env python3
"""Generate offline role-specific daily MP3s with voices from assets/voices.json.

Setup and model download instructions: scripts/KOKORO.md.
Usage: .venv-tts/bin/python scripts/generate_daily_kokoro.py YYYY-MM-DD
"""
from __future__ import annotations
import argparse
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path
import numpy as np
import soundfile as sf
import onnxruntime as ort
# Audio generation is local; disable runtime telemetry.
ort.disable_telemetry_events()
from kokoro_onnx import Kokoro
from validate_daily import DailyHTMLParser

ROOT = Path(__file__).resolve().parents[1]

class AudioTextParser(DailyHTMLParser):
    def handle_data(self, data: str) -> None:
        # Playback button labels are UI, not words to synthesize.
        if not any(node['tag'] == 'button' for node in self._stack):
            super().handle_data(data)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('date')
    args = parser.parse_args()
    # Restrict output to a real daily lesson directory.
    from datetime import date
    date.fromisoformat(args.date)
    folder = ROOT / 'daily' / args.date
    html_path = folder / 'index.html'
    html = html_path.read_text(encoding='utf-8')
    parsed = AudioTextParser()
    parsed.feed(html)
    page = parsed.page
    config = json.loads((ROOT / 'assets/voices.json').read_text(encoding='utf-8'))
    cfg = config['providers']['kokoro']
    voice_map = {role: value[cfg['voiceField']] for role, value in config['roles'].items()}
    assert page.audio_provider == 'kokoro', 'Declare audio-provider=kokoro before generating'
    used = set(page.sentence_speakers)
    declared = dict(pair.split('=', 1) for pair in page.voice_map.split(';'))
    assert declared == {role: voice_map[role] for role in used}, 'HTML/config voice map mismatch'
    assert page.sentence_indices == list(range(1, len(page.sentence_texts) + 1))
    assert page.sentence_texts and all(page.sentence_texts)
    model_path, voices_path = ROOT / cfg['modelPath'], ROOT / cfg['voicesPath']
    kokoro = Kokoro(str(model_path), str(voices_path))
    available = set(kokoro.get_voices())
    assert set(voice_map.values()) <= available, 'Model lacks a configured voice'
    full = []
    manifest = []
    with tempfile.TemporaryDirectory(prefix='english-kokoro-') as temp:
        temp_path = Path(temp)
        for i, (text, role) in enumerate(zip(page.sentence_texts, page.sentence_speakers), 1):
            samples, rate = kokoro.create(text, voice=voice_map[role], speed=cfg['speed'], lang=cfg['language'])
            assert rate == 24000 and len(samples) and np.isfinite(samples).all()
            wav = temp_path / f's{i:02d}.wav'
            sf.write(wav, samples, rate)
            target = temp_path / f's{i:02d}.mp3'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(wav), '-ar', '24000', '-ac', '1', '-b:a', '48k', str(target)], check=True)
            target.replace(folder / target.name)
            full.append(samples)
            if i < len(page.sentence_texts):
                next_role = page.sentence_speakers[i]
                # Stage transition: narration starts after a spoken turn.
                kind = 'stageChange' if next_role == 'narrator' and role != 'narrator' else 'sameSpeaker' if next_role == role else 'speakerChange'
                gap = cfg['pauses'][kind]
                full.append(np.zeros(round(gap * rate), dtype=np.float32))
            manifest.append({'index': i, 'speaker': role, 'voice': voice_map[role], 'text': text, 'seconds': len(samples) / rate})
            print(f'generated s{i:02d}.mp3 ({len(samples) / rate:.2f}s)', flush=True)
        audio = np.concatenate(full)
        wav = temp_path / 'article.wav'
        sf.write(wav, audio, 24000)
        output = temp_path / 'article.mp3'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(wav), '-ar', '24000', '-ac', '1', '-b:a', '48k', str(output)], check=True)
        output.replace(folder / 'article.mp3')
    evidence = {'provider': 'kokoro', 'speed': cfg['speed'], 'language': cfg['language'],
                'modelSHA256': hashlib.sha256(model_path.read_bytes()).hexdigest(),
                'voicesSHA256': hashlib.sha256(voices_path.read_bytes()).hexdigest(),
                'pauses': cfg['pauses'], 'sentences': manifest, 'articleSeconds': len(audio) / 24000}
    (folder / 'audio-manifest.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Full audio: {len(audio) / 24000:.3f}s')

if __name__ == '__main__':
    main()
