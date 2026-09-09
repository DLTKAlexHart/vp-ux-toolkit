# Vantagepoint Vibe Coding Kit

Lightweight HTML/CSS components and page templates that match the **current,
built Vantagepoint product** (the Harmony-reskinned look customers see today) —
for quickly creating mockups and prototypes in Claude Code, Cursor, or any
agentic IDE. No build step, no frameworks, no npm.

## Quick start

1. Download/clone this folder.
2. Open `index.html` in a browser (double-click works), or serve it:
   `python3 -m http.server` then visit http://localhost:8000.
3. Open the folder in your agentic IDE and prompt away, e.g.:

   > Using the kit in this folder, mock up a new "Consultant Invoices" list page
   > with columns for invoice #, firm, project, amount, and status. Start from
   > templates/list-view.html.

   Claude Code reads `CLAUDE.md` automatically; Cursor picks up
   `.cursor/rules/`. Both tell the agent how to use the kit correctly.

## What's inside

| Path | What it is |
|---|---|
| `css/vp-tokens.css` | **Design tokens extracted from the real product CSS** — 409 core tokens (light) + full dark theme. Generated, don't hand-edit. |
| `css/vp-base.css` | Reset, typography (1rem = 10px, Lexend), utilities. |
| `css/vp-shell.css` | App shell: 44px banner, 52px nav rail, flyout, page header. |
| `css/vp-components.css` | Buttons, fields, tabs, grids, dialogs, statuses, menus… |
| `js/vp-kit.js` | Tiny vanilla JS: tabs, dialogs, flyout, dark-mode toggle. |
| `js/vp-icons.js` | Injects the shared SVG icon sprite (source: `icons/_sprite.html`). |
| `templates/` | Full-shell starting pages: hub record, list view, settings + dialog. |
| `components.html` | Live component gallery with class names. |
| `docs/COMPONENTS.md` | Copy-paste markup reference (what agents read). |
| `CLAUDE.md` / `AGENTS.md` / `.cursor/rules/` | Agent guidance. |
| `scripts/extract-tokens.py` | Regenerates `vp-tokens.css` from a fresh product stylesheet. |

## Why this exists

The Harmony design system is our north star, but the shipped Vantagepoint
product deviates from it in many places (and skips parts of it entirely).
This kit is grounded in the **built product**: its tokens were machine-extracted
from the production stylesheet, so mockups made with it look like today's VP,
not the aspirational system. The component classes are clean/semantic
(`vp-btn`, `vp-field`, …) rather than the product's internal ExtJS class names,
so they're easy for designers and AI agents to compose.

## Updating when the product changes

1. Run Vantagepoint, open Chrome DevTools → Network, reload, and save the big
   `styles<date>.min.css` file.
2. Run `python3 scripts/extract-tokens.py path/to/that/file.css`.
3. Review the diff of `css/vp-tokens.css` and commit.

Component *recipes* (sizes, layouts) live in the other CSS files and only need
touching when the product visually changes.

## Fonts

Templates load **Lexend** (the product's UI font) from Google Fonts, with the
product's fallback stack (`tahoma, calibri, trebuchet ms`) when offline.
The product's **Harmony icon font** is not bundled; the kit uses inline SVG
icons instead. If you want font icons, drop `Harmony.woff2` from the product
repo into `fonts/` and add an `@font-face` — the glyph tokens
(`--harmony-icon-*`) are already in `vp-tokens.css`.

## Pattern alignment

Kit structure and conventions follow the **Vantagepoint UI Patterns** reference
(v2.0, bundled with the `vantagepoint-mockup` skill): Application Shell with
Right Utility Rail, Hub Toolbar, Record Header, Tab Bar, Record Sidebar,
Two-Column Field Layout with click-to-edit display fields, Named Grid Sections,
Info Bubbles, and the primary-LEFT / Cancel-RIGHT button convention. The
pattern-to-class mapping is at the top of `docs/COMPONENTS.md`.

Where that doc describes structure and behavior, this kit adds the exact
visual layer (real extracted tokens) — the two are complementary: patterns for
*what goes where*, kit for *what it looks like*.

## Known approximations

- Component dimensions (button height, paddings) are close approximations of
  the product; token colors/radii/fonts are exact.
- The nav rail/flyout is a simplified version of VP navigation (pin/unpin and
  inline module expansion not fully modeled).
- Dashboards aren't templated yet (`dashboards.scss` is a good source if you
  add one).
