"""Offline Pi excerpt importer and static marketplace preview renderer."""
import argparse
import base64
from decimal import Decimal, InvalidOperation
import hashlib
import html
import json
from pathlib import Path
import re


def escape(value):
    return html.escape(str(value), quote=True)


def visible_messages(path):
    """Read Pi messages, never tool arguments/results or thinking blocks."""
    messages = []
    for line in path.read_text().splitlines():
        row = json.loads(line)
        if row.get('type') != 'message':
            continue
        msg = row.get('message', {})
        if msg.get('role') not in ('user', 'assistant'):
            continue
        content = msg.get('content', [])
        text = content if isinstance(content, str) else '\n\n'.join(
            b['text'] for b in content if b.get('type') == 'text' and b.get('text'))
        if text.strip():
            messages.append({'role': msg['role'], 'text': text})
        if msg.get('errorMessage'):
            messages.append({'role': msg['role'], 'text': msg['errorMessage']})
    return messages


def amount(value):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError('Money must be a decimal string or null')
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError('Invalid money amount') from exc
    if not result.is_finite() or result < 0:
        raise ValueError('Money must be finite and nonnegative')
    return result


def total(receipts, key):
    values = [amount(r.get(key)) for r in receipts]
    return sum(values, Decimal('0')) if values and all(v is not None for v in values) else None


def money(value):
    if value is None:
        return 'Unknown'
    return '$' + (format(value, '.2f') if value == value.quantize(Decimal('.01'))
                  else format(value, 'f').rstrip('0'))


def logo_data(root, filename):
    path = (root / filename).resolve()
    if not path.is_relative_to(root.resolve()) or path.suffix not in ('.svg', '.png', '.webp'):
        raise ValueError('Logo must be a local image inside the examples directory')
    mime = {'.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp'}[path.suffix]
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()


