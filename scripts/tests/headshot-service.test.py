"""Run from the repository root: python3 scripts/tests/headshot-service.test.py."""

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.ids = []
        self.scripts = []
        self.script = None
        self.visible = []
        self.in_main = False
        self.h1_count = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "main":
            self.in_main = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "script":
            self.script = [attrs, ""]

    def handle_data(self, data):
        if self.script is not None:
            self.script[1] += data
        elif self.in_main:
            self.visible.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.scripts.append(self.script)
            self.script = None
        if tag == "main":
            self.in_main = False


root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
html = (root / "el-paso-headshot-photographer.html").read_text()
page = Page(html)
portfolio = Page((root / "headshot-portfolio.html").read_text())
assert page.h1_count == 1
assert len(page.ids) == len(set(page.ids)), "Duplicate element IDs"
canonicals = [a["href"] for tag, a in page.tags if tag == "link" and a.get("rel") == "canonical"]
assert canonicals == ["https://www.jordanliconphotography.com/el-paso-headshot-photographer.html"]
assert not any("noindex" in a.get("content", "") for tag, a in page.tags if tag == "meta" and a.get("name") == "robots")

images = [a for tag, a in page.tags if tag == "img"]
assert len(images) == 3
assert images[0].get("loading") != "lazy"
assert all(a.get("alt") and a.get("width") == "1800" and a.get("height") == "1200" for a in images)
assert all(a["src"].startswith("assets/headshots/") and a["src"].endswith(".webp") for a in images)
assert all(a["src"] in {urlsplit(p.get("src", "")).path.lstrip("/") for tag, p in portfolio.tags if tag == "img"} for a in images)

booking = 'href="https://jordan-licon-photography.bloom.io/Professional-Headshot"'
assert html.index(booking) < html.index('<section class="headshot-examples"')
assert html.index('href="headshot-portfolio.html"') < html.index('<section class="headshot-examples"')
for tag, attrs in page.tags:
    if tag != "a":
        continue
    target = urlsplit(attrs.get("href", ""))
    if target.path == "headshot-portfolio.html" and target.fragment:
        assert target.fragment in portfolio.ids, f"Missing portfolio anchor: {target.fragment}"
visible = " ".join(" ".join(page.visible).split())
assert "$350" in visible and "$200" in visible and "three outfits" in visible
assert "2201 East Mills Ave, 2nd Floor, El Paso, TX 79901" in visible
for attrs, content in page.scripts:
    if attrs.get("type") == "application/ld+json":
        data = json.loads(content)
        if data.get("@type") == "FAQPage":
            for question in data["mainEntity"]:
                assert question["name"] in visible
                assert question["acceptedAnswer"]["text"] in visible
if len(sys.argv) > 2:
    original = Page(Path(sys.argv[2]).read_text())
    assert original.scripts == page.scripts, "Tracking or structured data changed"
    for key in ("canonical",):
        assert [a for tag, a in original.tags if tag == "link" and a.get("rel") == key] == [a for tag, a in page.tags if tag == "link" and a.get("rel") == key]
print("PASS: early booking links, existing sample images, pricing, canonical, FAQ and portfolio anchors")
