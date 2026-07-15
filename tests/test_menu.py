from datamonitor import menu


def test_format_data_with_list():
    data = [{"id": 1}, {"id": 2}]

    result = menu.format_data(data)

    assert "총 2건" in result
    assert "{'id': 1}" in result


def test_show_current_data_prints_formatted_data(mocker):
    mocker.patch("datamonitor.menu.load_data", return_value=[{"id": 1}])
    print_mock = mocker.Mock()

    menu.show_current_data("dummy.json", print_func=print_mock)

    print_mock.assert_called_once()
    assert "총 1건" in print_mock.call_args[0][0]


def test_run_menu_shows_data_then_exits(mocker):
    mocker.patch("datamonitor.menu.load_data", return_value=[{"id": 1}])
    input_mock = mocker.Mock(side_effect=["1", "2"])
    print_mock = mocker.Mock()

    menu.run_menu("dummy.json", input_func=input_mock, print_func=print_mock)

    assert input_mock.call_count == 2
    printed = "\n".join(str(call.args[0]) for call in print_mock.call_args_list)
    assert "총 1건" in printed
    assert "종료" in printed


def test_run_menu_handles_invalid_choice_then_exits(mocker):
    mocker.patch("datamonitor.menu.load_data", return_value=[])
    input_mock = mocker.Mock(side_effect=["x", "2"])
    print_mock = mocker.Mock()

    menu.run_menu("dummy.json", input_func=input_mock, print_func=print_mock)

    printed = "\n".join(str(call.args[0]) for call in print_mock.call_args_list)
    assert "잘못된 입력" in printed
