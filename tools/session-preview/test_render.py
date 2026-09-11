import json
from pathlib import Path
import tempfile
import unittest
import render


class PreviewTests(unittest.TestCase):
    def test_session_markdown_formats_blocks_and_inline_content(self):
        page = render.markdown('## Result\n\n**Ready** and *checked* with `code`.\n\n'
                               '- First\n- Second\n\n1. Ordered\n\n'
                               '| Name | Value |\n|---|---|\n| Bank | Example |\n\n'
                               '```python\nprint("ok")\n```\n\n[Source](https://example.com)')
        for expected in ['<h2>Result</h2>', '<strong>Ready</strong>', '<em>checked</em>',
                         '<code>code</code>', '<ul>', '<ol>', '<th>Name</th>',
                         '<td>Example</td>', '<pre><code', 'href="https://example.com"']:
            self.assertIn(expected, page)

    def test_session_markdown_does_not_execute_html_or_load_images(self):
        page = render.markdown('<script>alert(1)</script>\n\n'
                               '[bad](javascript:alert%281%29)\n\n'
                               '![remote](https://example.com/image.png)\n\n'
                               '<img src=x onerror=alert(1)>')
        self.assertNotIn('<script>', page)
        self.assertNotIn('<img', page)
        self.assertNotIn('href="javascript:', page)
        self.assertIn('&lt;script&gt;', page)
        self.assertIn('remote', page)

    def test_direct_session_uses_template_and_preserves_text(self):
        records = [
            {'type': 'message', 'message': {'role': 'user', 'content': 'Exact question\nsecond line'}},
            {'type': 'message', 'message': {'role': 'assistant', 'content': [
                {'type': 'thinking', 'thinking': 'PRIVATE THOUGHT'},
                {'type': 'text', 'text': 'Exact <answer>\nnext line'}]}},
            {'type': 'message', 'message': {'role': 'assistant', 'content': [],
                                          'errorMessage': 'Recorded failure'}},
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'trace.jsonl'
            source.write_text('\n'.join(json.dumps(r) for r in records))
            render.session(source, root / 'out')
            page = (root / 'out/session.html').read_text()
            self.assertIn('Exact question\nsecond line', page)
            self.assertIn('Exact &lt;answer&gt;\nnext line', page)
            self.assertIn('Recorded failure', page)
            self.assertNotIn('PRIVATE THOUGHT', page)
            self.assertIn('APIs used', page)
            self.assertIn('Private Pi session', page)
            self.assertIn('Unknown', page)
            self.assertNotIn('Edited task and result excerpt.', page)
            self.assertNotIn('$0.00', page)
            provenance = json.loads((root / 'out/source.json').read_text())
            self.assertEqual(provenance['message_count'], 3)

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
