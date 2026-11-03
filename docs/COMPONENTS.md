# Component reference

Copy-paste markup for every kit component. Live examples: `components.html`.
All classes are prefixed `vp-`. State classes: `is-selected`, `is-edited`,
`is-invalid`, `is-disabled`, `is-open`.

Kit classes map to the named patterns in the **Vantagepoint UI Patterns**
reference (v2.0, bundled with the `vantagepoint-mockup` skill):

| Pattern | Kit classes |
|---|---|
| 1 · Application Shell | `.vp-app`, `.vp-banner`, `.vp-nav`, `.vp-nav-flyout`, `.vp-utility-rail` |
| 1b · Dashboard Shell (floating) | `.vp-app--workbench`, `.vp-nav--floating`, `.vp-utility-rail--floating`, `.vp-dash-card`, `.vp-app-header`, `.vp-banner__indicator` |
| 1c · Dashboard Widget | `.vp-widget`, `.vp-widget__header`, `.vp-widget__meta`, `.vp-widget__tool`, `.vp-widget__toolbar`, `.vp-widget__body`, `.vp-widget--fill` |
| 2 · Hub Toolbar | `.vp-hub-toolbar` |
| 3 · Record Header | `.vp-record-header`, `.vp-btn--dela` |
| 4 · Tab Bar | `.vp-tabs`, `.vp-tab` |
| 5 · Record Detail Sidebar | `.vp-record-body`, `.vp-record-sidebar` |
| 6 · Two-Column Field Layout | `.vp-form-grid`, `.vp-dfield`, `.vp-section-title` |
| 7 · Named Grid Section | `.vp-grid-section`, `.vp-grid`, `.vp-grid-empty` |
| 8 · Data Grid (Full-Tab) | `.vp-grid-wrap` + `.vp-grid` |
| 9 · Info Bubble | `.vp-bubble` |
| 10 · Modal Dialog | `.vp-dialog`, `.vp-dialog--confirm` |
| 11 · Inline Dropdown / click-to-edit | `.vp-dfield` (rest) ↔ `.vp-field` (active) |

**Conventions (from the pattern reference):**
- In any button pair, **primary/destructive goes LEFT, Cancel goes RIGHT** —
  including dialog footers. This is the reverse of many apps.
- Fields at rest are **plain text** (click-to-edit); use `.vp-dfield`. Only the
  field(s) being actively edited render as bordered inputs (`.vp-field`).
- Empty field values display as gray "None" (`.vp-dfield__value.is-empty`).
- Empty grids show: *"There are no records to show in this grid."*
- Shell, hub toolbar, record header, tab bar, and sidebar are boilerplate on
  every hub page — include them, but only annotate what a mockup is about.

## Shell skeleton (hub page)

```html
<body class="vp-app">
  <header class="vp-banner">…logo · search · firm + period + avatar…</header>
  <div class="vp-app__body">
    <nav class="vp-nav">
      <!-- Nav icons are Harmony glyphs on ALL page types (vp-hicons.css required) -->
      <button class="vp-nav__item" data-vp-flyout="navFlyout" title="Expand"><i class="vp-hicon vp-hicon--chevrons-right"></i></button>
      <div class="vp-nav__divider"></div>
      <button class="vp-nav__item" title="Search"><i class="vp-hicon vp-hicon--search"></i></button>
      …one button per module in product order…
      <button class="vp-nav__item is-selected" title="Hubs"><i class="vp-hicon vp-hicon--nav-hubs"></i></button>
      …
    </nav>
    <div class="vp-nav-flyout" id="navFlyout">…</div>   <!-- optional -->
    <main class="vp-main">
      <div class="vp-hub-toolbar">…module · Find · Filter · pager · +New…</div>
      <div class="vp-record-card">  <!-- white card, blue top line -->
        <div class="vp-record-header">…name · id · last modified · actions…</div>
        <div class="vp-page-header" style="padding-top:0"><div class="vp-tabs">…</div></div>
        <div class="vp-record-body">
          <aside class="vp-record-sidebar">…image + key fields…</aside>
          <div class="vp-page-content" style="flex:1">…tab content…</div>
        </div>
      </div>
    </main>
    <!-- Utility rail: Dela · Insights · Notifications · Help (no pin/people buttons) -->
    <aside class="vp-utility-rail">…Dela hicon · sparkles · bell · help…</aside>
  </div>
</body>
```

