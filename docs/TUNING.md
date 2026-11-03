# Tuning log

Measurements taken from the live product DOM (computed styles), not eyeballed.
Environment: vantagepointqe3 / Vantagepoint 2026.4, Firms hub record, 09/02/2026.

## Verified against live product (09/02/2026)

| Element | Measured | Kit |
|---|---|---|
| Global banner | 44px, white, text #646D82 | ✅ token |
| Left nav rail (collapsed) | 52px wide | ✅ token |
| Record action buttons (Dela/Other Actions) | h 32px, font 12px, pad 0 10px, radius 8px, border #3A70A6 | ✅ `.vp-btn` |
| Dela Actions | gradient `119deg #8A33C2 → #423FE2`, white text | ✅ `.vp-btn--dela` |
| `+ New [record]` (hub toolbar) | font 14px, pad 10px 14px (h ≈ 40–42) | ✅ `.vp-btn--add` |
| Tabs | h 24px, font 12px, pad 0 8px, radius 4px, **uppercase**, active bg #4C92D9 | ✅ `.vp-tab` (uppercase+letter-spacing added 09/10) |
| Record name | 22px / 500 / #555 | ✅ |
| Last-modified line | 13px / 500 / #555 | ✅ |
| Field group labels / grid headers | 13px / 600 / #4d4d4d | ✅ |
| Module label (hub toolbar) | 18px / 600 / #5A6170 | ✅ token |
| Find input | radius 4px, border #b4b4b4 | ✅ |
| Record sidebar | ~201px wide, white | ✅ 200px |
| Sidebar hub image | 150×150, radius 20px (`--border-radius-hub-image`) | ✅ |
| Record card | white, blue top line (`--color-application-top-line`), rounded top | ✅ `.vp-record-card` |
| Empty-grid text | 14px, normal (not italic), #a7a7a7 | ✅ |

## Verified 09/02/2026 — filter / saved-search popup (Employees hub, live DOM)

| Element | Measured | Kit |
|---|---|---|
| Popup | 615×442, white, r4, shadow 0 4px 8px rgba(0,0,0,.25) | ✅ `.vp-filter-popup` |
| Left panel | 250px wide, 1px separator | ✅ |
| "Saved Searches" header | 14px/600, pad 4px 18px | ✅ |
| Group headers (My/Shared Searches) | 13-14px/600, separator above | ✅ |
| Search items | 12px/400, 18px rows | ✅ |
| "+ New Search" | 12px link blue, pinned bottom | ✅ |
| Quick Find / Find-in-list inputs | 28px, r4 | ✅ |
| Record rows (right panel) | 38px min, name 14px #333, sub 12px gray, avatar 28px r4 | ✅ |
| Select All | primary pill 24px, 10px font, pad 4px 8px, r8, bottom-right | ✅ `.vp-btn--mini` |

## Verified 09/02/2026 — Projects record + pinned menu (live DOM)

| Element | Measured | Kit |
|---|---|---|
| Pinned nav menu | 250px, white, radius 0 12px 12px 0 | ✅ `.vp-nav-flyout` |
| Menu items | 30px tall, 12px font, #646D82; selected = blue 8px pill, white text | ✅ |
| "Unpin Menu" header | 12px, pin icon | ✅ `.vp-nav-flyout__pin` |
| Sub-items | indented under expanded module | ✅ `.vp-nav-flyout__sub` |
| "✦ Insights Available" chip | bg #D0DFFF, text #454BD4, 10px, r16, pad 2px 6px | ✅ `.vp-chip--insights` |
| Content section headers | 15px/400 #555; chevron before label; rule AFTER label fills width | ✅ `.vp-section-title` |
| Sidebar status | small colored square + plain text (not a pill) | ✅ `.vp-status-square` |
| Sidebar stage | colored text (e.g. "Won" green) | ✅ `.vp-stage-text--*` |
| Field value annotations | gray note after value ("Business Phone") | ✅ `.vp-dfield__note` |
| Tab bar overflow | ‹ › chevrons at both ends | ✅ `.vp-tabs__chevron` |
| Projects record header | number line under name; Insights chip on modified line | ✅ template |

Notes: in the product the pinned menu *replaces* the icon rail and shifts
content right; the kit overlays it (reads the same in static mockups). The
pinned menu also lists non-hub modules (Feature Flags, Invoice Data,
Materials…) that vary by role/config.

## Verified 09/02/2026 — modal dialog (Create Document, Employees hub, live DOM)

| Element | Measured | Kit |
|---|---|---|
| Dialog | radius **4px** (not the 16px token), border 1px #ccc, shadow 0 4px 8px rgba(0,0,0,.25), white | ✅ `.vp-dialog` |
| Title bar | 40px, bg #e5e5e5 (`--color-dialog-header-bg`), bottom border #dadada, pad 0 12px | ✅ |
| Title text | 18px/600 #555; ? and × icons right | ✅ |
| Footer buttons | pair anchored bottom-RIGHT; primary LEFT of Cancel; 32px/12px/r8 | ✅ |
| Disabled primary | bg #E0E4EB, text #BFC6D4 (matches tokens) | ✅ |
| Body | can contain a full Named Grid Section (title + icon toolbar + filter row) | ✅ compose |

Note: `--border-radius-dialog: 16px` exists in the tokens but shipped dialogs
render at 4px — ground truth is the built product.

