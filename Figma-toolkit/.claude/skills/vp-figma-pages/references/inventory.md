# VP Toolkit library inventory

Generated from the library file on 2026-11-02. Property types: T text, B boolean, I instance swap, V variant. Set properties with `setProperties`, matching names without the `#id` suffix. Keys are in `keys.md`. If the file changes, re-run the inventory script in `checks.md`.

## Controls

| Component (page) | Properties | Notes |
|---|---|---|
| Button (Button) | Label T, Leading icon B, Trailing icon B, Leading icon swap I, Trailing icon swap I, Type V [Default, Primary, Text, Small, Add, Dela, Icon, Mini], State V [Default, Hover, Disabled] | Default 32px, white with blue border. Primary is the main action. Add is the hub `+ New` (36-38px). Small is the section-header `+ Add item`. Icon is 32x32, swap the icon. Dela is the AI action. |
| Checkbox | Label T, Checked V [false, true] | |
| Radio | Label T, Selected V [false, true] | |
| Toggle | Label T, On V [false, true] | |
| Field | Label T, Value T, Required B, Help text B, Help T, Kind V [Text, Select, Textarea, Date], State V [Default, Hover, Focus, Edited, Invalid, Disabled] | 28px input, 220px default width, set FILL in a form grid. Invalid adds the error line. |
| Display field | Label T, Value T, Link B, Note B, Note text T, Empty V [false, true] | Click-to-edit resting state. Empty shows gray "None". |
| Search | Placeholder T | 28px, 200 wide. |
| Tab | Label T, State V [Default, Hover, Selected, Invalid] | 24px. Place in a horizontal auto-layout bar. |
| Menu, Menu item | Menu item: Label T, State V [Default, Hover] | Menu is a prebuilt popup. |

## Status and messages

| Component | Properties | Notes |
|---|---|---|
| Status | Kind V [Positive, Negative, Info, Attention, Neutral] | Pill. The label text is a child text node, edit it by finding the TEXT node named Label. |
| Status square | Label T, Kind V (same five) | Sidebar form: colored square plus text. |
| Stage text | Label T, Stage V [Won, Lost] | Colored text, not a pill. |
| Chip | Kind V [Approved, Rejected, Submitted, Insights] | Insights is the "Insights Available" chip. |
| Message | Text T, Kind V [Info, Attention, Negative, Positive] | Inline banner. |
| Info bubble | Title T, Mode V [Record, Informational, Record below] | Popover with a tail. Use instead of tooltips. |
| Badge dot | Context V [Banner, Utility rail] | Orange notification dot. |

## Data

| Component | Properties | Notes |
|---|---|---|
| Grid cell | Text T, Kind V [Header, Header sorted, Header checkbox, Text, Number, Link, Status, Checkbox, Row menu, Action, Footer text, Footer number], State V [Default, Hover, Selected] | Not every Kind has every State. Header and footer kinds are Default only. Status kind nests a Status instance: swap it to change the kind. |
| Grid section | Empty V [false, true] | Titled bordered grid with `+ Add item` left and an icon toolbar right. The Empty variant shows "There are no records to show in this grid." |
| Grid toolbar | none | Record count line. |
| Action bar | none | |
| KV pair | Label T, Value T, Kind V [Summary, Sidebar] | |

## Layout and structure

| Component | Properties | Notes |
|---|---|---|
| Panel | Title T | White panel, 8px radius, 16px padding. Content is a slot (added 2026-11-02): drop toggles, forms, grids or any content into it. |
| Section title | Title T, Collapsible V [false, true] | The rule goes after the label. |
| Divider | none | |
| Page header | none | Breadcrumb, title, Save and Cancel. Edit its text nodes by name: Parent, Current, Title. |
| Dialog | More link B, Kind V [Form, Confirm] | Form has a title bar and close. Confirm has none. |
| Filter popup | none | Two-panel saved-search popup. |

## Shell

