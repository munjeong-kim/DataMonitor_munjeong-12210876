import argparse

from datamonitor.monitor import DataMonitor


def main():
    parser = argparse.ArgumentParser(description="로컬 JSON 데이터 실시간 모니터링 도구")
    parser.add_argument("file", help="모니터링할 JSON 파일 경로")
    parser.add_argument("--interval", type=float, default=2.0, help="조회 주기(초), 기본값 2초")
    args = parser.parse_args()

    monitor = DataMonitor(args.file, interval=args.interval)
    try:
        monitor.run()
    except KeyboardInterrupt:
        print("\n모니터링을 종료합니다.")


if __name__ == "__main__":
    main()
