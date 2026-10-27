"""Recover one Hexo article body from a published HTML page.

Usage: python3 tools/recover_post_html.py INPUT_HTML OUTPUT_MD TITLE DATE
The output is review material; move it into source/_posts only after inspection.
"""

import html
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path


VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class ArticleBody(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth = 0
        self.parts = []
        self.stopped = False

    def handle_starttag(self, tag, attrs):
        if self.stopped:
            return
        classes = dict(attrs).get("class", "").split()
        if tag == "div" and "page-reward" in classes:
            self.stopped = True
            return
        if self.depth == 0:
            if tag == "div" and "article-entry" in classes:
                self.depth = 1
            return
        self.parts.append(self.get_starttag_text())
        if tag not in VOID_TAGS:
            self.depth += 1

    def handle_startendtag(self, tag, attrs):
        if self.depth and not self.stopped:
            self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if not self.depth or self.stopped:
            return
        self.depth -= 1
        if self.depth and not self.stopped:
            self.parts.append(f"</{tag}>")

    def handle_data(self, data):
        if self.depth and not self.stopped:
            self.parts.append(data)

    def handle_entityref(self, name):
        if self.depth and not self.stopped:
            self.parts.append(f"&{name};")

    def handle_charref(self, name):
        if self.depth:
            self.parts.append(f"&#{name};")


source, output, title, date = sys.argv[1:5]
parser = ArticleBody()
parser.feed(Path(source).read_text(encoding="utf-8"))
if not parser.parts:
    raise SystemExit("article-entry not found")
converted = subprocess.run(
    ["pandoc", "--from=html", "--to=gfm+raw_html"],
    input="".join(parser.parts),
    text=True,
    capture_output=True,
    check=True,
).stdout
front_matter = f"---\ntitle: {title}\ndate: {date}\ntags:\n  - reading\n  - 随笔\n---\n\n"
Path(output).write_text(front_matter + html.unescape(converted), encoding="utf-8")
