import json

from datamonitor.reader import load_data, get_last_modified


def test_load_data_returns_parsed_json(tmp_path):
    file_path = tmp_path / "data.json"
    file_path.write_text(json.dumps([{"id": 1}, {"id": 2}]), encoding="utf-8")

    data = load_data(file_path)

    assert data == [{"id": 1}, {"id": 2}]


def test_get_last_modified_returns_file_mtime(tmp_path):
    file_path = tmp_path / "data.json"
    file_path.write_text("{}", encoding="utf-8")

    mtime = get_last_modified(file_path)

    assert mtime == file_path.stat().st_mtime