| Component | Notes |
|---|---|
| Banner | 44px global banner. |
| Nav rail | Style V [Floating], Page V [Dashboards]. Floating dashboard card, 18 Harmony items. The Flat variants (Hub, Settings) were removed by the user; the four Templates were relinked to the Floating rails (4px/12px and 86px wrappers, body 801 tall, root 845). |
| Nav item | Icon I, Style V [Flat, Floating], State V [Default, Hover, Selected]. |
| Nav flyout, Flyout item | Flyout item: Label T, Show icon B, Show chevron B, Icon I, State V. |
| Utility rail, Utility item | Rail: Style V [Floating] (Flat removed).  Item: Icon I, Badge dot B, Style V, Type V [Icon, Dela], State V [Default, Hover, Active]. Active (Floating Dela) = pane open. |
| Hub toolbar | Editing V [false, true]. True swaps `+ New` for Save and Cancel. |
| List toolbar | List-page toolbar with filter, count and export. |
| Record header | Name, ID line, last-modified line, actions. |
| Record sidebar | 200px, image, key values, status. |
| Settings sidenav, Settings sidenav item | Item: Label T, State V [Default, Hover, Selected]. |

## Brand (page "Brand", from the product's own files)

| Component | Notes |
|---|---|
| Logo/Vantagepoint short | 229x36 disc, D and wordmark. Already inside Banner at 24px high. Fills bound, so it follows Dark. |
| Logo/Deltek Vantagepoint | 732x80 full lockup for login or splash screens. Fills bound. |
| Logo/Deltek | Style V [Blue, White]. Fixed brand colours (#1742F5, white), not recoloured. White on dark fills. |
| Logo/Dela | Four-part Dela mark from the Harmony font (dela-path1..4). Purple parts and text-colour parts. |
| Logo/Dela mono | Single colour (color/dela/text). Used in the Ask Dela utility item on the gradient. |

Never type "D" or "D+" as a logo. Use these.

## Icons (INSTANCE_SWAP, 16/20/24 per use)

search, bell, help, settings, menu, dashboard, folder, users, building, clock, dollar, chart, plus, chevron-down, chevron-right, dots, x, filter, columns, download, pencil, star, arrow-left, calendar, check, briefcase, pin.

## Styles

Text (apply with a style, never a font size): Heading/ Record name 22, Page title 18, Dialog title 18, H2 16, Section title 15, Panel title 15, Confirm title 15, H3 14, Grid section title 14, H4 13. Body/ Base 14, Value 14 medium, Small 13, Small medium 13, Caption 12, Status 12, Note 11, Caption italic 12. Label/ Field 13, Input 12, Section 13, Sidebar 12, Avatar 11, Micro 10, Key (uppercase) 11, Overline 12, Sort 10. Button/ Default 12, Small 13, Add 14, Mini 10. Tab/Default 12. Grid/ Cell 13, Header 13.
Effect: Shadow/ dialog, drop-target, focus, image, nav, nav-toolbar, popup, side-toolbar, tab, thumb, tile, tooltip.

## Variables (collection: names)

- **Color** (Light and Dark): `color/base/bg,text`, `color/page/bg,header-bg`, `color/grid/*`, `color/field/*`, `color/button/*`, `color/nav/*`, `color/app/*`, `color/tab/*`, `color/menu/*`, `color/dialog/*`, `color/status/*`, `color/message/*`, `color/chip/*`, `color/link/text`, `color/icon/*`, `color/divider/divider`, `color/application/top-line,header-bg,header-text`, `color/shadow/*`. Choose by role: a panel is `color/base/bg`, a page is `color/page/bg`, a link is `color/link/text`.
- **Spacing**: `space/2,4,6,7,8,10,12,14,16,18,20,24`. **Radius**: `radius/none,xs,sm,md,pill,lg,image,full`. **Size**: `size/banner-height,nav-rail-width,nav-flyout-width,input-height,button-height,tab-height,dialog-title-height,sidebar-width,hub-image,icon`.
- **Typography** (text styles bind these) and **Effect geometry** (shadow geometry, Light and Dark) are not bound by hand.

## Dashboard additions (2026-11-02)

Source: this repo (dashboard shell and widgets; see docs/COMPONENTS.md). Slots are marked S: drop content in them, never detach.

| Component (page) | Properties | Notes |
|---|---|---|
| Dash card (Action bar) | S Toolbar, S Body | 32px top corners, 6px blue top line, page-bg. Body gap 16. Sit it on a color/workbench/bg frame. |
| App header (Page header) | Title T, Analyze B, Edit Mode toggle B | 64px. Uses Button Dela and Toggle (Label position=Before). |
| Dash toolbar, Dash toolbar button (Action bar) | Button: Label T, Show icon B, Icon I, State V | Edit Mode only. |
| Dashpart widget (Dashboard widget) | Title T, Meta T, Show meta B, Dela tool B (default off), Refresh B, Options B, S Grid | Fill Grid with rows of Widget cell. Row heights: Header auto, Total 36, Text 42, Zebra 30. First column 250 wide, rest FILL. |
| Widget cell | Text T, Kind V [Header, Header number, Text, Number, Link, Total, Total number], State V [Default, Zebra, Cited] | Cited is the citation highlight. Number kinds right-align. |
| Widget tool | Tool V [Expand, Refresh, Options, Export, Filter, Dela] | Fixed per tool, not a swap. Dela is the circled 22px message-bubble button (Harmony/ask-dela) for the grid or widget toolbar. Circled tools (Export, Filter, Dela) use `color/action/grid-item-bg/border/text` (product tokens, Light/Dark). |
| Row tool | Tool V [Dela, Options] | 30x30 row-level tools beside a grid row: Ask Dela bubble (plain, no circle) and the Options kebab. Grid toolbar page. |
| KPI tile | Label T, Value T, Target T, Show target B, State V [Default, Miss] | Miss turns red and shows "Over target". |
| Banner | Style V [Standard, Dashboard], Firm T, Period T | Dashboard: 44px, wordmark logo, company-colour bar from color/banner/company-color. |
| Purpose panel | Mode V [Read, Edit] | Contains Suggest pill, Textarea fields. |
| Suggest pill, Dela draft card | Draft: State V [Loaded, Loading], Suggestion T, Basis T, Replace warning B | Dashed purple, never auto-fills. |
| Dela pane | Context T, S Thread | 502 wide, 78px right gutter for the utility rail. Composer inside. |
| Dela message | Role V [Dela, User], Message T, S Body (Dela) | Put Dela card in the Dela Body slot. |
| Dela card, Dela card heading, Dela card item, Dela citation, Dela pill, Dela tag | Card: Scope T, Basis T, S Body. Heading: Heading T, Count T, Show count B, Show tag B. Item: Text T, Show citation B | Slots cannot hold property bindings, so edit slot content directly. |
| Dela composer, Dela pane button | Composer: State V [Empty, Typing]. Button: Tone V [Header, Body], Icon I | Swapping a Dela pane button icon resets its colour: re-tint it. |

Icons added: 23 sprite (Icon/sparkle, layout, save, share, copy, trash, list, cloud-upload, cloud-download, expand, refresh, chevrons-right, user, network, flow, receipt, transfer, cash, calculator, book, cart, tools, sliders), 27 Harmony glyphs as Harmony/ (nav-* plus search, star, chevrons-right, bell, help, filter, export, expand, refresh, chevron-down, sparkles, ask-dela), and 10 Dela pane/ line icons. The dashboard's nav and widget tools use the Harmony set, not the Icon/ set.

New variables: color/workbench/bg, color/dashboard/*, color/status/{error,warning,success}-{bg,text}, color/grid/row-selected, color/badge/dot-alert, color/banner/company-color, color/dela/{accent,accent-bg,send-bg,send-hover-bg,pane-border,input-border,user-bubble,body-text,composer-bg}, color/shadow/black-18, radius/{tile,icon-bar,dash-card}, size/{dashpart-header-height,dash-toolbar-height,app-header-height,floating-item,floating-utility-width,floating-icon,dash-card-top-line,dela-pane-width,dela-rail-gutter}, space/34, font/size/24. New styles: Grid/Widget header, Grid/Widget total, Heading/KPI value, Dela/* (9), Shadow/floating. The Dela dark values are an invention (orange like the kit's dark Dela tab): the dashboard has no dark theme.
