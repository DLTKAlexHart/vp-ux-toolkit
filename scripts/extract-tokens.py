#!/usr/bin/env python3
"""
Regenerate css/vp-tokens.css from a Vantagepoint production CSS file.

Usage:
    python3 scripts/extract-tokens.py <path-to-product-min.css>

How it works:
    The built Vantagepoint stylesheet defines all design tokens as CSS custom
    properties on `body.harmony` (the current Harmony-reskinned look) with
    dark-mode overrides on `body.harmony[data-theme=dark]`, plus a small
    `:root` block of status tokens. This script pulls those three blocks out
    and rewrites them scoped to `:root` / `:root[data-theme="dark"]` so any
    plain HTML page can use them.

    Re-run this whenever you grab a fresh styles*.min.css from the product
    (Chrome DevTools > Network > the big styles...min.css file > Save).
"""
import re
import sys
import datetime
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent
OUT = KIT_ROOT / "css" / "vp-tokens.css"

# Tokens that are icon-font glyph codepoints (kept, but grouped separately).
GLYPH_PREFIXES = ("--harmony-icon", "--vp-icon", "--nav-icon", "--icon-")


def split_declarations(body: str):
    """Split a declaration block on `;`, but not inside url(), strings, etc."""
    decls, buf, depth, quote = [], [], 0, None
    for ch in body:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch == "(":
            depth += 1
            buf.append(ch)
        elif ch == ")":
            depth = max(0, depth - 1)
            buf.append(ch)
        elif ch == ";" and depth == 0:
            decls.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf:
        decls.append("".join(buf))
    return decls


def parse_block(body: str) -> dict:
    out = {}
    for decl in split_declarations(body):
        name, sep, value = decl.partition(":")
        name, value = name.strip(), value.strip()
        if sep and name.startswith("--") and value:
            # skip tokens pointing at product-internal assets (would 404 here);
            # keep data: URIs, which are self-contained
            if "url(" in value and "data:" not in value:
                continue
            out[name] = value
    return out


def extract(css: str) -> dict:
    wanted = {
        "body.harmony": "light",
        "body.harmony[data-theme=dark]": "dark",
        ":root": "root",
    }
    out = {}
    for m in re.finditer(r"([^{}]+)\{([^{}]*--[a-zA-Z][^{}]*)\}", css):
        sel = m.group(1).strip()
        if sel in wanted:
            props = parse_block(m.group(2))
            out.setdefault(wanted[sel], {}).update(props)
    return out


def emit(props: dict, indent: str = "  ") -> str:
    return "\n".join(f"{indent}{k}: {v};" for k, v in sorted(props.items()))


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    css = src.read_text(encoding="utf-8", errors="replace")
    tokens = extract(css)
    if "light" not in tokens:
        sys.exit("Could not find a `body.harmony` token block in that file.")

    light = tokens["light"]
    dark = tokens.get("dark", {})
    root = tokens.get("root", {})

    core_light = {k: v for k, v in light.items() if not k.startswith(GLYPH_PREFIXES)}
    glyphs = {k: v for k, v in light.items() if k.startswith(GLYPH_PREFIXES)}
    core_dark = {k: v for k, v in dark.items() if not k.startswith(GLYPH_PREFIXES)}

    stamp = datetime.date.today().isoformat()
    out = f"""/* ==========================================================================
   Vantagepoint design tokens — extracted from the BUILT product
   Source: {src.name}
   Generated: {stamp} by scripts/extract-tokens.py — do not edit by hand;
   re-run the script against a fresh product CSS instead.

   Light theme = `body.harmony` block (current Harmony-reskinned VP look).
   Dark theme  = `body.harmony[data-theme=dark]` overrides.
   Toggle dark mode by setting  <html data-theme="dark">.
   ========================================================================== */

:root {{
  color-scheme: light;

  /* --- status tokens (product :root block) --- */
{emit(root)}

  /* --- core tokens (colors, layout, typography) --- */
{emit(core_light)}

  /* --- icon glyph map (Harmony icon font codepoints; needs fonts/Harmony.woff2) --- */
{emit(glyphs)}
}}

:root[data-theme="dark"] {{
  color-scheme: dark;
{emit(core_dark)}
}}
"""
    OUT.write_text(out, encoding="utf-8")
    print(
        f"Wrote {OUT} — {len(core_light)} core tokens, "
        f"{len(core_dark)} dark overrides, {len(glyphs)} icon glyphs."
    )


if __name__ == "__main__":
    main()
