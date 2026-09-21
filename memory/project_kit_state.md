---
name: project-kit-state
description: Current state and known gaps in the VP starter kit as of Sept 2026
metadata:
  type: project
---

Kit is functional and tuned against 4+ live product screens. Grid measurements
fully verified from production CSS (styles20260907204731.min.css) on 2026-09-09.
Tokens refreshed to Sept 7 build (no value changes from Sept 2).

**Why:** Internal tool to let VP team members and AI agents produce convincing product mockups without needing to understand ExtJS internals.

**How to apply:** When asked to extend the kit, check TUNING.md for what has/hasn't been measured, and docs/NOTES.md for the "next up" list.

## Known gaps (as of 2026-09-09)

- Per-column filter row operator dropdown (33px wide button before each input) — kit uses plain input only
- List-view extras: Bulk Update button, "View: Default" selector
- Pinned menu currently overlays content (product pushes it)
- Dashboard template not built
- Dark theme not yet side-by-side checked

## Measurement workflow for Claude Code (no browser extension)

File > Save Page As (Web Page, Complete) in Chrome while logged into VP.
Drop the folder into the project. The companion styles*.min.css is the production
stylesheet — feed it to scripts/extract-tokens.py to refresh tokens, and grep it
for specific component measurements. This works as well as DevTools for CSS values.

## Local dev

`python3 -m http.server 8811` from kit root (port 8000 often taken by another project).
