# Labeling Guide

Rules for labeling the NAIP chips in `data/interim/chips/`. Apply them the same way to every chip, train and validation alike. When a case isn't covered here, decide, add the rule below, and keep applying it.

Chip file names start with the imagery year: `2022_c01234.png`. **2019 and 2022** chips are 60 cm per pixel; **2010 and 2015** chips are 1 m.

## warehouse_roof (polygon, hotkey `w`)

Trace the roof outline of every **warehouse or distribution center** in the chip, including ones that are not the chip's centre building.

A warehouse usually has:
- a large, flat, plain roof (often white or grey)
- a row of loading docks along at least one wall
- a truck yard or trailer parking beside the docks

Label it even if it is cut off by the chip edge (trace to the edge).

**Do not label:** big-box stores and malls (customer car parking, entrances, no truck yard), factories and plants (stacks, tanks, piping, complex roofs), offices, schools, hospitals, aircraft hangars, parking garages, apartment blocks.

Can't tell? Label it and tick **uncertain**.

## truck_trailer (polygon, hotkey `t`) — 2019 and 2022 chips only

One polygon per **semi-trailer**: a long box (~16 m, about 25 px at 60 cm), with or without a tractor attached. If a tractor is attached, outline trailer and tractor together.

- Include: trailers at dock doors, in yards, on roads; shipping containers **on a chassis**.
- Do not include: box trucks and vans, cars, stacked shipping containers on the ground, rail cars.
- Partly outside the chip: label it if at least half is visible.
- Trailers packed side by side: still one polygon each; polygons may touch.

## loading_dock (polygon, hotkey `d`) — 2019 and 2022 chips only

One polygon per **continuous row of dock doors** along a wall (not one per door). A gap of several empty door widths, or a change of wall, starts a new polygon. Outline the strip of wall where the doors are; trailers backed into the doors may fall inside it.

## Drawing trailers and docks

Both are drawn as **4-corner polygons**, not axis-aligned boxes, because many buildings and trailers sit at an angle in the chip. Click the four corners in order around the object, following its own edges, so the shape is a rotated rectangle that hugs it. Close the polygon by clicking the first point again. Use exactly 4 points; they are converted to oriented boxes for training.

## 2010 and 2015 chips (1 m)

Label **warehouse_roof only**. Trailers and docks are too small to label reliably at 1 m.

## Flags

- **uncertain**: at least one label is a judgement call. These get a second look before training.
- **unusable**: clouds, blur or missing imagery. Submit the chip with no labels.

A chip with nothing to label (common for negative chips, named `..._neg...`) is still submitted, with no labels. Empty chips teach the model what *not* to detect.

## Workflow

1. Start Label Studio: `./labeling/start_label_studio.sh`, then open http://localhost:8080
2. Label the **train** project and the **val** project the same way. Never copy labels between them.
3. Export regularly (Project → Export → JSON) to `data/interim/labels/`. The Label Studio database is not in git.
