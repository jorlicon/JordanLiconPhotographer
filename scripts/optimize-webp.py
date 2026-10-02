#!/usr/bin/env python3
"""Convert the raster images referenced by a page to WebP and point the page at the WebP files.

Rewrites <img src/srcset>, <video poster> and CSS url() references to files under /assets/.
Also mirrors remote portfolio images (styles/xlarge on photos.headshotcrew.com) into
assets/headshots/ as WebP so the page serves them from this domain.
og:image / twitter:image metas, icon/manifest/canonical links and JSON-LD are left
untouched so social previews and structured data keep their original formats.

Usage: python3 scripts/optimize-webp.py --page architecture.html
"""
import argparse
import hashlib
import os
import re
import urllib.request
from urllib.parse import urlparse

DOMAIN = "https://www.jordanliconphotography.com"
URL_RE = re.compile(
    r'(?P<pre>["\'(\s])'
    r'(?P<url>(?:' + re.escape(DOMAIN) + r')?/?assets/[^"\'()\s]+?)\.(?:jpg|jpeg|png)'
    r'(?P<desc>(?:\s+\d+w)?)'
    r'(?=["\'\s,)])'
)
REMOTE_URL_RE = re.compile(
    r'(?P<pre>["\'(])'
    r'(?P<url>https://photos\.headshotcrew\.com/[^"\'()\s]+?\.(?:jpg|jpeg|png))'
    r'(?P<query>\?[^"\'()\s]*)?'
    r'(?=["\'\s,)])'
)
MIRROR_STYLE = '/styles/xlarge/'
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


def download(url, dst):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (site-image-optimizer)'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    with open(dst, 'wb') as fh:
        fh.write(data)
    return len(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--page', required=True)
    args = parser.parse_args()

    if args.page == 'blog.html':
        import subprocess
        subprocess.run(['node', 'scripts/update-homepage-blog.mjs'], check=True)

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
        base = ref[len(DOMAIN):].lstrip('/') if ref.startswith(DOMAIN) else ref.lstrip('/')
        src = None
        for ext in ('.jpg', '.jpeg', '.png'):
            if os.path.exists(base + ext):
                src = base + ext
                break
        if src is None:
            print('skip missing', base)
            continue
        dst = os.path.splitext(base)[0] + '.webp'
        if not os.path.exists(dst):
            from PIL import Image
            img = Image.open(src)
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

    # Mirror remote portfolio images into the repo as WebP and repoint the page.
    remote_map = {}
    remote_spans = []
    for m in REMOTE_URL_RE.finditer(new_html):
        if covered(m.start(), spans):
            continue
        pathurl = m.group('url')
        if MIRROR_STYLE not in pathurl:
            continue
        pathkey = urlparse(pathurl).path
        if pathkey not in remote_map:
            d = os.path.dirname(pathkey).lstrip('/')
            name = os.path.basename(pathkey)
            safe = hashlib.md5(d.encode('utf-8')).hexdigest()[:6] + '-' + name
            base = 'assets/headshots/' + safe
            src = base
            dst = os.path.splitext(base)[0] + '.webp'
            try:
                if not os.path.exists(dst):
                    if not os.path.exists(src):
                        os.makedirs('assets/headshots', exist_ok=True)
                        size = download(pathurl + (m.group('query') or ''), src)
                        print('downloaded', src, size, 'bytes')
                    from PIL import Image
                    img = Image.open(src)
                    img.save(dst, 'WEBP', quality=82, method=6)
                remote_map[pathkey] = dst
            except Exception as exc:
                print('skip remote', pathkey, exc)
                remote_map[pathkey] = None
        dst = remote_map[pathkey]
        if dst is None:
            continue
        webp_url = DOMAIN + '/' + os.path.splitext(dst)[0] + '.webp'
        remote_spans.append((m.span(), m.group('pre') + webp_url))
        rewritten += 1

    for (start, end), replacement in sorted(remote_spans, key=lambda item: item[0][0], reverse=True):
        new_html = new_html[:start] + replacement + new_html[end:]

    if not rewritten:
        print('no changes needed')
        return

    with open(args.page, 'w', encoding='utf-8') as fh:
        fh.write(new_html)
    print('rewrote %d references, %d remote files mirrored' % (rewritten, len(remote_map)))


if __name__ == '__main__':
    main()
