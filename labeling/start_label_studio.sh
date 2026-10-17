#!/bin/zsh
# Start Label Studio locally for labeling the NAIP chips.
# Usage (from anywhere): ./labeling/start_label_studio.sh   then open http://localhost:8080
# Stop with Ctrl+C. Labels are stored in labeling/label-studio-data/ (gitignored; export regularly).

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="/Volumes/01-2TB/NJ-Truck-and-Warhouse-Pollution/data"  # external SSD

# Serve the chip PNGs straight from disk (no upload)
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="$DATA/interim/chips"
# Keep Label Studio's database and settings inside the project
export LABEL_STUDIO_BASE_DATA_DIR="$ROOT/labeling/label-studio-data"
# Fully offline: no usage analytics
export COLLECT_ANALYTICS=false

exec "$ROOT/.venv-labelstudio/bin/label-studio" start --port 8080 --no-browser "$@"
