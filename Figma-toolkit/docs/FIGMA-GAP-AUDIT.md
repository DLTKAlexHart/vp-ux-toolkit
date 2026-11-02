# billingDashboard2 vs VP Toolkit Figma library: gap audit

Audited 2026-11-02. Library: `QLYlJbr59j7i5becv6k2pq` (196 variables, 38 text styles, 12 effect styles, 27 icons, about 45 components). Dashboard: `index.html`, 12 custom elements, 10 stylesheets, 2 dashboards (Billing Review, My Projects).

## 0. Source drift (decide first)

The dashboard vendors its own `vp-ux-toolkit/` which is **newer** than the vp-kit the library was built from. Differences:
- `vp-components.css`: whole `.vp-widget` / `.vp-grid--fixed` / totals row / zebra block (+49 lines).
- `vp-shell.css`: floating nav and utility rail, wordmark banner, company gradient indicator, avatar image, `.vp-dash-card`, `.vp-app-header`, `.vp-app--workbench` (+88 lines).
- `vp-hicons.css` (new file) + `fonts/Harmony.woff2`, `Vantagepoint.woff2`: Harmony icon-font mappings.
- `icons/_sprite.html`: 50 symbols vs 27 (23 new).

Library only reflects the old kit. **Recommendation:** treat the dashboard's copy as the new source of truth, sync it back to vp-kit, then extend the library from it.

## 1. Variables missing from the library

| Token (kit) | Light / Dark | Used by |
|---|---|---|
| color-workbench-bg | #EDF0F6 / #15171A | page background behind floating nav and card |
| color-dashboard-dashpart-bg | #fff / #292929 | widget, KPI tile, toolbar, purpose panel |
| color-dashboard-dashpart-header-bg | #E6EEF2 / #101010 | widget and KPI title bar |
| color-dashboard-dashpart-header-text | #333 / #fff | same |
| color-dashboard-total-row-bg / -text | #E0EDCB / #103b56, #333 / #ccc | TOTALS row |
| color-status-error-text | #D83148 / #F46286 | KPI miss, draft warning |
| color-status-warning-bg | #FFB020 / #F9AF00 | stale-analysis border |
| color-dela-chat-*, color-dela-insight-* (13) | | Dela pane (the dashboard actually hardcodes its own, see 4) |
| border-radius-tile (8px), shadow-tile | | Radius has no tile token. `Shadow/tile` effect exists. |