See `templates/hub-record.html` for the complete markup. Non-hub pages
(settings, dashboards) keep banner + nav + utility rail and use
`.vp-page-header` / `.vp-page-content` directly.

## Dashboard shell (floating nav and utility rail)

Variant of the shell for dashboard pages. The nav and utility rail become
rounded cards floating on a bluish-gray workbench surface; the page content
sits in a rounded `.vp-dash-card` with a 6px primary top line. Full page:
`templates/dashboard-shell.html`.

```html
<body class="vp-app vp-app--workbench">
  <header class="vp-banner" style="--company-color:#008b8b">
    …product · <div class="vp-spacer"></div> · actions…
    <div class="vp-banner__indicator"></div>   <!-- gradient company bar -->
  </header>
  <div class="vp-app__body">
    <nav class="vp-nav vp-nav--floating">
      <button class="vp-nav__item" title="Expand"><i class="vp-hicon vp-hicon--chevrons-right"></i></button>
      <div class="vp-nav__divider"></div>
      <button class="vp-nav__item" title="Search"><i class="vp-hicon vp-hicon--search"></i></button>
      <button class="vp-nav__item is-selected" title="Dashboards"><i class="vp-hicon vp-hicon--nav-dashboard"></i></button>
      …one button per module…
    </nav>
    <main class="vp-main">
      <div class="vp-app-header"><h1 class="vp-app-header__title">…</h1><div class="vp-app-header__actions">…</div></div>
      <div class="vp-dash-card"><div class="vp-dash-card__body">…widgets…</div></div>
    </main>
    <aside class="vp-utility-rail vp-utility-rail--floating">
      <button class="vp-utility-rail__item vp-utility-rail__item--dela" title="Ask Dela">
        <i class="vp-hicon vp-dela">
          <span class="vp-hicon vp-hicon--dela-1"></span><span class="vp-hicon vp-hicon--dela-2"></span>
          <span class="vp-hicon vp-hicon--dela-3"></span><span class="vp-hicon vp-hicon--dela-4"></span>
        </i>
      </button>
      <button class="vp-utility-rail__item" title="Insights"><i class="vp-hicon vp-hicon--sparkles"></i></button>
      <button class="vp-utility-rail__item" title="Notifications"><i class="vp-hicon vp-hicon--bell"></i><span class="vp-badge-dot"></span></button>
      <button class="vp-utility-rail__item" title="Help"><i class="vp-hicon vp-hicon--help"></i></button>
    </aside>
  </div>
</body>
```

- Needs `css/vp-hicons.css` (Harmony and Vantagepoint fonts in `fonts/`). Icons are
  font glyphs: `<i class="vp-hicon vp-hicon--NAME">`, add `vp-hicon--sm` for 16px.
  Nav glyph names: `nav-my-stuff`, `nav-dashboard`, `nav-hubs`,
  `nav-resource-management`, `nav-proposals`, `nav-billing`, `nav-transaction`,
  `nav-cash-management`, `nav-accounting`, `nav-asset-management`,
  `nav-general-ledger`, `nav-payroll`, `nav-purchasing`, `nav-utilities`,
  `nav-settings`; general: `search`, `star`, `chevrons-right`, `bell`, `help`,
  `filter`, `export`, `expand`, `refresh`, `sparkles`, `chevron-down`.
- Selected nav item: add `is-selected` (blue pill, white icon).
- The Dela button is a four-layer glyph (`.vp-dela`); add `is-active` to show
  the gradient tile while a Dela pane is open.
