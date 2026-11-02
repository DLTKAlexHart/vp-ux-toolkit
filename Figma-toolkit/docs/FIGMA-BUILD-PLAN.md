# Figma build plan: finish the VP Toolkit library

**Status (2026-11-02):** Phases 1 to 8 built except the items below; Phase 9 (publish, test import) is pending and manual.
Not done: list-view and settings-form templates; browser-render comparison; contrast check; Code Connect; info bubble tail; notification dots; Quick find / Hub record wrapper as its own component. Effect styles hold Light values only (Figma cannot switch them by mode).

Goal: a published Figma library the team can enable in any file and use for foundations (variables, text, effect styles) and every kit component, matching the browser render. Recipe and gotchas: skill `vp-figma-library` (`.claude/skills/vp-figma-library/SKILL.md`). This plan is the work order; the skill is the how.

File: `QLYlJbr59j7i5becv6k2pq` (Deltek, Inc. plan). Already built: Cover, Getting Started, Typography (23 type variables, 37 text styles), 5 doc-only color variables.

## Rules for every phase

- Follow the VP conventions in the kit's `CLAUDE.md` (button pairs primary left and Cancel right, click-to-edit fields, no breadcrumbs, info bubbles not tooltips). Use the real class names from that file and `docs/COMPONENTS.md`; do not invent patterns.

- CSS is the source of truth. Record the selector beside every value.
- Variables before styles, styles before components. No hardcoded fill, stroke, radius, gap, padding or effect in a component.
- `use_figma` calls run one at a time. Run the skill's audit after every page and fix to zero before moving on.
- Update "Current state" in the skill and the Getting Started page at the end of each phase.
- Take a screenshot of each page and compare it to the browser render of the same thing (`components.html`). State what was not compared.
- Publishing is manual and last (Phase 9). Nothing before that is importable.

## Decisions to settle before Phase 1

| Question | Recommendation |
|---|---|
| Color token depth: kit has about 686 `--color-*` properties in the light block and a `[data-theme=dark]` block. Import all, or only what components use? | Import only tokens that a built component references, plus the `base`, `status`, `button`, `field`, `grid`, `tab`, `dialog`, `nav`, `action` groups. Add others on demand. 686 variables make the picker unusable. |
| Primitive layer: the kit has none (every token is a literal hex). | Do not invent primitives. Keep one `Color` collection with Light and Dark modes holding literal values, named to mirror the CSS (`color/button/bg-primary` is `var(--color-button-bg-primary)`). Flag this to the user as a deliberate departure from the usual primitives-plus-semantic pattern. |
| Dark mode | Build Light and Dark modes from the start; a missing Dark value is a bug. |
| Names | Variable names mirror CSS property names with `/` for `-` groups, so code and Figma round-trip. |
| PDM on cover (currently "Dawn") | Ask the user. |

## Phase 1: Color foundation

1. Extract every `--color-*` from `css/vp-tokens.css` (read in chunks; 1,380 lines) with its light and `:root[data-theme="dark"]` value. Write a JSON ledger to `/tmp` (name, light, dark, group, referenced-by).
2. Decide the used set: grep the component CSS for `var(--color-…)` and keep those plus the groups listed above.
3. Replace the 5 doc-only variables: rename in place if the values equal kit tokens (`color/base/bg`, etc.) so existing bindings survive; otherwise keep them under a `doc/` group.
4. Create the `Color` collection modes Light and Dark. Scopes by role: backgrounds `FRAME_FILL, SHAPE_FILL`; text and icon `TEXT_FILL`; borders `STROKE_COLOR`. WEB syntax `var(--color-…)`.
5. Specimen page `Colors`: one section per group, swatch, name, light hex, dark hex, CSS name. Add a second frame with the Dark mode set explicitly, so both modes are visible.
6. Exit: counts match the ledger; audit zero; screenshot of both modes.

## Phase 2: Effects, spacing, radius

1. Shadows: the 12 `--shadow-*` tokens become effect styles `Shadow/dialog`, `Shadow/popup`, `Shadow/focus`, and so on. Parse multi-layer values into multiple effects. Effect styles cannot bind to variables for color; note the dark-mode values in the description.
2. Radius collection `Radius` (button 8, dialog 4, others from `--border-radius-*` and literal values in the components). Scope `CORNER_RADIUS`.
3. Spacing collection `Spacing`: extract the recurring literal paddings and gaps from the component CSS (script: extend `extract-font-rules.py` into `extract-metrics.py` for `padding`, `margin`, `gap`, `height`, `width`, `border-radius`). Only values used by 2+ components become variables; one-offs stay literal and are noted in the component description. Scopes `GAP`, `WIDTH_HEIGHT` as appropriate.
4. Specimen pages `Effects` and `Spacing & Radius`.
5. Exit: every shadow in the CSS has a style; audit zero.

## Phase 3: Icons