Already present and reused: dela/gradient-start/end/text, application/top-line, application/header-text, banner/text, grid/*, nav/menu-*, field/*, button/*. The existing color/status/* set uses different names (positive, negative...), so error-text and warning-bg need adding.

## 2. Components missing

| # | Dashboard element | Library today | Needed |
|---|---|---|---|
| 1 | Floating nav (`vp-nav--floating`: 12px radius, shadow, 40px items, 24px icons, margin 12/4) | Nav rail 52px flat | New variant "Nav rail (floating)" + Nav item 40px |
| 2 | Floating utility rail (50px, radius 12/0/0/12, red 6px dot, Dela transparent, **Active gradient state**) | Utility rail, item has Default/Hover only | Variant + Active state for Dela |
| 3 | Banner, dashboard flavour: 200x34 wordmark, firm dot, period + chevron, 36px avatar, 6px company-colour gradient bar | Banner with 24px logo | Variant "Banner (dashboard)", company-colour indicator |
| 4 | App header (64px, title 18 semibold, Analyze button + Edit Mode toggle) | Page header is breadcrumb + title + Save/Cancel | New "App header" |
| 5 | Dash card (32px top radius, 6px blue top line) + workbench background | none | New "Dash card" shell |
| 6 | Dashpart widget (36px title bar, meta text, tool icons, circled 22px export/filter toolbar, fixed-column grid) | Grid section is a different pattern | New "Dashpart widget" |
| 7 | Widget grid specials: TOTALS row (green), numeric right-aligned header, twisty, zebra, cited-row highlight (#FFF3C4) | Grid cell has Header/Number/Footer kinds, no totals, no twisty | New Grid cell kinds Totals, Twisty; Cited state |
| 8 | KPI tile (label bar, 24px value, target line, **miss** state with red border and "Over target" flag) | none | New "KPI tile" (Default, Miss) |
| 9 | Dash toolbar (Edit Mode, 42px, 8 icon buttons + Dashpart Library link) | Action bar is generic | New "Dash toolbar" (or Action bar kind) |
| 10 | Purpose and guidance: read rows (110px label, "None" muted), edit field with **Suggest pill**, char counter, **draft card** (dashed purple, loading and loaded, warning line, Accept / Edit first) | Field Textarea, Display field | New "Suggest pill", "Dela draft card", counter help text, "Purpose panel" |
| 11 | Dela pane shell (gradient header, title, icon buttons, 360-440px wide, 62px rail gutter) | none | New "Dela pane" |
| 12 | Pane internals: Dela message row (avatar), user pill + initials avatar, context bar, history popover rows, composer (textarea, disclaimer, + and round send), busy dots, Stop pill, stale notice | none | New components for each |
| 13 | Dela analysis card: scope line, disclosure ("Based on..."), kv groups, H3 headings, list, count, "not in the data" tag, citation pill (numbered), action pills, chip row, footer with feedback | none | New "Dela card" kit (about 8 parts) |
| 14 | Prototype bar (dark band with dashboard picker) | none | **Local to the new file**, not a library component (prototype scaffolding) |
| 15 | Dashboard picker `<select>` | Field Select (28px) | Reuse; header picker is small variant, optional |

Reusable as is: Button (Default, Primary, Small, Dela, Icon), Toggle, Field Select/Textarea, Display field, Divider, Message, Logo/Vantagepoint short, Logo/Dela, Logo/Dela mono.

Check before building: Toggle label order (kit puts "Edit Mode:" before the track) and the Dela button icon.

## 3. Icons

- **Sprite icons missing (23 new):** sparkle, layout, save, share, copy, trash, list, cloud-upload, cloud-download, expand, refresh, chevrons-right, user, network, flow, receipt, transfer, cash, calculator, book, cart, tools, sliders. The dashboard uses 8 directly (sparkle, layout, save, share, copy, trash, list, cloud-upload) plus expand and refresh through Harmony. Import all 23 to stay on par with the kit.
- **Harmony font glyphs (the dashboard's real nav icons):** 15 nav (my-stuff, dashboard, hubs, resource-management, proposals, billing, transaction, cash-management, accounting, asset-management, general-ledger, payroll, purchasing, utilities, settings) plus search, star, chevrons-right, bell, help, filter, export, expand, refresh, chevron-down, sparkles, ask-dela. The library's nav icons are the 27 sprite line icons, which do not match what the dashboard renders. This is the largest visual gap. These need the same glyph-path import I did for Dela (Harmony.svg, flipped).
- **Dela pane line icons (inline SVG in dela-icons.js, 18px viewBox):** info, help, expand, collapse, history, newChat, more, plus, mic, send, plus the filled Dela glyph. Not in any kit set. Import as a "Dela/..." icon group.

## 4. Hardcoded values in the dashboard that are not tokens

These will become fixed fills in Figma unless the kit adds tokens: dela-pane colors (#5B3FD4, #EFEAFE, #2B3CE0, #D8DCE6, #C9CDD8, #E8E9EE, #1F2430), badge dot #d9261c (the kit uses orange), proto bar (#1a1f2e family), `#fff` composer and card backgrounds, `#FFF3C4` cited row, 👍 👎 emoji in feedback buttons. These do not follow Dark. Decision needed: add as `color/dela/*` tokens, or map to the closest existing token.

## 5. Other checks

- Font: dashboard loads Lexend (Google Fonts). I have not confirmed the library text styles use Lexend; verify before building.
- Banner logo is 24px high in the library but 34px in the dashboard (200x34 image). The same SVG, different size.
- Avatar image `assets/deltek.jpg` must be uploaded as an image fill.
- Widget data (3 grids x 7 columns, first column 250px) fits Grid cell once Totals/Twisty kinds exist.
- Every new variable needs a Dark value. The dashboard has no Dark toggle, but the kit does.

## 6. Proposed order

1. Sync the kit (section 0) and decide on section 4 tokens.
2. Add variables (section 1), then the 23 sprite icons and the Harmony glyphs.
3. Build components 1-13, Dela card kit last.
4. Publish, then build the dashboard file from the library (prototype bar and page-level frames local).
