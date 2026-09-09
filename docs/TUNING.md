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
| Tabs | h 24px, font 12px, pad 0 8px, radius 4px, active bg #4C92D9 | ✅ `.vp-tab` |
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

## Not yet verified

- Grid row height / cell padding (kit ≈ 30–34px; looked close on screenshot)
- Grid per-column filter row (inputs with ≈ operator buttons under the header
  row, seen in the Create Document dialog) — not built
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
