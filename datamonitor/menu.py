from datamonitor.reader import load_data

MENU_TEXT = """
==== 데이터 모니터링 메뉴 ====
1. 데이터 조회
2. 종료
"""


def format_data(data):
    if isinstance(data, list):
        lines = [f"- {item}" for item in data]
    elif isinstance(data, dict):
        lines = [f"- {key}: {value}" for key, value in data.items()]
    else:
        return str(data)
    return f"총 {len(data)}건\n" + "\n".join(lines)


def show_current_data(file_path, print_func=print):
    data = load_data(file_path)
    print_func(format_data(data))


def run_menu(file_path, input_func=input, print_func=print):
    while True:
        print_func(MENU_TEXT)
        choice = input_func("메뉴를 선택하세요: ").strip()
        if choice == "1":
            show_current_data(file_path, print_func=print_func)
        elif choice == "2":
            print_func("프로그램을 종료합니다.")
            break
        else:
            print_func("잘못된 입력입니다. 다시 선택해주세요.")
