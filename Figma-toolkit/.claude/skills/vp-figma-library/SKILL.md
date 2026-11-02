---
name: vp-figma-library
description: Build or extend the VP Toolkit Figma component library so it matches the Vantagepoint HTML/CSS kit in this repo (css/, components.html, templates/) exactly. Use when asked to add a page to the VP Toolkit Figma file (typography, colors, spacing, shadows, or any component such as button, field, grid, dialog, tab), to sync Figma with changed kit CSS, or to audit the library for import-readiness. Requires the figma-use and figma-generate-library skills.
---

# VP Toolkit Figma library

Build Figma foundations and components from the kit's CSS so that a designer's Figma matches what the browser renders. The CSS is the source of truth. Never measure from screenshots or guess values.

**Figma file:** key `QLYlJbr59j7i5becv6k2pq`, Deltek, Inc. plan `organization::1303904496611212311`. URL `https://www.figma.com/design/QLYlJbr59j7i5becv6k2pq`.

## Before you start

1. Load `figma-generate-library` and `figma-use`. Pass `skillNames: "figma-use,figma-generate-library"` on every `use_figma` call.
2. Load the tool schemas in one call: `ToolSearch select:mcp__plugin_figma_figma__create_session,use_figma,get_screenshot,get_libraries,search_design_system`.
3. Call `create_session` with the file key, then pass its `sessionId` on every file call.
4. Run `use_figma` calls one at a time. Each call is atomic: on an error nothing was written, so fix the script and rerun.
5. Inspect first. Run a read-only `use_figma` listing pages, collections, variables and text styles, and match what exists. Never duplicate a name.

## Current state

Built and audited (2026-11-02): 34 pages (Cover, Getting Started, Typography, Colors, Effects, Spacing & Radius, Icons, a `---` separator, one page per component family including Badge dot, Divider, Page header, Grid toolbar and Stage text, a `---` separator, Templates).

- Collections: `Typography` (23), `Color` (about 117, Light and Dark; includes 14 shadow colours), `Effect geometry` (6, Light and Dark), `Spacing` (12, includes `space/7`), `Radius` (8), `Size` (10). 196 variables, all with scopes and WEB syntax.
- Effect styles are bound to variables, so shadows follow Dark mode when a frame sets explicit modes on both `Color` and `Effect geometry`.
- 38 text styles, 12 shadow effect styles, 27 icon components.
- Components: Button (8 types x 3 states), Checkbox, Radio, Toggle, Field (Text, Select, Textarea, Date x 6 states), Display field, Status, Status square, Chip, Message, Info bubble (with tail), Tab, Search, Menu, Dialog, Grid cell (Header, Header sorted, Header checkbox, Text, Number, Link, Status, Checkbox, Row menu, Action, Footer), Grid section, Grid toolbar, Action bar, KV pair, Panel, Section title, Banner, Nav item, Utility item, Utility Dela, Flyout item, Nav rail, Nav rail (settings), Nav flyout, Utility rail, Settings sidenav and item, Badge dot, Divider, Page header, Stage text, Hub toolbar, List toolbar, Record header, Record sidebar, Filter popup.
- Templates: Hub record (Light, Dark), List view, Settings form.
- Brand page (2026-11-02): Logo/Dela, Logo/Dela mono (Harmony glyphs dela-path1..4), Logo/Deltek (Blue, White), Logo/Vantagepoint short, Logo/Deltek Vantagepoint, all from the product's own files (archive/billingDashboard/public/*.svg and control-center/docs/brand/, both outside this repo, plus fonts/Harmony.woff2 here). Banner and Utility Dela now use them instead of typed "D" and "D+". The kit itself ships no image files, only the CSS "D" and "D+" text.
- Vector gotchas: `vectorPaths` accepts only absolute M, L, C, Q, Z and fonts are y-up, so convert and flip y; `createNodeFromSvg` ignores `transform` on paths; add large SVGs in chunks of about five paths per call.
- Verified: sizes against headless Chrome for components and for the list and settings templates; Dark mode screenshots of every component page.

Not done: Code Connect, a Roboto-versus-Lexend glyph pass beyond the earlier sample, PDM name on the cover (user said to ignore). The four `Specimen/Aa` text styles have no bound font size (56px has no kit token; they are documentation-only). Publishing and the test import are manual and still pending.