- Optional: `js/vp-nav.js` renders the nav and rail from an array instead:

```html
<div id="nav"></div>
<script src="js/vp-nav.js"></script>
<script>
  vpNav.render("#nav", [
    { title: "Search", icon: "search" },
    { divider: true },
    { title: "Dashboards", icon: "nav-dashboard" },
  ], { selected: "Dashboards", onSelect: (item) => console.log(item.title) });
  vpUtilityRail.render("#rail", { onDela: () => {} });
</script>
```

  The render targets sit inside `.vp-app__body` as the nav and rail's parents; give
  them `style="display:contents"` so the flex layout is unchanged.

## Dashboard widget

Dashpart widgets are the content cards placed inside `.vp-dash-card__body`. Each
has a gray 36px title bar, optional meta text and icon tools in the header,
an optional circled-icon toolbar row, and a body for content (usually a grid).
Requires `css/vp-hicons.css` for toolbar icons.

**Basic widget — header with meta and icon tools:**

```html
<div class="vp-widget">
  <div class="vp-widget__header">
    Aging Summary
    <span class="vp-widget__meta">Sep 2026</span>
    <button class="vp-widget__tool" title="Refresh"><i class="vp-hicon vp-hicon--refresh"></i></button>
    <button class="vp-widget__tool" title="More options"><i class="vp-hicon vp-hicon--chevron-down"></i></button>
  </div>
  <div class="vp-widget__body">
    <!-- content, KPI tiles, text, etc. -->
  </div>
</div>
```

- `.vp-widget__meta` pushes subsequent tools to the right edge (via `margin-left: auto`).
- `.vp-widget__tool` in the header is icon-only, no border — use for Refresh, More, ×.

**Widget with circled toolbar (below the header):**

```html
<div class="vp-widget">
  <div class="vp-widget__header">Revenue by Client</div>
  <div class="vp-widget__toolbar">
    <button class="vp-widget__tool" title="Filter"><i class="vp-hicon vp-hicon--filter"></i></button>
    <button class="vp-widget__tool" title="Export"><i class="vp-hicon vp-hicon--export"></i></button>
    <button class="vp-widget__tool" title="Expand"><i class="vp-hicon vp-hicon--expand"></i></button>
  </div>
  <div class="vp-widget__body">…</div>
</div>
```

- `.vp-widget__toolbar` tools have a circular border (22×22px) and are right-aligned.

**Widget with fixed-column grid and totals row:**

Grids inside widgets skip the outer `.vp-grid-wrap` border/radius — put
`.vp-grid-wrap` directly inside `.vp-widget`, not inside `.vp-widget__body`.
Add `vp-grid--fixed` for wrapping column headers and even cell padding.

```html
<div class="vp-widget">
  <div class="vp-widget__header">
    Aging Summary
    <span class="vp-widget__meta">Period: Sep 2026</span>
  </div>
  <div class="vp-grid-wrap">
    <table class="vp-grid vp-grid--fixed">
      <thead>
        <tr>
          <th>Client</th>
          <th class="num">0–30</th>
          <th class="num">31–60</th>
          <th class="num">Over 60</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="twisty"><svg class="vp-icon vp-icon--sm"><use href="#i-chevron-right"/></svg></span>
            Apex Design Group
          </td>
          <td class="num">$20,000</td>
          <td class="num">$18,400</td>
          <td class="num">$60,000</td>
        </tr>
        <tr>
          <td>Baari Sep17 Pro 1 Main</td>
          <td class="num">$12,000</td>
          <td class="num">$8,000</td>
          <td class="num">$50,000</td>
        </tr>
      </tbody>
      <tfoot>
        <tr class="is-totals">
          <td>Total</td>
          <td class="num">$32,000</td>
          <td class="num">$26,400</td>
          <td class="num">$110,000</td>
        </tr>
      </tfoot>
    </table>
  </div>
</div>
```

