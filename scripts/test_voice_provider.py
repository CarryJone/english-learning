"""Regression checks for offline voice declarations and historical edge pages."""
import json
import unittest
from pathlib import Path
from validate_daily import DailyHTMLParser, Validation, validate_voice_map

ROOT = Path(__file__).resolve().parents[1]

class VoiceProviderTests(unittest.TestCase):
    def page(self, day):
        parser = DailyHTMLParser()
        parser.feed((ROOT / 'daily' / day / 'index.html').read_text())
        return parser.page

    def validate(self, page):
        result = Validation()
        validate_voice_map(ROOT, '2026-10-13', page, result)
        return result.errors

    def test_historical_page_defaults_to_edge(self):
        page = self.page('2026-10-06')
        self.assertEqual(page.audio_provider, 'edge')
        self.assertEqual(self.validate(page), [])

    def test_current_page_uses_kokoro(self):
        page = self.page('2026-10-13')
        self.assertEqual(page.audio_provider, 'kokoro')
        self.assertEqual(self.validate(page), [])

    def test_edge_voice_rejected_on_kokoro_page(self):
        page = self.page('2026-10-13')
        config = json.loads((ROOT / 'assets/voices.json').read_text())
        page.voice_map = page.voice_map.replace(config['roles']['traveler']['kokoroVoice'], config['roles']['traveler']['voice'])
        self.assertTrue(self.validate(page))

    def test_unknown_provider_rejected(self):
        page = self.page('2026-10-13')
        page.audio_provider = 'unknown'
        self.assertTrue(self.validate(page))

if __name__ == '__main__':
    unittest.main()