def render(data, root, *, messages=None):
    if messages is None and (data.get('reviewed') is not True or data.get('mode') not in ('live', 'replay')):
        raise ValueError('Only reviewed live or replay excerpts can be published')
    if not re.fullmatch(r'[a-z0-9-]+', data['id']):
        raise ValueError('Invalid example id')
    if not data.get('provenance'):
        raise ValueError('Source provenance is required')
    replay = data['mode'] == 'replay'
    providers = []
    receipts = []
    for p in data['providers']:
        rows = p['receipts']
        receipts.extend(rows)
        statuses = ', '.join(sorted({r['status'] for r in rows})) or 'unknown'
        logo = (f'<img alt="{escape(p["name"])} logo" src="{logo_data(root, p["logo"])}">'
                if p.get('logo') else '')
        providers.append(f'''<div class="provider"><div class="provider-name">
          {logo}
          <div><strong>{escape(p['name'])}</strong><small>{escape(p['service'])}</small></div></div>
          <dl><div><dt>Paid</dt><dd>{money(total(rows, 'paid_usd'))}</dd></div>
          <div><dt>Held</dt><dd>{money(total(rows, 'held_usd'))}</dd></div></dl>
          <small>{len(rows)} request{'s' if len(rows) != 1 else ''} · {escape(statuses)}</small></div>''')
    blocks = []
    for block in data['blocks']:
        kind = block['type']
        if kind == 'text':
            blocks.append(f'<p>{escape(block["text"])}</p>')
        elif kind == 'table':
            heads = ''.join(f'<th>{escape(c)}</th>' for c in block['columns'])
            body = ''.join('<tr>' + ''.join(f'<td>{escape(c)}</td>' for c in row) + '</tr>' for row in block['rows'])
            blocks.append(f'<div class="table-scroll"><table><thead><tr>{heads}</tr></thead><tbody>{body}</tbody></table></div>')
        elif kind == 'artifact':
            blocks.append(f'<div class="artifact"><span class="file-icon">↳</span><div><strong>{escape(block["name"])}</strong><small>{escape(block["detail"])}</small></div><span class="file-label">OUTPUT</span></div>')
        else:
            raise ValueError(f'Unknown block type: {kind}')
    paid, held = total(receipts, 'paid_usd'), total(receipts, 'held_usd')
    committed = paid + held if paid is not None and held is not None else None
    css = Path(__file__).with_name('style.css').read_text()
    mode = 'Saved-data replay' if replay else 'Recorded live run'
    if messages is not None:
        mode = 'Private Pi session'
    ledger = 'Original retrieval cost' if replay else 'API cost at capture'
    replay_note = '<p class="replay-note">This replay: <strong>$0.00 new spend</strong></p>' if replay else ''
    conversation = f'''<div class="user-row"><div class="user-bubble"><span class="message-label">YOU</span><p>{escape(data['prompt'])}</p></div></div>
    <div class="assistant"><div class="assistant-label"><span class="agent-mark">w</span><strong>Agent</strong><span>with Weft</span></div>
    <p class="intro">{escape(data['intro'])}</p>{''.join(blocks)}
    <div class="limits"><strong>What this result covers</strong><p>{escape(data['limits'])}</p></div></div>'''
    description = 'Edited task and result excerpt.<br>Original evidence retained.'
    if messages is not None:
        conversation = ''.join(
            f'<div class="user-row"><div class="user-bubble"><span class="message-label">YOU</span><p>{escape(m["text"])}</p></div></div>'
            if m['role'] == 'user' else
            f'<div class="assistant"><div class="assistant-label"><span class="agent-mark">w</span><strong>Agent</strong><span>with Weft</span></div><div class="session-text">{escape(m["text"])}</div></div>'
            for m in messages)
        description = 'Actual Pi message text, in file order.<br>Tools and reasoning omitted.<br>Private: review before sharing.'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="referrer" content="no-referrer"><title>{escape(data['title'])} · Weft</title><style>{css}</style></head>
    <body><header><a class="brand" href="index.html"><span class="mark">w</span>weft<span class="brand-sub"> / skill examples</span></a>
    <span class="header-label">REAL TASKS. RECORDED RESULTS.</span></header>
    <main><div class="heading"><div><span class="eyebrow">SKILL IN ACTION</span><h1>{escape(data['title'])}</h1>
    <p class="subtitle">{escape(data['skill'])}</p></div><span class="run-mode">{mode}</span></div>
    <div class="layout"><section class="conversation" aria-label="Conversation">
    {conversation}
    </section><aside aria-label="Providers and cost"><h2>APIs used</h2><p class="aside-sub">{ledger}</p>
    {''.join(providers)}<div class="total"><span>Paid + held</span><strong>{money(committed)}</strong></div>
    {replay_note}<p class="cost-note">Receipt amounts at the time of this run. Held funds are not settled payments. Agent model costs are not included.</p>
    <div class="run-details"><h2>About this example</h2><p>Run in Pi<br>{escape(data['date'])}</p><p>{description}</p></div>
    </aside></div><footer><span>weft.network</span><span>Recorded example · Results and prices can change</span></footer></main></body></html>'''


def build(source, output):
    output.mkdir(parents=True, exist_ok=True)
    examples = []
    for path in sorted(source.glob('*.json')):
        data = json.loads(path.read_text())
        page = render(data, source)
        (output / (data['id'] + '.html')).write_text(page)
        examples.append(data)
    cards = ''.join(f'<li><a href="{d["id"]}.html">{escape(d["title"])}</a> '
                    f'<a download href="{d["id"]}.png">PNG</a><p>{escape(d["skill"])}</p></li>' for d in examples)
    (output / 'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Weft skill examples</title><style>' + Path(__file__).with_name('style.css').read_text() + '</style><main><h1>See a skill in action</h1><p>Edited excerpts from recorded Pi runs. Choose an example or download its screenshot.</p><ul class="index">' + cards + '</ul></main></html>')
    return len(examples)


def session(source, output, metadata=None):
    """Render visible messages directly, without rewriting or public approval."""
    details = json.loads(metadata.read_text()) if metadata else {}
    messages = visible_messages(source)
    if not messages:
        raise ValueError('Session has no visible user or assistant text')
    data = dict(id='session', title=details.get('title', 'Pi skill session'),
                skill=details.get('skill', 'Recorded conversation'),
                date=details.get('date', 'Date not supplied'), mode='recorded',
                prompt='', intro='', blocks=[], limits='',
                providers=details.get('providers', []), provenance=[{
                    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()}])
    output.mkdir(parents=True, exist_ok=True)
    (output / 'session.html').write_text(render(data, metadata.parent if metadata else source.parent,
                                               messages=messages))
    (output / 'source.json').write_text(json.dumps({
        'source_sha256': data['provenance'][0]['source_sha256'],
        'message_count': len(messages), 'private': True,
        'ordering': 'physical file order; includes all recorded branches',
    }, indent=2) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['import', 'build', 'session'])
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--metadata', type=Path, help='Session title, date, skill and receipt-backed providers')
    args = parser.parse_args()
    if args.command == 'import':
        draft = {'reviewed': False, 'source_sha256': hashlib.sha256(args.source.read_bytes()).hexdigest(),
                 'messages': visible_messages(args.source)}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(draft, indent=2) + '\n')
        print('Private draft only: review and remove private content before publication.')
    elif args.command == 'session':
        session(args.source, args.output, args.metadata)
        print(f'Private Pi session rendered to {args.output}; review before sharing.')
    else:
        print(f'Rendered {build(args.source, args.output)} examples to {args.output}')