- `tr.is-totals` — totals row: distinct background, bold 600 text, 36px height. First cell auto-indented to align with tree content (uses `padding-left: 34px`).
- `.twisty` — inline expand/collapse icon for tree rows (use `vp-icon--sm` chevron).

**Zebra-striped grid (for dense lists):**

```html
<div class="vp-widget">
  <div class="vp-widget__header">Top Projects by Revenue</div>
  <div class="vp-grid-wrap">
    <table class="vp-grid vp-grid--fixed vp-grid--zebra">
      <thead><tr><th>Project</th><th class="num">Revenue</th></tr></thead>
      <tbody>
        <tr><td>Riverside Medical Center</td><td class="num">$2,450,000</td></tr>
        <tr><td>Harborfront Transit Hub</td><td class="num">$5,720,000</td></tr>
        <tr><td>Lakeview Elementary</td><td class="num">$1,180,000</td></tr>
      </tbody>
    </table>
  </div>
</div>
```

- `.vp-grid--zebra` — odd rows get `--color-grid-header-bg` background; row height 30px.
- Combine with `vp-grid--fixed` for consistent padding.

**Full-height widget:**

Add `.vp-widget--fill` to set a fixed 440px height (for tall chart or grid widgets).

```html
<div class="vp-widget vp-widget--fill">…</div>
```

## Pinned navigation menu

Toggled by the banner hamburger (`data-vp-flyout="navFlyout"`). 250px white
panel, rounded right corners; the current module expands inline with indented
sub-items; selected item = blue pill:

```html
<div class="vp-nav-flyout" id="navFlyout">
  <button class="vp-nav-flyout__pin" data-vp-flyout="navFlyout">
    <svg class="vp-icon vp-icon--sm"><use href="#i-pin"/></svg> Unpin Menu
  </button>
  <button class="vp-nav-flyout__item"><svg class="vp-icon vp-icon--sm"><use href="#i-search"/></svg> Search</button>
  <hr class="vp-divider">
  <button class="vp-nav-flyout__item"><svg class="vp-icon vp-icon--sm"><use href="#i-folder"/></svg> Projects <span class="chev">∨</span></button>
  <div class="vp-nav-flyout__sub">
    <button class="vp-nav-flyout__item is-selected">Project</button>
    <button class="vp-nav-flyout__item">Plan</button>
  </div>
</div>
```

Full example (Projects module expanded): `templates/hub-record.html`.

## Hub toolbar

```html
<div class="vp-hub-toolbar">
  <span class="vp-hub-toolbar__module">Projects</span>
  <div class="vp-search"><svg class="vp-icon vp-icon--sm"><use href="#i-search"/></svg><input placeholder="Find Projects"></div>
  <button class="vp-btn">Active <svg class="vp-icon vp-icon--sm"><use href="#i-chevron-down"/></svg></button>
  <div class="vp-hub-toolbar__pager"><button>‹</button> 4 of 128 <button>›</button></div>
  <div class="vp-spacer"></div>
  <button class="vp-btn vp-btn--add"><svg class="vp-icon vp-icon--sm"><use href="#i-plus"/></svg> New Project</button>
</div>
```

While a field is being edited, replace `+ New [record type]` with
`Save` (primary, left) + `Cancel` (outlined, right).

## Filter / saved-search popup

The Filter button opens the two-panel dropdown (measured: 615×442). Wrap the
button in `position:relative` and toggle with `data-vp-flyout`:

