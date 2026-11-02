---
name: vp-figma-pages
description: Build Figma pages, screens, dialogs and templates for Vantagepoint using the published "VP Toolkit – Component Library". Use when asked to design, mock up or lay out a Vantagepoint screen in Figma (hub record, list view, settings form, dialog, any new page), to import the VP library into a file, or to find which VP component, style or variable to use. Requires figma-use and figma-generate-design. For changing the library itself, use vp-figma-library instead.
---

# Building Vantagepoint pages in Figma

Compose screens from the VP Toolkit library: instances, styles and variables, never redrawn shapes or literal values. A page that looks right but is made of detached frames and hex colors is a failed page. This repo's HTML/CSS (`css/`, `components.html`, `templates/`) is the source of truth for how a screen should look; the library mirrors it.

**Library file:** "VP Toolkit – Component Library", key `QLYlJbr59j7i5becv6k2pq`, Deltek, Inc. plan `organization::1303904496611212311`.
**Name in Figma:** consumer files list the library as "vp-kit - Component Library" (the name it was published under), not "VP Toolkit – Component Library". Match on the library key or on this name. Verified end to end 2026-11-02: merged-set keys import, styles, variables and Dark mode work from a new Design file.
**This skill vs `vp-figma-library`:** that one edits the library. This one consumes it. Never edit a main component from a page file; change the library, publish, then accept the update.

## 1. Import the library (once per file)

Instances can only come from a published library. Publishing is manual and the API cannot do it.

1. Library file owner: Assets panel, Libraries, Publish. Republish after every library change.
2. Consumer file: Assets panel, Libraries, toggle on "VP Toolkit – Component Library". Accept updates when Figma prompts.
3. Confirm through MCP: `create_session` for the target file, then `get_libraries` with its `fileKey`. The VP library must appear under `libraries_added_to_file`. If it is only under `libraries_available_to_add`, stop and ask the user to enable it. `get_libraries` pages 20 at a time: follow `libraries_available_to_add_next_offset` until it is null before concluding the library is missing (it was on page 2). A key import error ("Component set … not found") with the library not added is the same signal. Do not rebuild components locally as a workaround.
4. Use the key tables in `references/keys.md` with `importComponentSetByKeyAsync`, `importComponentByKeyAsync` and `importStyleByKeyAsync`. If a key fails, the library was not republished or was renamed: run `search_design_system` (one intent per query, scoped with `includeLibraryKeys`) and update `references/keys.md`.
5. Never assume. Run `get_libraries` before `search_design_system`. An empty `getLocalVariableCollectionsAsync()` in a consumer file only means the variables are remote.

Mode behaviour: `Color` has Light and Dark modes and `Effect geometry` has Light and Dark. A frame follows the mode of its nearest ancestor that sets one, else Light. For a Dark screen set the mode on the screen's root frame, and on both collections, or shadows stay Light:

```js
root.setExplicitVariableModeForCollection(colorCollection, darkModeId);
root.setExplicitVariableModeForCollection(effectCollection, darkModeId);
```

Import the collections with `figma.teamLibrary.getAvailableLibraryVariableCollectionsAsync()`, then `importVariableByKeyAsync` on one variable per collection and read `variableCollectionId` to get the collection and its mode ids.

## 2. Rules for every page

1. **Instance first.** Every UI element that exists in the library is an instance. Check `references/inventory.md` before drawing anything. If it is missing, say so and ask; do not improvise a lookalike.
2. **No detaching.** Detach only when the user asks, and say what it costs (no more library updates). If an instance cannot do what is needed (reorder layers, add children), the fix is a new variant or property in the library.
3. **Change instances through their API.** Use `setProperties` for variants, text, booleans and icon swaps. Match property keys by name: `Object.keys(inst.componentProperties).find(k => k.split('#')[0] === 'Label')`. Never hardcode the `#id` suffix. Never set `characters` on a text node that a TEXT property controls.
4. **Overrides are limited to what Figma allows.** Fills, text and nested swaps survive library updates; layout and layer order do not. Do not resize an instance's internals to fake a variant.
5. **Styles and variables, not literals.** Text: `setTextStyleIdAsync` with a VP text style. Shadows: `effectStyleId` with a `Shadow/*` style. Fills, strokes, padding, gaps, radii: bound variables (`setBoundVariableForPaint`, `setBoundVariable`). Zero hex colors and zero loose pixel values on page-level frames. A value with no token gets a question to the user, not a literal.
6. **Auto layout everywhere.** Every container is `figma.createAutoLayout`. Append to the parent before setting `layoutSizingHorizontal/Vertical = 'FILL'`. Use FILL for rows, panels and spacers, HUG for buttons and chips, FIXED only for the VP fixed widths (nav rail 52, utility rail 44, sidebar 200, sidenav 220, banner 44 tall). Never position children with x/y inside a layout.
7. **Name every layer** for what it is (`Page content`, `Grid wrap`, `Row 3`), never `Frame 12`. Repeated structure that is not in the library (a card used six times) becomes one local component with instances, not six copies.
8. **Icons are instances** of `Icon/*` (INSTANCE_SWAP). Never `createNodeFromSvg`, never rotated primitives. A new icon is a library change.
9. **Fonts:** Lexend only, loaded before any text write (`Regular`, `Medium`, `SemiBold`, `Bold`; style names have no spaces). If the text style is applied, do not set `fontName` yourself.
10. **Content comes from the user or the kit's templates.** Do not invent names, numbers or copy for real screens. Placeholder text must be clearly labelled as such.

