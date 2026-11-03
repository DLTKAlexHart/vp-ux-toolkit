---
name: project-kit-state
description: Current state and known gaps in the VP starter kit as of Sept 2026
metadata:
  type: project
---

Kit is functional and tuned. Now being actively used and collaborated on with a colleague (Christopher Brown). All agent guides (CLAUDE.md, AGENTS.md, .cursor/rules/vp-kit.mdc, docs/COMPONENTS.md) are in sync as of 2026-11-03.

**Why:** Internal tool to let VP team members and AI agents produce convincing product mockups without needing to understand ExtJS internals.

**How to apply:** When asked to extend the kit, check TUNING.md for what has/hasn't been measured, and docs/NOTES.md for the "next up" list.

## Known gaps (updated 2026-11-03)

- Per-column filter row operator dropdown (33px wide button before each input) — kit uses plain input only
- List-view extras: Bulk Update button, "View: Default" selector
- Pinned menu currently overlays content (product pushes it)
- Dashboard widget components (KPI tiles, charts, sparklines) — shell template exists, widgets not built
- Dark theme not yet side-by-side checked

## Recent additions (Christopher's PR, merged 2026-11-02)

- Dashboard shell template (`templates/dashboard-shell.html`) with floating nav + utility rail on workbench surface
- Harmony and Vantagepoint icon fonts (`fonts/`, `css/vp-hicons.css`), `.vp-hicon` glyph classes
- `js/vp-nav.js` — optional helper to render floating nav and utility rail from JS arrays (no framework, vanilla only)
- New shell CSS classes: `.vp-app--workbench`, `.vp-nav--floating`, `.vp-utility-rail--floating`, `.vp-dash-card`, `.vp-app-header`

## Measurement workflow for Claude Code (no browser extension)

File > Save Page As (Web Page, Complete) in Chrome while logged into VP.
Drop the folder into the project. The companion styles*.min.css is the production
stylesheet — feed it to scripts/extract-tokens.py to refresh tokens, and grep it
for specific component measurements. This works as well as DevTools for CSS values.

## Local dev

`python3 -m http.server 8811` from kit root (port 8000 often taken by another project).
