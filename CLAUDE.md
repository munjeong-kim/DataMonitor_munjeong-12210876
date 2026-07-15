# DataMonitor

## 개요
현재 저장된 데이터의 상태를 콘솔(터미널)에서 실시간으로 조회할 수 있는 관리자용 데이터 모니터링 도구.
현재는 PoC(Proof of Concept) 단계로, 핵심 아이디어의 실현 가능성을 검증하는 것이 목표.

## 목적
- 별도의 대시보드/웹 UI 없이 콘솔만으로 저장된 데이터의 현재 상태를 즉시 확인
- 데이터 변경/적재 상황을 실시간으로 트래킹하여 이상 유무를 빠르게 파악
- 운영자(관리자)가 별도 도구 설치 없이 빠르게 데이터 상태를 점검할 수 있도록 지원

## 현재 상태
- PoC 1차 구현 완료
- Python 3.13 가상환경(.venv) 구성됨

## 프로젝트 구조
```
datamonitor/
  reader.py   # JSON 파일 로드, 최종 수정 시각 조회
  monitor.py  # DataMonitor 클래스 - 상태 조회, 변경 감지, 콘솔 폴링 루프
  cli.py      # 커맨드라인 진입점 (python -m datamonitor.cli <file> --interval N)
data/
  sample_data.json  # 동작 확인용 샘플 데이터
tests/
  test_reader.py
  test_monitor.py
```

## 실행 방법
```
python -m datamonitor.cli data/sample_data.json --interval 2
```

## 테스트 실행
```
pytest -v
```

## 데이터 소스
- 로컬에 저장된 JSON 파일
- 별도의 DB 연결 없이 파일 시스템에서 직접 읽어 상태를 조회

## 테스트
- pytest, pytest-mock 사용
- PoC 기능 검증을 위한 간단한 테스트 위주로 작성 (파일 I/O 등은 pytest-mock으로 모킹)

## PoC 범위 (제안)
- 로컬 JSON 파일을 읽어 현재 데이터 상태(건수, 최신 갱신 시각, 주요 지표 등) 조회
- 콘솔에서 일정 주기로 갱신되는 실시간 뷰 제공 (polling 또는 watch 방식)
- 최소 기능 위주로 구현하고, 이후 요구사항에 따라 확장

## 개발 시 참고사항
- PoC 단계이므로 과도한 추상화나 확장성 설계보다는 핵심 시나리오 검증에 집중
- 데이터 소스가 로컬 JSON으로 고정되어 있으므로 DB 연동을 고려한 설계는 불필요