1. Source: `icons/_sprite.html` (27 symbols). Import each as a vector component `Icon/<name>` on an `Icons` page at 16px, fill bound to a text-color variable so recoloring works.
2. Publish a single `Icon` component set (name = variant) or individual components; prefer individual components so INSTANCE_SWAP lists them.
3. Check the `--harmony-icon-*` font codepoints in the tokens file: record which icons exist only in the font, and ask the user before substituting.
4. Exit: all 27 present, sized, named, with description of the sprite id.

## Phase 4: Atoms (one page each)

Source: the pattern-to-class table at the top of `docs/COMPONENTS.md`, `docs/COMPONENTS.md`, `docs/TUNING.md`, `components.html`, CSS.

| Order | Component | Notes |
|---|---|---|
| 1 | Button | `.vp-btn` family: primary, secondary, destructive, small, mini, add, and `.vp-btn--dela` (gradient 119deg #8A33C2 to #423FE2, white text; a gradient fill bound to color variables). States default, hover, active, disabled, focus. Action buttons 32px tall, 12px font, 0 10px padding, 8px radius; the hub-toolbar `+ New` is larger (14px, 10px/14px padding), so make it a size variant. Icon slot via INSTANCE_SWAP, text property for label. |
| 2 | Checkbox, Radio, Toggle | `.vp-check`, `.vp-toggle`. Checked, unchecked, disabled. |
| 3 | Status, Chip | `.vp-status-square` (colored square plus text, the sidebar pattern), `.vp-stage-text--won` (colored text, not a pill), `.vp-status` badges, `.vp-chip` including `.vp-chip--insights`. Status colors `--vp-status-color-*`. |
| 4 | Input (form field) | `.vp-field`: text, select, textarea. States default, focus, error, disabled. 28px tall. |
| 5 | Display field | `.vp-dfield` click-to-edit resting state, label plus value. |
| 6 | Message | `.vp-message` info, warning, error, success. |
| 7 | Info bubble | `.vp-bubble`, including the generated variant (upright; Lexend has no italic). |

Per component: variant matrix at or under 30 (split otherwise), `combineAsVariants`, grid-positioned, component properties linked, description with CSS selector and usage, hardcoded value check.

## Phase 5: Molecules

1. Tab and tab bar (`.vp-tab`, `.vp-tabs`): 24px tall, 12px font, 0 8px padding, 4px radius; selected is a solid blue pill.
2. Search, Filter popup (`.vp-filter`), Menu (`.vp-menu`, dropdown items). No breadcrumb: VP has no breadcrumb pattern, so do not build one.
3. Action bar (`.vp-action`), KV pair (`.vp-kv`), Panel (`.vp-panel`), Section title (`.vp-section-title`, rule after the label), Banner (`.vp-banner`, 44px).
4. Info bubble lives in Phase 4; Dialog (`.vp-dialog`, `.vp-overlay`) here: 4px radius, gray 40px title bar #e5e5e5 with 18px/600 title, shadow 0 4px 8px, primary button left and Cancel right. Two variants: form dialog (title bar and x) and confirmation dialog `.vp-dialog--confirm` (no title bar, bold title in the body).

Slots: use component properties or nested instances of an empty frame; document the intended contents on the page.

## Phase 6: Data grid

`.vp-grid`: header cell (#f3f3f3), data cell (text, number, link, status, checkbox; borders #D1D1D1), row (default, hover #f0ffff, selected #D9EBF2), named grid section `.vp-grid-section` (`+ Add [item]` left next to the title, icon toolbar right), and the empty state ("There are no records to show in this grid.", 14px normal #a7a7a7, no filter icon). Build cell and row as components, then a sample grid assembled from instances. This is the largest matrix; split cell type and row state into separate components.

## Phase 7: Shell and patterns

Shell: global banner, 52px collapsed nav rail (`--nav-menu-width`, 12px-radius selected state), pinned nav flyout `.vp-nav-flyout` (250px, "Unpin Menu" header, selected item is a blue pill), right utility rail `.vp-utility-rail`. Hub: toolbar `.vp-hub-toolbar` (module label, Find, Filter, pager, `+ New`, replaced by Save left and Cancel right while editing), record header `.vp-record-header` (22px/500 #555 name, last-modified line, actions right), record sidebar `.vp-record-sidebar` (200px, 150x150 image with 20px radius), record card `.vp-record-card` (white, blue top line, rounded top corners). Page background #F9FAFC. Build the hub as one composed `Hub/Record` frame from instances. Then the three templates (`templates/hub-record.html`, `list-view.html`, `settings-form.html`) as example screens on a `Templates` page, assembled only from library instances. If a template needs a detached or hardcoded element, that component is missing: go back and build it.

## Phase 8: Quality gate

Run all of these and fix to zero:

1. Skill audit: text styles with no description; variables with `ALL_SCOPES` or no WEB syntax; text nodes with no style; unbound fills and strokes; unbound radii, gaps and paddings in components; unnamed or duplicate nodes.
2. Every component has a description with CSS selector, and the component name matches `Group/Name` or `Name` with `Property=Value` variants.
3. Dark mode: switch every specimen and component page to Dark with `setExplicitVariableModeForCollection` and screenshot; no unreadable text, no hardcoded white.
4. Browser parity: render `components.html` in headless Chrome and compare against the Figma component frames for height, width, wrapping and color. Log mismatches in the skill.
5. Accessibility: contrast of text-on-fill pairs in both modes; minimum target sizes noted (the kit's 28px inputs are a product decision, not changed).
6. Page structure: Cover, Getting Started, foundations pages, a `---` separator, one page per component, a `---` separator, Templates. Getting Started lists pages, how to enable the library, and how to report issues.
7. Optional: Code Connect mapping for each component to the kit's HTML class (`.figma.ts`). Defer unless the team wants dev-mode snippets.

## Phase 9: Publish and verify import (user does the click)

1. User: Assets panel, Libraries, Publish, with a description and the current plan. Choose to publish styles, components and variables.
2. Make the library available to the team: set it as a default library for the Deltek drafts or the relevant team and confirm view access for the audience.
3. Test import: create a scratch file, enable the library, and check that all of these work: apply a text style, apply a color variable in both modes, apply an effect style, insert a Button and change its variant, swap an icon, flip the file to Dark mode.
4. Test an update: change one value in the library, publish, confirm the scratch file shows "update available" and takes the change.
5. Record the library key and publish date in the skill and the memory entry.

## Ongoing maintenance

- When kit CSS changes, rerun the extract scripts, diff against the Figma values, update variables first (components follow), publish with a change note.
- Do not detach instances in templates; fix the library instead.
- Never rename a published variable, style or component without a plan: renames break overrides in consumer files. Add the new one, move usages, then delete the old.
- Version note on the Getting Started page after each publish.

## Order and effort

Phases 1 to 3 are foundations and should finish before any component. Phases 4 to 7 are one component page per session step; expect 4 to 8 `use_figma` calls per component. The largest risks are the color token volume (Phase 1), the grid matrix (Phase 6) and glyph-metric differences between Figma's static Lexend and the kit's variable font, which only the Phase 8 browser comparison will expose.

## Parity audit (2026-11-02): kit versus Figma, class by class

Method: browser measurements from headless Chrome rendering the kit's own CSS with its variable Lexend (`/tmp/vpcmp`, rebuilt per run), diffed against Figma node sizes read through `use_figma`. Text metrics: a 590-character string per text style, 33 styles, worst difference 0.1%.

Gaps found and the fix for each:

| Kit class | Gap in Figma | Fix |
|---|---|---|
| `.vp-btn` with icons | no leading or trailing icon slots; Add 36 high vs 38, Dela 60 wide vs 129 | done: boolean and instance-swap properties |
| `.vp-banner` | Figma had bell and help; kit has menu button, firm, Period Ending, settings button, avatar | rebuild |
| `.vp-banner__*` | `.vp-banner__period`, `.vp-banner__icon-btn` hover | rebuild |
| `.vp-badge-dot` | not drawn | add |
| `.vp-nav__item`, `.vp-nav__divider`, `.vp-nav__bottom` | rail items had no selected/hover variants, no bottom group | rebuild as a set |
| `.vp-nav-flyout__*` | only one flyout state; no hover | add |
| `.vp-utility-rail__item` | no hover, no badge dot | add |
| `.vp-field` | no select, textarea, date, required asterisk, help text | add kinds and props |
| `.vp-page-header`, `.vp-breadcrumb` | missing (settings template) | add. Note: CLAUDE.md says no breadcrumb on hub pages, and the settings template uses one, so it is included for that template only |
| `.vp-tabs__chevron`, `.vp-tabs` | no tab bar with overflow chevrons | add |
| `.vp-record-sidebar__collapse` | not drawn | add |
| `.vp-collapse-toggle` | collapsible section chevron is an icon, kit uses a text glyph | keep icon, note |
| `.vp-dfield__note` | missing | add to display field |
| `.vp-dialog__more-link` | missing | add |
| `.vp-divider` | missing | add |
| `.vp-grid th .sort`, `.row-menu`, `.drag-handle`, `tfoot td` | no sort arrow, no row menu, no footer cell | add |
| `.vp-bubble__close`, `__footer`, body text | bubble was title and meta only | rebuild |
| `.vp-bubble--below` | missing | add variant |
| `.vp-grid-toolbar`, `__count` | missing | add |
| `.vp-stage-text--won/--lost` | won only as sidebar badge | add stage text |
| `.vp-status-square--*` | present | ok |
| `.vp-btn--text`, `--icon` | present | ok |
| `.vp-record-card` | only inside the template | add as component |
| `.vp-page-content` | n/a | layout only |
| Shadow effect styles | Light values only | bind effect colors to variables |


## Parity pass 2 (2026-11-02, later)

Added: list-view and settings-form templates, Settings sidenav, Nav rail (settings), List toolbar, Grid cell Link, Status and Action kinds, info bubble tail, Badge dot, and bound effect styles. Browser comparison done for both templates (list rows 37px, settings panels within 2px) and Dark screenshots for every component page. Still open: Code Connect, publishing, test import.
