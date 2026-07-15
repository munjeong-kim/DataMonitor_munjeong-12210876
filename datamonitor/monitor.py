import time
from datetime import datetime

from datamonitor.reader import load_data, get_last_modified


class DataMonitor:
    def __init__(self, file_path, interval=2.0):
        self.file_path = file_path
        self.interval = interval
        self._last_mtime = None

    def get_status(self):
        data = load_data(self.file_path)
        mtime = get_last_modified(self.file_path)
        count = len(data) if isinstance(data, (list, dict)) else 1
        return {
            "count": count,
            "last_modified": datetime.fromtimestamp(mtime).isoformat(),
            "mtime": mtime,
        }

    def has_changed(self, status):
        changed = self._last_mtime is not None and status["mtime"] != self._last_mtime
        self._last_mtime = status["mtime"]
        return changed

    def run(self, max_iterations=None):
        iterations = 0
        while max_iterations is None or iterations < max_iterations:
            status = self.get_status()
            changed = self.has_changed(status)
            self.print_status(status, changed)
            iterations += 1
            if max_iterations is None or iterations < max_iterations:
                time.sleep(self.interval)

    @staticmethod
    def print_status(status, changed):
        marker = "[CHANGED]" if changed else "[OK]"
        print(f"{marker} count={status['count']} last_modified={status['last_modified']}")
