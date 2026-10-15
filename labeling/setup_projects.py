"""Create the Label Studio projects for the chips: one for train, one for validation.

Each project gets the label config (label_config.xml), the labeling guide as its
instructions, and a local-files storage pointing at data/interim/chips/<split>/,
which is synced so every chip becomes a task. Safe to re-run: existing projects
are left alone.

Requires Label Studio to be running (./labeling/start_label_studio.sh).

Usage (from the repo root):
    .venv-labelstudio/bin/python labeling/setup_projects.py
"""

from pathlib import Path

import markdown
import requests

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CHIP_DIR = ROOT / "data" / "interim" / "chips"
URL = "http://localhost:8080"
TOKEN = (HERE / "label-studio-data" / ".api_token").read_text().strip()
HEADERS = {"Authorization": f"Token {TOKEN}"}

PROJECTS = {
    "train": "NJ warehouses: train",
    "val": "NJ warehouses: validation (never train on these)",
}


def api(method, path, **kwargs):
    resp = requests.request(method, f"{URL}/api{path}", headers=HEADERS, timeout=120, **kwargs)
    resp.raise_for_status()
    return resp.json() if resp.content else None


def main():
    config = (HERE / "label_config.xml").read_text()
    guide = markdown.markdown((HERE / "LABELING_GUIDE.md").read_text())
    existing = {p["title"]: p for p in api("GET", "/projects", params={"page_size": 100})["results"]}

    for split, title in PROJECTS.items():
        if title in existing:
            print(f"{title}: already exists (id {existing[title]['id']}), skipped")
            continue
        project = api("POST", "/projects", json={
            "title": title,
            "description": f"512 x 512 NAIP chips from data/interim/chips/{split}/",
            "label_config": config,
            "expert_instruction": guide,
            "show_instruction": True,
            "color": "#E8A33D" if split == "train" else "#3D7EE8",
        })
        storage = api("POST", "/storages/localfiles", json={
            "project": project["id"],
            "title": f"chips/{split}",
            "path": str(CHIP_DIR / split),
            "regex_filter": r".*\.png$",
            "use_blob_urls": True,
        })
        api("POST", f"/storages/localfiles/{storage['id']}/sync")
        n_tasks = api("GET", f"/projects/{project['id']}")["task_number"]
        print(f"{title}: created (id {project['id']}) with {n_tasks} chips")

    print(f"Open {URL}")


if __name__ == "__main__":
    main()
