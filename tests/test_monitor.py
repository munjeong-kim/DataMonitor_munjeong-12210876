from datamonitor.monitor import DataMonitor


def test_get_status_returns_count_and_mtime(mocker):
    mocker.patch("datamonitor.monitor.load_data", return_value=[{"id": 1}, {"id": 2}])
    mocker.patch("datamonitor.monitor.get_last_modified", return_value=1000.0)

    monitor = DataMonitor("dummy.json")
    status = monitor.get_status()

    assert status["count"] == 2
    assert status["mtime"] == 1000.0


def test_has_changed_is_false_on_first_call_and_when_mtime_is_same():
    monitor = DataMonitor("dummy.json")

    first = monitor.has_changed({"mtime": 1000.0})
    second = monitor.has_changed({"mtime": 1000.0})

    assert first is False
    assert second is False


def test_has_changed_is_true_when_mtime_differs():
    monitor = DataMonitor("dummy.json")
    monitor.has_changed({"mtime": 1000.0})

    changed = monitor.has_changed({"mtime": 2000.0})

    assert changed is True


def test_run_prints_status_for_each_iteration_and_sleeps_between(mocker):
    mocker.patch("datamonitor.monitor.load_data", return_value=[{"id": 1}])
    mocker.patch("datamonitor.monitor.get_last_modified", return_value=1000.0)
    mock_sleep = mocker.patch("datamonitor.monitor.time.sleep")
    print_status_mock = mocker.patch.object(DataMonitor, "print_status")

    monitor = DataMonitor("dummy.json", interval=1)
    monitor.run(max_iterations=3)

    assert print_status_mock.call_count == 3
    assert mock_sleep.call_count == 2
