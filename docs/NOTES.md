# Working notes

Loose session-to-session state for whoever (human or AI) picks this up next.
Keep it short — durable facts belong in TUNING.md (measurements),
COMPONENTS.md (markup), or CLAUDE.md (conventions). Update before ending a
work session.

## Current state (2026-11-03, session 2)

Nav tuning pass complete (measured from live product via computed styles + screenshots):
- Nav items corrected to 42×32px (were 40×40)
- All hub templates switched from SVG sprite icons to Harmony glyphs in the nav rail
- Full production module order applied to all templates
- Utility rail corrected: Dela hicon · Insights · Notifications · Help (removed Pin, People)
- `css/vp-hicons.css` now required on all page types (not dashboard-only)
- All agent guides updated and in sync

Key facts:
- Widget CSS lives in `css/vp-components.css` (lines 942–989) — no build needed
- Floating nav/rail is a modifier on the existing `.vp-nav` / `.vp-utility-rail` base
- `js/vp-nav.js` is optional vanilla JS only — no framework, no build step
- All agent guides (CLAUDE.md, AGENTS.md, .cursor/rules/vp-kit.mdc, docs/COMPONENTS.md) are in sync

## Next up

- Pinned nav menu (expanded state): verify the full item list and "Unpin Menu" header against the live product pinned view — screenshots captured, deeper pass pending
- List-view extras: Bulk Update button, "View: Default" selector
- Per-column filter row operator dropdown (33px wide button before each filter input) — kit has plain input only, sufficient for mockups
- Dashboard widget components (KPI tiles, charts, sparklines) — dashboard shell template exists but widgets are not built
- Dark theme side-by-side check against product dark mode

## Working setup

- Iterate in Cowork with this folder selected, or Claude Code/Cursor in the repo.
- Live-product tuning workflow: open the real VP screen in Chrome, move the tab
  into the Claude tab group, and ask Claude to screenshot + measure computed
  styles (see TUNING.md "How to re-measure"). Alternatively: File > Save Page
  As (complete web page) and drop the folder into the project — the companion
  styles*.min.css can be fed directly to scripts/extract-tokens.py.
- Local preview: `python3 -m http.server 8811` from the kit root
  (port 8000 is often taken by another local project).

## Decisions log

- 2026-09-02: Canonical home will be an enterprise GitHub repo; kit folder is
  the repo root. Raw product stylesheets stay OUT of the repo (bulky inputs,
  not deliverables) — regenerate tokens via scripts/extract-tokens.py.
- 2026-09-02: No Claude Project for kit-building; folder docs are the memory.
  A Project may be added later purely as a Q&A front door for colleagues.
- 2026-09-09: "Save page as complete" is a viable measurement workflow for
  Claude Code (no browser extension available in CLI). Drop the saved
  styles*.min.css into the project, run extract-tokens.py, grep for measurements.
