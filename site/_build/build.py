#!/usr/bin/env python3
"""Build site pages: wrap src/*.html content with shared head/nav/footer.
Src format: first line = TITLE: ..., optional CTA_* override lines, then body content."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent   # site/
SRC = ROOT / '_build' / 'src'
NAV = (ROOT / '_build' / 'nav.html').read_text(encoding='utf-8')
FOOTER_TPL = (ROOT / '_build' / 'footer.html').read_text(encoding='utf-8')

HEAD = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,300;1,9..144,400&family=Be+Vietnam+Pro:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/base.css">
</head>
<body>
'''

DEFAULTS = {
    'CTA_TITLE': 'Sẵn sàng thắp lại ngọn đèn bên trong?',
    'CTA_SUB': 'Bắt đầu bằng một buổi kết nối miễn phí — cùng lắng nghe và tìm hướng đi phù hợp nhất cho bạn.',
    'CTA_BTN': 'Đặt lịch khai vấn',
}

for src in sorted(SRC.glob('*.html')):
    lines = src.read_text(encoding='utf-8').split('\n')
    meta = dict(DEFAULTS)
    title = 'Coach Hà Bùi'
    body_start = 0
    for i, ln in enumerate(lines):
        m = re.match(r'^(TITLE|CTA_TITLE|CTA_SUB|CTA_BTN):\s*(.+)$', ln)
        if m:
            if m.group(1) == 'TITLE':
                title = m.group(2)
            else:
                meta[m.group(1)] = m.group(2)
            body_start = i + 1
        elif ln.strip() == '':
            body_start = i + 1
        else:
            break
    body = '\n'.join(lines[body_start:])
    footer = FOOTER_TPL
    for k, v in meta.items():
        footer = footer.replace('{{' + k + '}}', v)
    out = HEAD.format(title=title) + NAV + '\n' + body + '\n' + footer + '\n</body>\n</html>\n'
    dest = ROOT / src.name
    dest.write_text(out, encoding='utf-8')
    print(f'built {dest.name} ({len(out)} bytes)')
