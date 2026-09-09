# Vantagepoint Vibe Coding Kit — agent guide

You are building **mockups and prototypes that look like the current, built Deltek
Vantagepoint product** (the Harmony-reskinned look), using this kit's CSS and
markup patterns. This is NOT the "north star" Harmony design system — it matches
what customers actually see today.

## Rules

1. **Always use the kit's CSS.** Link these four files (in this order) in every page:
   `css/vp-tokens.css`, `css/vp-base.css`, `css/vp-shell.css`, `css/vp-components.css`,
   plus `js/vp-icons.js` and `js/vp-kit.js` (both `defer`). Use relative paths.
2. **Never hardcode colors, radii, or fonts.** Use the CSS custom properties from
   `css/vp-tokens.css` (e.g. `var(--color-button-bg-primary)`). They were extracted
   from the real product stylesheet — treat them as ground truth.
3. **Copy markup patterns** from `templates/*.html` and `components.html` rather than
   inventing new structures. Class reference: `docs/COMPONENTS.md`.
4. **Start new pages from a template.** For a record/detail screen copy
   `templates/hub-record.html`; for a list screen copy `templates/list-view.html`;
   for settings/forms copy `templates/settings-form.html`. Keep the shell
   (banner + nav rail) intact so mockups feel like real product screens.
5. **Icons:** use the inline sprite via `<svg class="vp-icon"><use href="#i-NAME"/></svg>`.
   Available ids are in `icons/_sprite.html`. To add an icon, add a `<symbol>` there
   and run `python3 scripts/build-icons.py`.
6. **Page-specific styles** go in a `<style>` block in that page, built on tokens —
   don't edit the shared `css/` files for a one-off mockup.
7. **Dark mode** works automatically: set `data-theme="dark"` on `<html>`
   (there's a toggle wired to `data-vp-theme-toggle`). Don't write custom dark styles;
   the tokens handle it.
8. **Typography:** `html` is `font-size: 62.5%`, so 1rem = 10px. Body text is 1.4rem
   Lexend. Don't change the root font size.
9. **No frameworks, no build step.** Plain HTML/CSS/vanilla JS only. Pages must work
   when opened directly from disk.

## VP conventions you must follow (from the UI pattern reference v2.0)

- **Button pairs: primary/destructive LEFT, Cancel RIGHT** — everywhere,
  including dialog footers. This is the reverse of most apps.
- **Click-to-edit:** fields at rest are plain text (`.vp-dfield` — bold label,
  value below; empty = gray "None"). Only actively-edited fields render as
  bordered inputs (`.vp-field`). Don't build forms as walls of inputs.
- **Hub pages** always have, top to bottom: Hub Toolbar (`.vp-hub-toolbar` —
  module label, Find, Filter, pager `‹ N of NNN ›`, `+ New [record type]`),
  Record Header (`.vp-record-header` — name, ID/hierarchy, "Last modified …
  by …" line, actions right: Dela Actions ✦ / Add Touchpoint / Other Actions ∨),
  Tab Bar, then Record Sidebar (`.vp-record-sidebar`) + tab content.
  While editing, `+ New` is replaced by Save (left) + Cancel (right).
- **Shell:** global banner + collapsed left nav rail + Right Utility Rail
  (`.vp-utility-rail`: Dela D+, pin, person, notifications, help) are on every
  screen. They're boilerplate — include them, don't make them the focus.
- **Grids:** related-record lists use Named Grid Sections (`.vp-grid-section`)
  with `+ Add [item]` LEFT next to the title and icon toolbar right; empty
  grids say "There are no records to show in this grid." (omit the filter icon
  when empty).
- **Dialogs:** form dialogs have title bar + ×; confirmation dialogs
  (`.vp-dialog--confirm`) have no title bar — bold title in the body.
- **Popovers:** linked record names and ⓘ icons open Info Bubbles
  (`.vp-bubble`), not tooltips.
- **Pinned menu:** the hamburger pins open a 250px nav panel (`.vp-nav-flyout`,
  "Unpin Menu" header, current module expanded with indented sub-items,
  selected item = blue pill). Content section headers put the rule AFTER the
  label (`.vp-section-title`). Sidebars show status as a colored square + text
  (`.vp-status-square`), stages as colored text (`.vp-stage-text--won`) — not
  pills. Record headers can carry a `✦ Insights Available` chip
  (`.vp-chip--insights`).
- There is no breadcrumb pattern in VP — don't add one to hub pages.
- Full pattern-to-class mapping: table at the top of `docs/COMPONENTS.md`.

## Key visual facts (measured from the live product — see docs/TUNING.md)

- Primary blue `#4C92D9` (`--color-button-bg-primary`), secondary buttons are white
  with `#3A70A6` text/border. Action buttons: 32px tall, 12px font, 0 10px padding,
  8px radius. The hub-toolbar `+ New` button is larger (14px font, 10px/14px padding).
- Dela Actions button: gradient `119deg #8A33C2 → #423FE2`, white text (`.vp-btn--dela`).
- Tabs: 24px tall, 12px font, 0 8px padding, 4px radius; selected = solid blue pill.
- Record name: 22px/500 `#555`; last-modified line 13px/500; field labels and grid
  headers 13px/600 `#4d4d4d`.
- Inputs are 28px tall, 4px radius, `#b4b4b4` border. Edited fields get a blue tint
  (`.is-edited`), invalid a yellow tint (`.is-invalid`).
- Top banner is 44px (`--banner-height`); left nav is a 52px white icon rail
  (`--nav-menu-width`) with a 12px-radius selected state in primary blue.
- Hub content sits in a white record card (`.vp-record-card`) with a blue top line
  (`--color-application-top-line`) and rounded top corners, inset ~8px from the edges.
- Record sidebar: 200px wide; 150×150 image with 20px radius (`--border-radius-hub-image`).
- Grid: `#f3f3f3` header, `#D1D1D1` cell borders, hover `#f0ffff`, selected `#D9EBF2`;
  empty grids: 14px normal (not italic) `#a7a7a7`.
- Dialogs: 4px radius (NOT the 16px token), gray 40px title bar (#e5e5e5) with
  18px/600 title, shadow 0 4px 8px; footer pair anchored bottom-right with the
  primary button left of Cancel. Required-empty fields show the yellow tint.
- Page background `#F9FAFC`; non-hub content sits in white panels (`.vp-panel`).
- Status colors: positive `#5cae30`, negative `#c41f1f`, info `#4287ed`,
  attention `#fcaa32`, neutral `#c4c4c4` (`--vp-status-color-*`).

## Interactivity available (js/vp-kit.js)

- Tabs: `data-vp-tab="panelId"` on `.vp-tab` toggles panels by id.
- Dialogs: `data-vp-open="dialogId"` / `data-vp-close`; Escape and overlay click close.
- Nav flyout: `data-vp-flyout="flyoutId"` toggles `.is-open`.
- Theme: `data-vp-theme-toggle`.
For anything beyond this, write minimal vanilla JS in the page.

## Regenerating tokens from a fresh product build

`python3 scripts/extract-tokens.py path/to/styles<date>.min.css`
(the big CSS file saved from Chrome DevTools while running Vantagepoint).
