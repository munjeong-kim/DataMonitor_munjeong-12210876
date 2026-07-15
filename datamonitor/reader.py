import json
from pathlib import Path


def load_data(file_path):
    with Path(file_path).open("r", encoding="utf-8") as f:
        return json.load(f)


def get_last_modified(file_path):
    return Path(file_path).stat().st_mtime
