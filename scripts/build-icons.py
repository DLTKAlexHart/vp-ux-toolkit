#!/usr/bin/env python3
"""Regenerate js/vp-icons.js from icons/_sprite.html after adding icons."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "icons" / "_sprite.html").read_text()
svg = src[src.index("<svg xmlns"):].strip()
out = f'''/* ==========================================================================
   vp-icons.js — injects the shared SVG icon sprite into the page.
   Include once per page: <script src="../js/vp-icons.js"></script>
   Then use: <svg class="vp-icon"><use href="#i-search"/></svg>
   Icon source of truth: icons/_sprite.html (regenerate this file by
   re-running scripts/build-icons.py if you add icons).
   ========================================================================== */
(function () {{
  var sprite = {svg!r};
  function inject() {{ document.body.insertAdjacentHTML("afterbegin", sprite); }}
  if (document.body) inject();
  else document.addEventListener("DOMContentLoaded", inject);
}})();
'''
(ROOT / "js" / "vp-icons.js").write_text(out)
print("wrote js/vp-icons.js")