Update this section when you finish a page.

## Workflow for every page

Order is fixed: **extract, variables, styles or components, specimen page, screenshot, audit.** A component with a hardcoded value is a bug.

1. **Extract** values from the CSS (see below). Record the selector beside every value.
2. **Create variables** with specific scopes and web code syntax.
3. **Create styles or components** bound to those variables.
4. **Build the specimen page**, one row per style or component with spec and CSS selector.
5. **Screenshot and look.** `get_screenshot` returns a URL; `curl -f -L -o /tmp/figshot/x.png "<url>"`, then Read the PNG. Do not request base64.
6. **Audit** (below). Fix everything before moving on.
7. **Compare to the browser.** Copy the kit page to /tmp, swap the Google Fonts link for an `@font-face` pointing at `fonts/Lexend-Variable.woff2`, add a script that writes `getBoundingClientRect` values into a `<pre>`, run `Chrome --headless=new --allow-file-access-from-files --dump-dom`, and compare with Figma node sizes. This is the real test of "identical". Say so if you skip it.
8. **Dark check.** Clone the page's content into a temp frame, call `setExplicitVariableModeForCollection` for both `Color` and `Effect geometry`, screenshot, then delete the temp page.

## Extracting from the CSS

`css/vp-tokens.css` is 1,381 lines and over the Read cap; read it with `offset` and `limit`. It holds colors, shadows and icon codepoints, but almost no type: only `--font-base`, `--font-size-application-header` and `--line-height-application-header`. Real type values are literal rem values in the component CSS, so extract by rule:

```bash
python3 -I ../Figma-toolkit/.claude/skills/vp-figma-library/scripts/extract-font-rules.py css
```

Run it from the repo root with `python3 -I Figma-toolkit/.claude/skills/vp-figma-library/scripts/extract-font-rules.py css`. Also read `css/vp-base.css` for the `h1` to `h4` and body defaults. A rule that sets only `font-size` inherits weight 400 and line-height 1.4 from `body`; those are defaults, not omissions. Do not use `grep -A` with `^\.vp-x \{` patterns; the `{` is read as a repeat and fails.

### CSS to Figma conversions

| CSS | Figma |
|---|---|
| `html { font-size: 62.5% }` | 1rem = 10px, so `1.4rem` = 14px |
| unitless `line-height: 1.4` | `{unit:'PERCENT', value:140}` |
| `line-height: 24px` or a `2rem` token | `{unit:'PIXELS', value:24}` or `20` |
| `letter-spacing: 0.03em` | `{unit:'PERCENT', value:3}` |
| `text-transform: uppercase` | `textCase = 'UPPER'` |
| weights 400, 500, 600, 700 | Lexend `Regular`, `Medium`, `SemiBold`, `Bold` |

## Fonts

- Lexend is installed in Figma with static weights Thin to Black. Style names have no spaces: `{family:'Lexend', style:'SemiBold'}`. The cover template uses Roboto; load `Roboto` styles to edit it.
- Confirm with `figma.listAvailableFontsAsync()`, and `loadFontAsync` every style in every call that writes text.
- The kit ships a variable font (`control-center/fonts/Lexend-Variable.woff2`, outside this repo); Figma uses static cuts. Same design, but glyph metrics were never compared pixel by pixel.
- Lexend has no italic. `.vp-bubble__generated` is `font-style: italic` in CSS (the browser fakes a slant); `Body/Caption italic` is upright in Figma. Keep this note in its description.

## Variables

One collection per concern. Always set scopes (never `ALL_SCOPES`) and WEB code syntax.

```js
const col = figma.variables.createVariableCollection('Typography');
col.renameMode(col.modes[0].modeId, 'Value');
const v = figma.variables.createVariable('font/size/14', col, 'FLOAT');
v.setValueForMode(col.modes[0].modeId, 14);
v.scopes = ['FONT_SIZE'];
v.setVariableCodeSyntax('WEB', '1.4rem');
```