```html
<div style="position:relative">
  <button class="vp-btn" data-vp-flyout="filterPopup">
    <svg class="vp-icon vp-icon--sm"><use href="#i-filter"/></svg> Active
    <svg class="vp-icon vp-icon--sm"><use href="#i-chevron-down"/></svg>
  </button>
  <div class="vp-filter-popup" id="filterPopup" style="top:36px; left:0">
    <div class="vp-filter-popup__left">
      <div class="vp-filter-popup__header">Saved Searches</div>
      <div class="vp-search vp-filter-popup__quickfind"><input placeholder="Quick Find"></div>
      <button class="vp-filter-popup__item is-selected">Active</button>
      <button class="vp-filter-popup__item">All</button>
      <div class="vp-filter-popup__group">My Searches</div>
      <button class="vp-filter-popup__item">…</button>
      <div class="vp-filter-popup__new"><a>+ New Search</a></div>
    </div>
    <div class="vp-filter-popup__right">
      <div class="vp-search"><input placeholder="Find in list..."></div>
      <div class="vp-filter-popup__list">
        <label class="vp-filter-popup__row">
          <input type="checkbox"><span class="vp-filter-popup__avatar">RM</span>
          <span><span class="vp-filter-popup__row-name">Record Name - 0001</span><br>
          <span class="vp-filter-popup__row-sub">Organization</span></span>
        </label>
      </div>
      <div class="vp-filter-popup__footer">
        <button class="vp-btn vp-btn--primary vp-btn--mini">Select All</button>
      </div>
    </div>
  </div>
</div>
```

Live example: `templates/list-view.html` (click the filter button).

## Record header

```html
<div class="vp-record-header">
  <button class="vp-record-header__icon">…</button>  <!-- Projects only -->
  <div>
    <div class="vp-record-header__name">Record Name</div>
    <div class="vp-record-header__id">2024-0117.00 &gt; 001 Phase</div>
    <div class="vp-record-header__modified">Last modified 09/01/2026 4:12 PM by Maria Delgado</div>
  </div>
  <div class="vp-record-header__actions">
    <button class="vp-btn vp-btn--dela">✦ Dela Actions …</button>   <!-- Projects, Firms -->
    <button class="vp-btn">Add Touchpoint</button>
    <button class="vp-btn">Other Actions …</button>                  <!-- minimum -->
  </div>
</div>
```

## Record sidebar

```html
<div class="vp-record-body">
  <aside class="vp-record-sidebar">
    <button class="vp-record-sidebar__collapse">‹</button>
    <div class="vp-record-sidebar__image">…img/icon…<div class="vp-record-sidebar__stage">Active</div></div>
    <div class="vp-record-sidebar__section">
      <div class="vp-record-sidebar__section-title">Project Summary</div>
      <div class="vp-kv"><span class="vp-kv__label">Project Number</span><span class="vp-kv__value">2024-0117.00</span></div>
      …
    </div>
  </aside>
  <div class="vp-page-content" style="flex:1">…</div>
</div>
```

## Buttons

```html
<button class="vp-btn vp-btn--primary">Save</button>
<button class="vp-btn">Cancel</button>
<button class="vp-btn vp-btn--add"><svg class="vp-icon vp-icon--sm"><use href="#i-plus"/></svg> New</button>
<button class="vp-btn vp-btn--text">Text</button>
<button class="vp-btn vp-btn--icon"><svg class="vp-icon"><use href="#i-pencil"/></svg></button>
<button class="vp-btn vp-btn--sm">Small</button>
```

## Action bar

```html
<div class="vp-action-bar">
  <button class="vp-btn vp-btn--primary">Save</button>
  <button class="vp-btn">Cancel</button>
  <div class="vp-action-bar__sep"></div>
  <button class="vp-btn">Other Actions <svg class="vp-icon vp-icon--sm"><use href="#i-chevron-down"/></svg></button>
  <div class="vp-spacer"></div>
</div>
```

## Display field (click-to-edit resting state)

VP fields at rest are plain text — bold label, value below, no input chrome:

```html
<div class="vp-dfield">
  <div class="vp-dfield__label">Project Name</div>
  <div class="vp-dfield__value">Riverside Medical Center Expansion</div>
</div>
<div class="vp-dfield">
  <div class="vp-dfield__label">Estimated Completion</div>
  <div class="vp-dfield__value is-empty">None</div>       <!-- empty = gray "None" -->
</div>
```

Section headers within field layouts: `<div class="vp-section-title">Name and
Background</div>` (bold + full-width rule; add a `.vp-collapse-toggle` chevron
button inside for expandable sections).