Variables are remote in a consumer file, so look them up by name, never by guess:

```js
const cols = await figma.teamLibrary.getAvailableLibraryVariableCollectionsAsync();
const vars = await figma.teamLibrary.getVariablesInLibraryCollectionAsync(cols.find(c => c.name === 'Color').key);
const v = await figma.variables.importVariableByKeyAsync(vars.find(x => x.name === 'color/base/text').key);
```

If `find` returns undefined, return the name list and stop. Guessed names (`color/panel/bg`, `color/text/*`) do not exist; page background is `color/page/bg`, card/panel fill `color/base/bg`, body text `color/base/text`.

## 3. Workflow for a page

Follow in order; one `use_figma` call per section, run strictly one at a time, and return every created node ID.

1. **Read the kit first.** The matching `templates/*.html` or `components.html` section, and `css/vp-shell.css` for layout. Note the section list, not pixel values.
2. **Map each section to library parts** using `references/inventory.md`. Write the map (section, component, variant, properties) in chat before building. Gaps go to the user now.
3. **Choose a template as the starting shell.** Hub record, List view and Settings form exist on the library's `Templates` page. For a new page of a known type, import the shell parts (Banner, Nav rail, Utility rail) as instances rather than copying a template frame, so the page stays linked.
4. **Create the root frame first** (1280 wide, vertical auto layout, fill `color/page/bg`), in its own call, placed clear of existing content. Build each section inside it. Never build top-level and reparent across calls.
5. **Shell:** Banner (44 tall, FILL width), then a horizontal Body: Nav rail, Main (FILL), Utility rail. The library now ships only the Floating `Nav rail` (Page=Dashboards) and Floating `Utility rail` (the user removed the Flat variants on 2026-11-02). Wrap them: Nav rail 4px left and 12px top, Utility rail 86px top, both on a `color/workbench/bg` root; set the selected item through its State variant.
6. **Main:** a toolbar or page header, then `Page content` (16px padding from `space/16`, FILL). Hub pages: `Hub toolbar`, a Record card (base bg, 2px top stroke `color/application/top-line`, rounded top), `Record header`, tabs, `Record sidebar` plus tab content. List pages: `List toolbar`, grid wrap of `Grid cell` instances. Settings pages: `Page header`, `Settings sidenav` plus panels.
7. **Grids are rows of Grid cell instances.** Fix each column width on the cell, set cells to `layoutSizingVertical = 'FILL'` so the tallest cell sets the row height, clear the default white fill on row frames, and set the selected row through the `State=Selected` variant of every cell in that row.
8. **Forms:** read-only values use `Display field`; only the field being edited is a `Field`. Do not build walls of inputs. Dialog button order is primary left, Cancel right.
9. **Validate each section:** `get_screenshot` of the section node, then `curl -f -L -o /tmp/figshot/x.png "<url>"` and Read the PNG. Look for clipped text, leftover placeholder text ("Label", "Value", "Button"), wrong variants, and overlap.
10. **Final checks:** run the audit in `references/checks.md`. For a Dark page, screenshot it in Dark.
11. **Report:** what was built, any library gap, and anything not verified.

Known VP conventions: primary or destructive button LEFT and Cancel RIGHT; dialogs 4px radius; inputs 28px; action buttons 32px with 8px radius; info bubbles instead of tooltips; no breadcrumb on hub pages (the settings template does use one); Dela button only for AI actions; status as pills in grids and sidebars as colored square plus text (`Status square`); stages as colored text (`Stage text`).

## 4. Common mistakes

- Dark pages: a text node or frame with a literal fill (a new Text defaults to black, a new frame to white) will not switch. Bind text to `color/base/text`, clear fills on layout-only frames (`Body`, `Page content`), and audit for literal fills before screenshotting Dark. Instances switch on their own.
- Slots: `getNodeByIdAsync` on a slot or a node inside one often returns null in a later call. Re-find by name from the root frame. A hidden slot (`visible=false`) disappears from `children` until `figma.skipInvisibleInstanceChildren = false`; to show a toolbar in only one state, hide the slot in a clone, never in the frame you will clone from.
- Slots ignore `resize` on width. For a max-width body (the dashboard's 1170px) put a fixed-width auto-layout wrapper inside the slot.
- A component instance keeps its library height (Dash card 400): set `layoutSizingVertical = 'HUG'` after filling it.
- Grids: build rows of Widget cell, first column FIXED 250, others FIXED to (grid width - 250) / (n-1), last one FILL, cells `layoutSizingVertical='FILL'`. Zebra rows are 30 tall, so set the row FIXED at 30. A wrapping header cell must be HUG so the row grows.
- Compare against the real page: measure the HTML in headless Chrome (`--dump-dom` with an injected script) and extract table data from the DOM instead of retyping it.
- Calling `figma.importVariableByKeyAsync`: it lives on `figma.variables`.
- Referencing `node.findAncestor`: not available. Walk `parent` instead.

- Building from memory of a key. Keys come from `references/keys.md` or a fresh lookup; never guess an ID.
- Using `search_design_system` before checking `get_libraries`, or combining several terms in one query.
- `layoutSizing = 'FILL'` before `appendChild` (throws), or `resize()` after setting HUG (resets that axis to FIXED).
- Setting text on an instance's text node instead of `setProperties` (the next library update resets it, or it was never linked).
- Reading `componentPropertyDefinitions` on a variant. Read it on the component set.
- Forgetting the Effect geometry mode on Dark pages.
- Screenshotting only the whole page at low resolution. Check each section.