Naming and syntax rules:
- Slash-separated names. Where the CSS has a custom property, the WEB syntax is `var(--that-name)`, for example `color/button/bg-primary` maps to `var(--color-button-bg-primary)`. Use the literal value when there is no custom property.
- Scopes: backgrounds `FRAME_FILL, SHAPE_FILL`; text `TEXT_FILL`; borders `STROKE_COLOR`; gaps `GAP`; radii `CORNER_RADIUS`; type `FONT_FAMILY`, `FONT_WEIGHT`, `FONT_SIZE`, `LINE_HEIGHT`, `LETTER_SPACING`.
- Semantic color variables alias primitives; never duplicate a raw value. Light and Dark modes mirror the `[data-theme=dark]` block in `vp-tokens.css`.

Typography collection (built): `font/family/base` = Lexend; `font/weight/regular|medium|semibold|bold`; `font/size/10,11,12,13,14,15,16,18,22`; `font/line-height/none|tight|base|relaxed` (100/130/140/150 percent) and `header` (20px), `tab` (24px); `font/letter-spacing/none|key|overline` (0/3/4 percent). 16px exists only for the base `h2`; the 24px in `index.html` is the demo page and was left out on purpose.

## Text styles

Name `Group/Name` (Heading, Body, Label, Button, Tab, Grid; `Specimen/` for documentation-only). One style per distinct spec: merge selectors that share a spec, but keep two styles when line height differs even if size and weight match (`Heading/Page title` 18/600 lh 20px vs `Heading/Dialog title` 18/600 lh 1.4).

```js
const s = figma.createTextStyle();
s.name = 'Label/Field';
s.fontName = {family:'Lexend', style:'SemiBold'};
s.fontSize = 13;
s.lineHeight = {unit:'PERCENT', value:140};
s.letterSpacing = {unit:'PERCENT', value:0};
s.description = '13/600, lh 1.4. .vp-dfield__label';   // required: spec plus CSS selectors
s.setBoundVariable('fontFamily', familyVar);
s.setBoundVariable('fontSize', sizeVar);
s.setBoundVariable('fontWeight', weightVar);
```

Do not bind `lineHeight` or `letterSpacing`. `setBoundVariable` accepts them, but Figma converts the value to PIXELS (a 140 percent variable becomes 140px). Set exact values instead; the variables exist for reference and code syntax.

## Specimen pages

One auto-layout frame (1280 wide) per page: header, then a section per group. Each row is `[name / spec / CSS selectors] | [live sample]`.

- Build with `figma.createAutoLayout`. Append to the parent before setting `layoutSizing*` to `FILL`.
- Wrapping text needs `textAutoResize = 'HEIGHT'` plus an explicit width.
- Apply styles with `await text.setTextStyleIdAsync(style.id)`, then set `characters`. Bind fills and strokes to Color variables with `figma.variables.setBoundVariableForPaint(paint, 'color', variable)` (it returns a new paint; reassign it).
- Use the library's own styles for the doc's labels. Doc colors are `color/base/bg`, `color/base/text`, `color/banner/text`, `color/divider`, `color/status/border`.
- Cover uses the standard Deltek thumbnail template (instance `THUMBNAIL TEMPLATE`): set title and names by editing its text nodes. The PDM line still says "Dawn" from the template until the user says otherwise.
- Position new top-level nodes away from existing content. Return every created node ID.

## Components (not yet built)

One page per component family, in dependency order (atoms first). Source the markup and states from `components.html` and `docs/COMPONENTS.md`, and the measurements from `docs/TUNING.md` and the CSS. Bind every fill, stroke, radius, gap and text style to variables. Use `combineAsVariants` and position variants in a grid afterwards. Use INSTANCE_SWAP for icons (icons come from `icons/_sprite.html`). Keep a variant matrix at or under 30. VP conventions that affect layout: primary or destructive button on the left and Cancel on the right; dialogs are 4px radius (not the 16px token); inputs 28px tall; action buttons 32px tall with 8px radius.

## Import-readiness audit

Run as one read-only `use_figma` call after every page. All counts must be 0:

- text styles with an empty `description`
- variables with `ALL_SCOPES` or no `codeSyntax.WEB`
- text nodes with no `textStyleId`
- fills or strokes not bound to a variable
- text styles missing a bound `fontFamily`, `fontSize` or `fontWeight`
- duplicate or unnamed pages, styles and components

