import argparse

from datamonitor.menu import run_menu
from datamonitor.monitor import DataMonitor


def run_watch(args):
    monitor = DataMonitor(args.file, interval=args.interval)
    try:
        monitor.run()
    except KeyboardInterrupt:
        print("\n모니터링을 종료합니다.")


def run_menu_command(args):
    run_menu(args.file)


def main():
    parser = argparse.ArgumentParser(description="로컬 JSON 데이터 모니터링 도구")
    subparsers = parser.add_subparsers(dest="command", required=True)

    watch_parser = subparsers.add_parser("watch", help="콘솔에서 실시간으로 데이터 상태를 폴링")
    watch_parser.add_argument("file", help="모니터링할 JSON 파일 경로")
    watch_parser.add_argument("--interval", type=float, default=2.0, help="조회 주기(초), 기본값 2초")
    watch_parser.set_defaults(func=run_watch)

    menu_parser = subparsers.add_parser("menu", help="메뉴에서 현재 데이터를 조회")
    menu_parser.add_argument("file", help="조회할 JSON 파일 경로")
    menu_parser.set_defaults(func=run_menu_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
