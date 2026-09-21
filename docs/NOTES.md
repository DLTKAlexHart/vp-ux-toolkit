# Working notes

Loose session-to-session state for whoever (human or AI) picks this up next.
Keep it short — durable facts belong in TUNING.md (measurements),
COMPONENTS.md (markup), or CLAUDE.md (conventions). Update before ending a
work session.

## Current state (2026-09-10)

Grid and hub record shell both tuned. Token file refreshed to Sept 9 build
(styles20260909205338.min.css from Projects hub pages — same token values as Sept 7).

Hub record shell changes applied (see TUNING.md for details):
- Module label: corrected to 1.8rem (was 1.5rem), now uses `--font-size-application-header`
- Record ID line: corrected to 1.5rem/500 (was 1.2rem), now uses `--color-title-subheader-text`
- Record name + modified line: switched from hardcoded `#555555` to correct tokens
  (`--color-title-header-text` / `--color-title-secondary-subheader-text`) — these
  properly adapt to dark mode (#dddddd in dark)
- Sidebar section padding: 10px 8px 0 (was 12px 14px 0)
- Template default: hub toolbar now shows `+ New Project`, Save/Cancel in comment
- Tabs: `text-transform: uppercase; letter-spacing: 0.03em` added to `.vp-tab`
  (confirmed from production .ngcrm-tabs stylesheet rule)

## Next up

- Per-column filter row operator dropdown (33px wide button before each filter input) — kit has plain input only, sufficient for mockups
- List-view extras: Bulk Update button, "View: Default" selector
- Consider: pinned menu pushing content (currently overlays)
- Dashboard template (dashboards.scss in the parent folder is the source)
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
