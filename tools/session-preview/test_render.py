import json
from pathlib import Path
import tempfile
import unittest
import render


class PreviewTests(unittest.TestCase):
    def test_import_excludes_reasoning_tools_and_metadata(self):
        records = [
            {'type': 'session', 'secret': 'hidden'},
            {'type': 'message', 'message': {'role': 'user', 'content': 'Question'}},
            {'type': 'message', 'message': {'role': 'assistant', 'content': [
                {'type': 'thinking', 'thinking': 'hidden reasoning'},
                {'type': 'toolCall', 'arguments': {'secret': 'hidden'}},
                {'type': 'text', 'text': 'Visible answer'}]}},
            {'type': 'message', 'message': {'role': 'toolResult', 'content': [{'type': 'text', 'text': 'hidden receipt'}]}},
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'session.jsonl'
            path.write_text('\n'.join(json.dumps(r) for r in records))
            self.assertEqual(render.visible_messages(path), [
                {'role': 'user', 'text': 'Question'},
                {'role': 'assistant', 'text': 'Visible answer'}])

    def test_decimal_money_and_unknown_are_distinct(self):
        self.assertEqual(render.money(render.total([{'held_usd': '0.01'}] * 4, 'held_usd')), '$0.04')
        self.assertEqual(render.money(render.amount('0.260981')), '$0.260981')
        self.assertEqual(render.money(render.amount('0.00')), '$0.00')
        self.assertEqual(render.money(render.total([{}], 'paid_usd')), 'Unknown')
        for bad in ['NaN', 'Infinity', '-1', 0.1]:
            with self.assertRaises(ValueError):
                render.amount(bad)

    def test_sample_render_escapes_and_labels_replay(self):
        root = Path(__file__).resolve().parents[2] / 'examples/session-previews'
        data = json.loads((root / 'stock-news-sentiment.json').read_text())
        data['prompt'] = '<script>alert("bad")</script>'
        page = render.render(data, root)
        self.assertNotIn('<script>', page)
        self.assertIn('&lt;script&gt;', page)
        self.assertIn('Original retrieval cost', page)
        self.assertIn('$0.00 new spend', page)
        self.assertIn('Held', page)
        data['reviewed'] = False
        with self.assertRaises(ValueError):
            render.render(data, root)

    def test_logo_paths_cannot_escape_source(self):
        with self.assertRaises(ValueError):
            render.logo_data(Path('/tmp/examples'), '../secret.png')


if __name__ == '__main__':
    unittest.main()
