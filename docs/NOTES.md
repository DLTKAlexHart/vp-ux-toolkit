# Working notes

Loose session-to-session state for whoever (human or AI) picks this up next.
Keep it short — durable facts belong in TUNING.md (measurements),
COMPONENTS.md (markup), or CLAUDE.md (conventions). Update before ending a
work session.

## Current state (2026-09-02)

Kit is functional and tuned against four live product screens (Firm record,
Employees list + filter popup, Projects record + pinned menu, two dialogs).
All measured values logged in TUNING.md. Templates render convincingly
side-by-side with the real product.

## Next up

- Grid row height / cell padding — measure against a real grid
- Per-column filter row (≈ operator inputs under grid headers) — not built yet
- List-view extras: Bulk Update button, "View: Default" selector
- Consider: pinned menu pushing content (currently overlays)
- Dashboard template (dashboards.scss in the parent folder is the source)
- Eventually: dark theme side-by-side check against product dark mode

## Working setup

- Iterate in Cowork with this folder selected, or Claude Code/Cursor in the repo.
- Live-product tuning workflow: open the real VP screen in Chrome, move the tab
  into the Claude tab group, and ask Claude to screenshot + measure computed
  styles (see TUNING.md "How to re-measure").
- Local preview: `python3 -m http.server 8811` from the kit root
  (port 8000 is often taken by another local project).

## Decisions log

- 2026-09-02: Canonical home will be an enterprise GitHub repo; kit folder is
  the repo root. Raw product stylesheets stay OUT of the repo (bulky inputs,
  not deliverables) — regenerate tokens via scripts/extract-tokens.py.
- 2026-09-02: No Claude Project for kit-building; folder docs are the memory.
  A Project may be added later purely as a Q&A front door for colleagues.