## Form field (active editing state)

```html
<div class="vp-field">                      <!-- + is-edited / is-invalid / is-disabled -->
  <label class="vp-field__label">Name<span class="req">*</span></label>
  <input type="text">
  <span class="vp-field__error">Required field</span>   <!-- when invalid -->
  <span class="vp-field__help">Helper text</span>       <!-- optional -->
</div>
```

Lay fields out with `.vp-form-grid` (auto-fill 220px columns); span with
`.span-2` / `.span-full`. Works with `input`, `select`, `textarea`.

## Checkbox / radio / toggle

```html
<label class="vp-check"><input type="checkbox" checked> Label</label>
<label class="vp-toggle"><input type="checkbox" checked><span class="vp-toggle__track"></span> Label</label>
```

## Tabs

```html
<div class="vp-tabs">
  <button class="vp-tab is-selected" data-vp-tab="tabOne">One</button>
  <button class="vp-tab" data-vp-tab="tabTwo">Two</button>
</div>
<div id="tabOne">…</div>
<div id="tabTwo" hidden>…</div>
```

## Data grid

Column headers are **uppercase** (measured). No vertical separators between
header columns. Body rows are 33px tall; cells have 6px padding, vertical-align
top. Hover bg is `#f0ffff` (the real product color — cyan, but verified).

```html
<div class="vp-grid-wrap">
  <table class="vp-grid">
    <thead>
      <tr>
        <th>Col <span class="sort">▲</span></th><th>Amount</th>
      </tr>
      <!-- optional per-column filter row (34px, plain text inputs): -->
      <tr class="vp-filter-row">
        <th><input type="text" placeholder="Filter…"></th>
        <th><input type="text" placeholder="Filter…"></th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Row</td><td class="num">$1,000</td></tr>
      <tr class="is-selected"><td>Selected row</td><td class="num">$2,000</td></tr>
    </tbody>
    <tfoot><tr><td>Total</td><td class="num">$3,000</td></tr></tfoot>
  </table>
</div>
```

Optional toolbar above: `.vp-grid-toolbar` with `.vp-search` and
`.vp-grid-toolbar__count`.

## Status badges & chips

```html
<span class="vp-status vp-status--positive">Active</span>     <!-- pill: grid/list cells -->
<span class="vp-status-square vp-status-square--positive">Active</span>  <!-- square+text: sidebar fields -->
<span class="vp-kv__value vp-stage-text--won">Won</span>      <!-- stage as colored text -->
<span class="vp-chip vp-chip--approved">Approved</span>       <!-- approved/rejected/submitted -->
<span class="vp-chip--insights">✦ Insights Available</span>   <!-- record-header indicator -->
```

Sidebars use the square+text form, not the pill. Field-value annotations
(e.g. phone type) use `<span class="vp-dfield__note">Business Phone</span>`
after the value.

## Messages

```html
<div class="vp-message vp-message--info">…</div>   <!-- info/attention/negative/positive -->
```

## Dialog

**Button order: primary/destructive LEFT, Cancel RIGHT** (VP convention).

Form dialog:

```html
<button class="vp-btn" data-vp-open="myDialog">Open</button>
<div class="vp-overlay" hidden></div>
<div class="vp-dialog" id="myDialog" hidden>
  <div class="vp-dialog__header">
    <div class="vp-dialog__title">Title</div>
    <button class="vp-btn vp-btn--icon vp-dialog__close" data-vp-close><svg class="vp-icon"><use href="#i-x"/></svg></button>
  </div>
  <div class="vp-dialog__body">
    …form fields…
    <a class="vp-dialog__more-link">Add More [X] Information</a>  <!-- optional -->
  </div>
  <div class="vp-dialog__footer">
    <button class="vp-btn vp-btn--primary" data-vp-close>Save</button>
    <button class="vp-btn" data-vp-close>Cancel</button>
  </div>
</div>
```

