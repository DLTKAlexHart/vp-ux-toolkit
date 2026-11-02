# Figma Toolkit

Everything for the Vantagepoint Figma component library ("VP Toolkit – Component Library"): two Claude Code skills, the key and component references, and the build docs.

- **Library file:** key `QLYlJbr59j7i5becv6k2pq`, Deltek, Inc. plan `organization::1303904496611212311`.
- **Name in consumer files:** "vp-kit - Component Library" (the name it was published under).
- **Source of truth:** this repo's HTML/CSS kit (`css/`, `components.html`, `templates/`, `docs/COMPONENTS.md`). The library mirrors it.

## Contents

| Path | What it is |
|---|---|
| `.claude/skills/vp-figma-library/` | Skill for **changing the library**: recipe, gotchas, audit, current state. `scripts/extract-font-rules.py` pulls typography rules from the kit CSS. |
| `.claude/skills/vp-figma-pages/` | Skill for **building screens** from the published library. |
| `.claude/skills/vp-figma-pages/references/inventory.md` | Every component, its variants and properties. |
| `.claude/skills/vp-figma-pages/references/keys.md` | Component, style and variable keys for imports. |
| `.claude/skills/vp-figma-pages/references/checks.md` | Audit to run on a finished page. |
| `docs/FIGMA-BUILD-PLAN.md` | Phased work order for the library build. |
| `docs/FIGMA-GAP-AUDIT.md` | Dashboard kit vs library gap audit (written 2026-11-02, partly stale: the gaps it lists have since been built). |

## Requirements

- Claude Code with the **Figma plugin** (provides the Figma MCP tools and the `figma-use`, `figma-generate-design` and `figma-generate-library` skills the two skills depend on).
- Edit access to the library file. Publishing is manual: the API cannot do it.

## Loading the skills

Claude Code discovers skills from a `.claude/skills/` folder in the directory you start it in, or from `~/.claude/skills/` for every project.

**Option A, per project (simplest).** Start Claude Code from this folder:

```bash
cd Figma-toolkit
claude
```

Both skills load automatically. Check with `/skills` or ask "what skills do you have?".

**Option B, everywhere.** Link them into your user skills folder:

```bash
mkdir -p ~/.claude/skills
ln -s "$PWD/.claude/skills/vp-figma-library" ~/.claude/skills/vp-figma-library
ln -s "$PWD/.claude/skills/vp-figma-pages"   ~/.claude/skills/vp-figma-pages
```

Symlinks keep one copy, so edits stay in sync. Use `cp -R` instead to give a teammate a standalone copy.

**Option C, inside another project.** Copy or link the two folders into that project's `.claude/skills/`.

Restart Claude Code after adding skills. They trigger from the request (for example "mock up a list page in Figma" uses `vp-figma-pages`), or invoke one directly with `/vp-figma-pages` or `/vp-figma-library`.

## Which skill when

| You want to | Skill |
|---|---|
| Design or mock up a screen, dialog or template in Figma; find the right component or variable | `vp-figma-pages` |
| Add or fix a component, variable, style or icon in the library | `vp-figma-library` |

Never edit a main component from a page file. Change the library, publish, then accept the update in the consumer file.

## Workflow

1. **Edit the library** with `vp-figma-library` (one `use_figma` call at a time, audit after each page).
2. **Publish** in Figma: Assets panel, Libraries, Publish.
3. **Accept the update** in each consumer file (Assets, Libraries, Update). Until then, new variants and properties do not exist there.
4. **Build pages** with `vp-figma-pages`: confirm the library is enabled (`get_libraries`), then import by key from `references/keys.md`.
5. **Update the references** (`inventory.md`, `keys.md`) whenever the library changes, so the pages skill stays accurate.

## Conventions

- One component per concept; merge variants through properties, never "X (variant)" copies.
- Colours, spacing and radii are bound variables; text and shadows are styles; icons are instances.
- Lexend only.
- Code Connect mapping is not started.

## Paths

The skills refer to the kit by paths relative to the repo root (`css/`, `templates/`, `docs/`). This folder sits at the repo root, so they resolve as is. A few references point outside this repo (brand assets, the Lexend variable font) and are labelled as such.
