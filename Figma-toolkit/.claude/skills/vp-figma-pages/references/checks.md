# Checks for a finished page

Run both as read-only `use_figma` calls after the last section. Replace `ROOT_ID` with the page's root frame.

## 1. Library hygiene (all counts must be 0)

```js
const root = await figma.getNodeByIdAsync('ROOT_ID');
const all = root.findAll(() => true);
const insideInstance = n => { let a = n.parent; while (a) { if (a.type === 'INSTANCE') return true; a = a.parent; } return false; };
const own = all.filter(n => !insideInstance(n));
return {
  detachedLookalikes: own.filter(n => n.type === 'FRAME' && /^(Button|Field|Tab|Checkbox|Toggle|Status|Chip)/.test(n.name)).map(n => n.name + ':' + n.id),
  unboundFills: own.filter(n => ['FRAME','RECTANGLE','TEXT','VECTOR'].includes(n.type) && [...(n.fills||[]), ...(n.strokes||[])].some(p => p.type === 'SOLID' && p.visible !== false && !p.boundVariables?.color)).map(n => n.name + ':' + n.id),
  textWithoutStyle: all.filter(n => n.type === 'TEXT' && !n.textStyleId && !insideInstance(n)).map(n => n.name + ':' + n.id),
  defaultNames: own.filter(n => /^(Frame|Rectangle|Group|Ellipse|Text) \d+$/.test(n.name)).map(n => n.id),
  nonLexend: all.filter(n => n.type === 'TEXT' && n.fontName !== figma.mixed && n.fontName.family !== 'Lexend').map(n => n.id),
  placeholders: all.filter(n => n.type === 'TEXT' && /^(Label|Value|Button|Item|Title|Text|Placeholder|Section title|Panel title|Page title)$/.test(n.characters)).map(n => n.name + ':' + n.id + ' "' + n.characters + '"'),
  instances: all.filter(n => n.type === 'INSTANCE' && !insideInstance(n)).length,
  remoteInstances: all.filter(n => n.type === 'INSTANCE' && n.mainComponent && n.mainComponent.remote).length
};
```

`unboundFills` must be 0 for page-level nodes; in a consumer file the instances come from the remote library, so `remoteInstances` should be close to `instances`. A big gap means local copies were made.

## 2. Layout health

```js
const root = await figma.getNodeByIdAsync('ROOT_ID');
const frames = root.findAll(n => n.type === 'FRAME');
return {
  noAutoLayout: frames.filter(f => f.layoutMode === 'NONE' && f.children.length > 1).map(f => f.name + ':' + f.id),
  fixedFrames: frames.filter(f => f.layoutMode !== 'NONE' && f.layoutSizingVertical === 'FIXED' && f !== root).map(f => f.name + ':' + f.id + ' h=' + Math.round(f.height)),
  clipped: root.findAll(n => n.type === 'TEXT' && n.textAutoResize === 'NONE').map(n => n.name + ':' + n.id)
};
```

Fixed-height frames are legitimate for the shell (rails, banner, Main fills the window); anything else should hug or fill.

## 3. Re-generate the inventory after a library change

Run this against the library file and update `inventory.md` and `keys.md`:

```js
const out = [];
for (const p of figma.root.children) {
  if (['---','Templates','Cover','Getting Started','Typography','Colors','Effects','Spacing & Radius','Icons'].includes(p.name)) continue;
  await figma.setCurrentPageAsync(p);
  p.findAll(n => n.type === 'COMPONENT_SET' || (n.type === 'COMPONENT' && n.parent.type !== 'COMPONENT_SET')).forEach(c => out.push({
    page: p.name, name: c.name, key: c.key,
    props: Object.entries(c.componentPropertyDefinitions).map(([k, v]) => k.split('#')[0] + ':' + v.type[0] + (v.variantOptions ? '[' + v.variantOptions.join('|') + ']' : ''))
  }));
}
return out;
```

## Literal-fill audit (run on every page root, Light and Dark clone)

Finds fills on your own nodes (not inside instances) that are not bound to a variable. Expect an empty list.

```js
const inInst = n => { let p = n.parent; while (p) { if (p.type === 'INSTANCE') return true; p = p.parent; } return false; };
const lit = root.findAll(n => 'fills' in n && n.type !== 'INSTANCE' && !inInst(n) && n.fills !== figma.mixed
  && n.fills.some(f => f.type === 'SOLID' && !f.boundVariables?.color)).map(n => n.name);
return lit;
```