Confirmation dialog (destructive actions — no title bar or ×):

```html
<div class="vp-dialog vp-dialog--confirm" id="deleteConfirm" hidden>
  <div class="vp-dialog__header"></div>
  <div class="vp-dialog__body">
    <div class="vp-dialog__confirm-title">Delete Firm</div>
    <p>This will delete the Firm Advanced Mechanical Technologies, Inc.</p>
  </div>
  <div class="vp-dialog__footer">
    <button class="vp-btn vp-btn--primary" data-vp-close>Delete</button>
    <button class="vp-btn" data-vp-close>Cancel</button>
  </div>
</div>
```

## Named grid section

```html
<div class="vp-grid-section">
  <div class="vp-grid-section__header">
    <span class="vp-grid-section__title">Key Team Members</span>
    <button class="vp-btn vp-btn--sm"><svg class="vp-icon vp-icon--sm"><use href="#i-plus"/></svg> Add Team Member</button>
    <div class="vp-grid-section__toolbar">
      <button class="vp-btn vp-btn--icon"><svg class="vp-icon vp-icon--sm"><use href="#i-settings"/></svg></button>
      <button class="vp-btn vp-btn--icon"><svg class="vp-icon vp-icon--sm"><use href="#i-download"/></svg></button>
      <button class="vp-btn vp-btn--icon"><svg class="vp-icon vp-icon--sm"><use href="#i-filter"/></svg></button>
    </div>
  </div>
  <div class="vp-grid-wrap"><table class="vp-grid">…</table></div>
  <!-- empty state instead of the table:
  <div class="vp-grid-empty">There are no records to show in this grid.</div> -->
</div>
```

`+ Add [item]` always sits left, next to the title. Omit the filter icon when
the grid is empty. Row-level `⋮` menu: `<button class="row-menu">⋮</button>` in
the last cell (visible on hover).

## Info bubble

```html
<div class="vp-bubble" style="top:…; left:…">   <!-- position near trigger -->
  <button class="vp-bubble__close">✕</button>
  <div class="vp-bubble__title">Maria Delgado</div>
  <div class="vp-bubble__meta">00123 · PROJECT MANAGER · HEALTHCARE STUDIO</div>
  <div>Work: (555) 210-3348</div>
  <div class="vp-bubble__footer">
    <span class="vp-status vp-status--positive">Active</span><span class="sep">|</span><a href="#">More…</a>
  </div>
</div>
```

Record-reference mode (above) for linked record names; informational mode for
`ⓘ` triggers uses `__title` + text + `.vp-bubble__generated` + footer links.
`--below` flips the tail to the bottom edge.

## Dropdown menu

```html
<div class="vp-menu">
  <button class="vp-menu__item">Edit</button>
  <hr class="vp-menu__sep">
  <button class="vp-menu__item">Delete</button>
</div>
```

Position it yourself (absolute, relative to its trigger).

## Panels & misc

```html
<div class="vp-panel">
  <div class="vp-panel__header"><div class="vp-panel__title">Section</div></div>
  …
</div>

<div class="vp-kv"><span class="vp-kv__label">Label</span><span class="vp-kv__value">Value</span></div>
<div class="vp-search"><svg class="vp-icon vp-icon--sm"><use href="#i-search"/></svg><input placeholder="Quick find"></div>
```

Utilities: `.vp-row`, `.vp-stack`, `.vp-spacer`, `.vp-divider`, `.vp-muted`,
`.vp-truncate`, `[hidden]`.

## Icons

`<svg class="vp-icon"><use href="#i-NAME"/></svg>` — sizes `vp-icon--sm` (16),
default (20), `vp-icon--lg` (24). Ids: search, bell, help, settings, menu,
dashboard, folder, users, building, clock, dollar, chart, plus, chevron-down,
chevron-right, dots, x, filter, columns, download, pencil, star, arrow-left,
calendar, check, briefcase. Add more in `icons/_sprite.html`, then run
`python3 scripts/build-icons.py`.
