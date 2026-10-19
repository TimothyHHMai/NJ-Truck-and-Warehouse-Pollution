"""Create the Label Studio projects for the validation images: precision, recall, and trailer counts.

Each project gets its label config (label_config_<name>.xml), the labeling guide as its
instructions, and a local-files storage pointing at data/interim/chips/<name>/,
which is synced so every image becomes a task. Safe to re-run: existing projects
only get their label config and instructions refreshed. Projects not listed here
(e.g. the earlier train/val chip projects) are left untouched.

Requires Label Studio to be running (./labeling/start_label_studio.sh).

Usage (from the repo root):
    .venv-labelstudio/bin/python labeling/setup_projects.py
"""

from pathlib import Path

import markdown
import requests

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = Path("/Volumes/01-2TB/NJ-Truck-and-Warhouse-Pollution/data")  # external SSD
CHIP_DIR = DATA / "interim" / "chips"
URL = "http://localhost:8080"
TOKEN = (HERE / "label-studio-data" / ".api_token").read_text().strip()
HEADERS = {"Authorization": f"Token {TOKEN}"}

PROJECTS = {  # image folder (and config name) -> (title, colour)
    "precision": ("NJ validation: warehouse precision", "#E8A33D"),
    "recall": ("NJ validation: warehouse recall", "#3D7EE8"),
    "sites": ("NJ validation: dock-yard trailer counts", "#2FB37A"),
}


def api(method, path, **kwargs):
    resp = requests.request(method, f"{URL}/api{path}", headers=HEADERS, timeout=120, **kwargs)
    resp.raise_for_status()
    return resp.json() if resp.content else None


def main():
    guide = markdown.markdown((HERE / "LABELING_GUIDE.md").read_text())
    existing = {p["title"]: p for p in api("GET", "/projects", params={"page_size": 100})["results"]}

    for name, (title, colour) in PROJECTS.items():
        config = (HERE / f"label_config_{name}.xml").read_text()
        if title in existing:
            pid = existing[title]["id"]
            api("PATCH", f"/projects/{pid}", json={"label_config": config, "expert_instruction": guide})
            print(f"{title}: already exists (id {pid}), label config and guide updated")
            continue
        project = api("POST", "/projects", json={
            "title": title,
            "description": f"NAIP validation images from data/interim/chips/{name}/",
            "label_config": config,
            "expert_instruction": guide,
            "show_instruction": True,
            "color": colour,
        })
        storage = api("POST", "/storages/localfiles", json={
            "project": project["id"],
            "title": f"chips/{name}",
            "path": str(CHIP_DIR / name),
            "regex_filter": r".*\.png$",
            "use_blob_urls": True,
        })
        api("POST", f"/storages/localfiles/{storage['id']}/sync")
        n_tasks = api("GET", f"/projects/{project['id']}")["task_number"]
        print(f"{title}: created (id {project['id']}) with {n_tasks} images")

    print(f"Open {URL}")


if __name__ == "__main__":
    main()
