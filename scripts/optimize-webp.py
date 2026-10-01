#!/usr/bin/env python3
"""Convert the raster images referenced by a page to WebP and point the page at the WebP files.

Rewrites <img src/srcset>, <video poster> and CSS url() references to files under /assets/.
og:image / twitter:image metas, icon/manifest/canonical links and JSON-LD are left
untouched so social previews and structured data keep their original formats.

Usage: python3 scripts/optimize-webp.py --page architecture.html
"""
import argparse
import os
import re

DOMAIN = "https://www.jordanliconphotography.com"
URL_RE = re.compile(
    r'(?P<pre>["\'(\s])'
    r'(?P<url>(?:' + re.escape(DOMAIN) + r')?/?assets/[^"\'()\s]+?)\.(?:jpg|jpeg|png)'
    r'(?P<desc>(?:\s+\d+w)?)'
    r'(?=["\'\s,)])'
)
PROTECTED_TAG_RE = re.compile(r'image|icon|manifest|canonical|preload', re.I)


def protected_spans(html):
    spans = []
    for m in re.finditer(r'<script\b[^>]*>.*?</script>', html, re.S | re.I):
        spans.append(m.span())
    for m in re.finditer(r'<(?:meta|link)\b[^>]*>', html, re.I):
        if PROTECTED_TAG_RE.search(m.group(0)):
            spans.append(m.span())
    return spans


def covered(pos, spans):
    return any(start <= pos < end for start, end in spans)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--page', required=True)
    args = parser.parse_args()

    with open(args.page, encoding='utf-8') as fh:
        html = fh.read()
    spans = protected_spans(html)

    refs = []
    seen = set()
    for m in URL_RE.finditer(html):
        if covered(m.start(), spans):
            continue
        ref = m.group('url')
        if ref not in seen:
            seen.add(ref)
            refs.append(ref)

    webp_ref = {}
    for ref in refs:
        path = ref[len(DOMAIN):].lstrip('/') if ref.startswith(DOMAIN) else ref.lstrip('/')
        dst = os.path.splitext(path)[0] + '.webp'
        if not os.path.exists(path):
            print('skip missing', path)
            continue
        if not os.path.exists(dst):
            from PIL import Image
            img = Image.open(path)
            img.save(dst, 'WEBP', quality=82, method=6)
        webp_ref[ref] = os.path.splitext(ref)[0] + '.webp'

    out, last, rewritten = [], 0, 0
    for m in URL_RE.finditer(html):
        ref = m.group('url')
        if covered(m.start(), spans) or ref not in webp_ref:
            continue
        out.append(html[last:m.start()])
        out.append(m.group('pre') + webp_ref[ref] + m.group('desc'))
        last = m.end()
        rewritten += 1
    out.append(html[last:])
    new_html = ''.join(out)

    if not rewritten:
        print('no changes needed')
        return

    with open(args.page, 'w', encoding='utf-8') as fh:
        fh.write(new_html)
    print('rewrote %d references across %d files' % (rewritten, len(webp_ref)))


if __name__ == '__main__':
    main()
