---
name: feedback-cleanup-saved-pages
description: After using Chrome "Save page as complete" downloads for measurements, delete them immediately once done
metadata:
  type: feedback
---

Delete "Save page as complete" downloads from `/Users/alexandrahart/Projects/VantagepointClone/` as soon as the extraction work is done — run `extract-tokens.py`, capture measurements in TUNING.md, then `rm -rf` the `.htm` file and its `_files/` directory. Also delete any raw `.min.css` files dropped there once tokens are extracted.

**Why:** They're large (~12MB each with the _files/ dir), aren't committed to the repo, and aren't needed once measurements are captured. The user confirmed this explicitly on 2026-09-10.

**How to apply:** At the end of any session where a saved page was used for research, offer to clean up before wrapping up — or just do it proactively once extraction is confirmed complete. Do NOT delete the SCSS source files in that same directory (`dashboards.scss`, `production.scss`, `variables.scss`, `_baseComponent.scss`) — those are kept as reference.
