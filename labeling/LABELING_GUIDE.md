# Labeling Guide

Rules for checking the validation images in `data/interim/chips/{precision,recall,sites}/`, built by `notebooks/03_labeling_dataset.ipynb`. Nothing here is training data: these labels only measure how good the warehouse inventory and the trailer counts are. Apply the rules the same way to every image. When a case isn't covered here, decide, add the rule below, and keep applying it.

## What counts as a warehouse

A warehouse or distribution center usually has:
- a large, flat, plain roof (often white or grey)
- a row of loading docks along at least one wall
- a truck yard or trailer parking beside the docks

**Not warehouses:** big-box stores and malls (customer car parking, entrances, no truck yard), factories and plants (stacks, tanks, piping, complex roofs), offices, schools, hospitals, aircraft hangars, parking garages, apartment blocks.

Mixed buildings (e.g. a plant with a warehouse wing) count as a warehouse if the docks and truck yard are a major part of the site.

## 1. Precision: "NJ validation: warehouse precision"

100 images (2022, 60 cm), one inventory building each, outlined in yellow. Pick one answer for **the outlined building only**:
- **warehouse** (`1`)
- **not_warehouse** (`2`)
- **unsure** (`3`): use sparingly; these get a second look.

If the outline only covers part of a building, judge the building it's on.

## 2. Recall: "NJ validation: warehouse recall"

20 images, each a 1 km × 1 km cell (2022, 60 cm). Every inventory building is outlined in yellow. Scan the whole cell and place one point on each:
- **missed_warehouse** (`m`): a warehouse that is **not** outlined, with its centre inside the image. Count only warehouses about 50,000 sq ft (4,650 m²) or larger, roughly 70 × 70 m or ~115 × 115 px.
- **not_warehouse** (`x`): an outlined building that is **not** a warehouse, again only if its centre is inside the image.

Buildings cut off at the image edge: click only those whose centre is inside (roughly, more than half visible), so each building belongs to exactly one cell.

A cell with nothing to click (common in the `other` cells, r13 to r20) is still submitted, with no points.

## 3. Trailer counts: "NJ validation: dock-yard trailer counts"

70 tiles named `<year>_<site>.png`, e.g. `2019_s20.png`. Each site has a 2022 tile, and 30 sites also have one extra tile: an older one (2019, 2015 or 2010) or a 2023 one at 30 cm. The tile covers the same ground in every year. Label all of a site's tiles in one sitting so you judge them consistently.

Place one **trailer** point (`t`) on the centre of every semi-trailer **anywhere in the tile**, not only at the main building: a long box about 16 m long (53 px at 30 cm, 27 px at 60 cm, 16 px at 1 m), with or without a tractor attached (attached tractor and trailer = one point).
- Include: trailers at dock doors, in yards, on roads; shipping containers **on a chassis**; flatbeds (empty or loaded), tankers, car carriers and other open trailers of semi-trailer length. An empty flatbed is a thin deck: count it only if you can make out its outline.
- Do not include: box trucks and vans, cars, stacked containers on the ground, rail cars.
- At the tile edge: count it if at least half is visible.

**skip_site**: if the 2022 tile has no truck yard (no dock doors or trailer parking), tick it and move on. Skip that site's older tile too. A real yard that happens to be empty that day is **not** skipped: submit it with zero points. Aim for ~30 kept sites.

Only the 2022 tile decides whether a site is skipped. If the 2022 tile is kept, label the older tile normally: if the warehouse wasn't built yet, submit it with zero points rather than skipping it.

**1 m years (2010, 2015):** trailers are ~3 px wide. Count what you can, and tick **uncertain** if a lot of it is guesswork. Seeing how much worse 1 m counts are is part of the point.

## Flags

- **uncertain**: at least one label is a judgement call. These get a second look.
- **unusable**: clouds, blur or missing imagery. Submit with no labels.

## Workflow

1. Start Label Studio: `./labeling/start_label_studio.sh`, then open http://localhost:8080
2. First time only: `.venv-labelstudio/bin/python labeling/setup_projects.py` creates the three projects.
3. Export each project regularly (Project → Export → JSON) to `data/interim/labels/`. The Label Studio database is not in git.
4. File names and `index.csv` in each image folder link every image to its building, cell or site, and to the pixel-to-map transform.