The library is only importable by other files after it is published (Assets, Libraries, Publish in the Figma UI). The API cannot do this. Leave it to the user, then test-import into a scratch file.

## What to tell the user when done

State what was built (counts), what the audit returned, and what was not verified: the browser comparison if skipped, any CSS value that cannot be reproduced in Figma (such as italic Lexend), and that publishing is still pending.

## Gotchas found while building components

- `resize(w, h)` on an auto-layout frame resets that axis to FIXED. Set `primaryAxisSizingMode` / `counterAxisSizingMode` to `AUTO` after the last `resize`, or the frame stays at the tiny initial size.
- `combineAsVariants` stacks every variant at (0,0). Lay them out and call `resizeWithoutConstraints` on the set. Set variant sizing before combining, not after.
- Figma strokes sit inside the frame and count toward hug size; CSS borders add to the box. A 1px border makes `padding 0 10px` come out 2px wider in Figma if the padding variable is the CSS value plus the border. Match the CSS by binding the CSS padding (not padding plus border) and checking the resulting height against the CSS.
- Cloning a variant loses its TEXT property link. Re-set `componentPropertyReferences = {characters: key}` on the clone, or instances show the default text.
- Instances cannot have children added or removed. To change an icon inside an instance, call `swapComponent` on the nested instance.
- A new auto-layout `figma.createFrame()` defaults to fixed 100x100 and a white fill. Set `layoutSizingVertical = 'HUG'` and clear `fills` when you do not want them.
- Descriptions are HTML-escaped on read-back when they contain double quotes or ampersands. Use single quotes and the word "and".
- A missing icon, style or variable in a script throws late; look everything up first and throw with the name.
- Missing CSS values still need a variable: add `space/N` for any recurring padding (7px menu items, 14px, 18px) so nothing is hardcoded.
- A list or table row of cell instances: set each cell `layoutSizingVertical = 'FILL'` so a taller cell (status pill) sets the row height for all. Row frames made with `createAutoLayout` carry a white fill; clear it.
- Rotating a node pivots on its top-left. For a rotated tail, set `relativeTransform` with the translation computed from the wanted centre.
- A cloned cell variant keeps its text link only after `componentPropertyReferences` is set again.

- Dashboard additions (2026-11-02): these became this repo's kit version (developed in billingDashboard2/vp-ux-toolkit; adds .vp-widget, floating nav and utility rail, app header, dash card, Harmony icon font). Library now has pages "Dashboard widget" and "Dela assist" plus Style variants merged into the existing Nav item, Nav rail, Utility item, Utility rail and Banner sets (no parallel '(floating)' copies: one component per concept), and App header, Dash toolbar and Dash card. Full list in vp-figma-pages/references/inventory.md. Gotchas learned: (1) Slots (component.createSlot) work and remove the need for detaching: Panel Content, Dashpart widget Grid, Dash card Toolbar/Body, Dela pane Thread, Dela message Body, Dela card Body. Slot children cannot carry componentPropertyReferences. (2) Cloning a variant drops text property references: rebind them. (3) Swapping an icon inside a variant resets nested colour overrides, so give icons their tone in the instance. (4) Bind gradient stops with boundVariables.color on each stop. (5) vectorPaths max is about 50KB per use_figma call, so quantize Harmony glyphs (round to integers, /4 for 256 grid) and import in batches of 3-6. (6) Harmony glyph vectors keep a default stroke from createVector: clear it. (7) Measure the real CSS in headless Chrome (--dump-dom with an injected script) instead of reading CSS.
- One source of truth (2026-11-02): never create 'X (variant)' copies. Add a Style or Page property to the existing set (cloning a variant into it with appendChild, then rebind property references), swapComponent every instance, then delete the copy. Cloning drops component property references and combineAsVariants preserves instances, so templates follow. Icon sets Icon/, Harmony/ and Dela pane/ are different artwork, not duplicates.
- **Publish and verify:** after republishing, test from a new Design file (see `vp-figma-pages` section 1): enable the library, import a few set keys, bind a variable, switch a frame to Dark. Consumers see the library as "vp-kit - Component Library". Merged or rebuilt sets get new keys, so update `vp-figma-pages/references/keys.md` and copy to `docs/`.
