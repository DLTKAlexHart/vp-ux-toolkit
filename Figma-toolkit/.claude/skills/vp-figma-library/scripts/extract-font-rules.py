#!/usr/bin/env python3
"""Print every CSS rule that sets a typographic property, one per line:
    file | selector | property: value ; property: value

Usage: python3 -I extract-font-rules.py <css-dir>
(<css-dir> is this repo's css/ folder; run from the repo root: python3 -I Figma-toolkit/.claude/skills/vp-figma-library/scripts/extract-font-rules.py css)
"""
import re
import sys
from pathlib import Path

PROPS = re.compile(
    r"\s*(font-size|font-weight|line-height|letter-spacing|text-transform|font-style|text-decoration)"
)

css_dir = Path(sys.argv[1])
for name in ("vp-base.css", "vp-components.css", "vp-shell.css"):
    css = re.sub(r"/\*.*?\*/", "", (css_dir / name).read_text(), flags=re.S)
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        selector = " ".join(m.group(1).split())
        props = [p.strip() for p in m.group(2).split(";") if PROPS.match(p)]
        if props:
            print(name, "|", selector[:70], "|", " ; ".join(" ".join(p.split()) for p in props))