Also verified on the Activities form dialog (same page): identical chrome
(gray title bar, 4px radius, ?/× right); Save (primary) left of Cancel,
right-anchored; required-but-empty fields use the yellow tint
(`--color-field-bg-invalid`, kit `.is-invalid`) with a red `*` on the label;
dialogs can contain their own tab bar, and a tab can carry a red required
marker (kit: `.vp-tab.is-invalid` or a `<span class="req">*</span>`).

## Verified 09/09/2026 — data grid (source: styles20260907204731.min.css)

Extracted from the production stylesheet directly (saved web page from Contacts hub list view).

| Element | Measured | Kit |
|---|---|---|
| Body row height | 33px (`height:33px` on `tbody>tr`) | ✅ `tbody tr { height: 33px }` |
| Body cell (TD) padding | `6px 6px` | ✅ updated from `7px 10px` |
| Body cell vertical-align | `top` | ✅ added |
| Header row height | 36px (`.hdrHeight { height: 36px }`) | ✅ `th { height: 36px }` |
| Header cell padding | 4px 6px (inner `.columnHdr`) | ✅ `th { padding: 0 6px }` |
| Column header text-transform | `uppercase` | ✅ added `text-transform: uppercase` |
| Header column separators | **none** — `th` has border-bottom only | ✅ removed `border-right` from `th` |
| Body cell borders | `border-width: 1px 0 0 1px` (top+left) | ✅ equivalent via bottom+right on each cell |
| Cell border color | `var(--color-grid-cell-border)` = `#D1D1D1` | ✅ |
| Hover bg | `var(--color-grid-bg-hover)` = `#f0ffff` | ✅ confirmed (odd cyan, but real) |
| Selected row bg | `var(--color-grid-bg-selected)` = `#D9EBF2` | ✅ |
| Grid body bg | `var(--color-grid-body-bg)` = `#F9F9F9` | ✅ updated `.vp-grid-wrap` |
| Filter row height | 34px | ✅ `.vp-filter-row th { height: 34px }` |
| Filter row input height | 29px | ✅ |
| Filter row border color | `var(--color-grid-border-filter-row)` = `#B0B0B0` | ✅ |

Notes: Filter row inputs in the product have an operator dropdown (33px wide) to the left of each input — the kit simplifies this to a plain text input, which is sufficient for mockup fidelity.

## Verified 09/10/2026 — hub record shell (source: styles20260909205338.min.css, Projects hub pages)

| Element | Measured | Kit |
|---|---|---|
| Module label (hub toolbar) | `var(--font-size-application-header)` = 1.8rem / 600 / `#5A6170` | ✅ updated from 1.5rem |
| Record name | `var(--color-title-header-text)` = `#555555` | ✅ switched from hardcoded `#555555` |
| Record ID line | 1.5rem / 500 / `var(--color-title-subheader-text)` = `#555555` | ✅ updated from 1.2rem / `--color-banner-text` |
| Record modified line | 1.3rem / 500 / `var(--color-title-secondary-subheader-text)` = `#555555` | ✅ switched from hardcoded `#555555` |
| Sidebar section padding | `10px 8px 0` | ✅ updated from `12px 14px 0` |
| Hub toolbar default state | shows `+ New [record]`, not Save/Cancel | ✅ template corrected |
| Banner bg (default light theme) | `#FFFFFF` (gradient is company-specific theming) | ✅ confirmed |

## Verified 2026-11-03 — collapsed left nav rail (computed styles, live Hubs page)

| Element | Measured | Kit |
|---|---|---|
| Nav container width | 52px | ✅ `--nav-menu-width` |
| Nav item width | 42px | ✅ updated from 40px |
| Nav item height | 32px | ✅ updated from 40px |
| Nav item border-radius | 8px | ✅ |
| Nav item selected bg | `rgb(76, 146, 217)` = `#4C92D9` | ✅ primary blue token |
| Nav item selected icon | `rgb(255, 255, 255)` white | ✅ |
| Nav icon type | Harmony font glyphs (`vp-hicon`) on **all pages**, not SVG sprite | ✅ updated all templates |
| Nav item order | Expand `»` · divider · Search · Favorites · My Stuff · Dashboards · Hubs · Resource Management · Proposals · Billing · Transaction Center · Cash Management · Accounting · Asset Management · General Ledger · Payroll · Purchasing · Utilities · Settings | ✅ updated all templates |
| Utility rail items | Dela (hicon glyph) · Insights (sparkles) · Notifications (bell) · Help | ✅ updated from D+ · Pin · People · Bell · Help |

Notes: The product nav uses a single DOM element that expands in place (class `closed`
toggled to open the pinned menu), shifting content right. The kit uses a separate
`vp-nav-flyout` overlay — reads identically in static mockups, but doesn't push content.

## Not yet verified

- Grid per-column filter row operator dropdown (33px wide, precedes each filter input) — kit uses plain input only
- List-view extras seen on real Employees list: Bulk Update button, View
  selector ("View: Default"), record-count + calendar icons in the filter
  pill group — not built
- Nav rail icon set and order (kit uses placeholder module icons)
- Dark theme side-by-side
- Save/Cancel inline pair size in hub toolbar (kit uses 32px action size;
  real Save may match the larger + New sizing)

## How to re-measure

Open the real product in Chrome, move the tab into the Claude tab group, and
ask Claude to read computed styles for the element in question — or use
DevTools: select element → Computed → height/padding/font-size.
