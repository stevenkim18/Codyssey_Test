### Windows의 Docker Desktop에서 리눅스 컨테이너와 윈도우 컨테이너의 차이를 문서로 제출한다.

배경

- 리눅스와 맥은 unix 기반이지만 윈도우는 OS의 태생이 다름.
- 현업에서 리눅스를 서버로 많이 사용하지만 윈도우도 서버용 OS를 서비스하고 있음(Window Server)
- Window, Docker Desktop에서 리눅스 컨테이너와 윈도우 컨테이너를 설정해서 사용할 수 있음.
    - 동시에 사용은 안되고 2개 중에 한개만 가능.

운영 체제 커널

| 항목 | 리눅스 컨테이너 (Linux Containers) | 윈도우 컨테이너 (Windows Containers) |
| --- | --- | --- |
| 사용 커널 | Linux 커널 | Windows NT 커널 |
| 커널 공유 여부 | WSL2 또는 Hyper-V를 통해 가상 머신 위에서 Linux 커널 공유 | Windows 호스트 커널 또는 Hyper-V 격리 사용 |

이미지 및 호환성

| 항목 | 리눅스 컨테이너 | 윈도우 컨테이너 |
| --- | --- | --- |
| 이미지 종류 | Ubuntu, Alpine, Debian 등 | Windows Server Core, Nano Server 등 |
| 호환성 | Linux 기반 앱만 실행 가능 | Windows 전용 앱만 실행 가능 |
| 크로스 플랫폼 지원 | 가능 (Windows, Mac, Linux) | 불가능 (Windows에서만 실행 가능) |

실행환경

| 항목 | 리눅스 컨테이너 | 윈도우 컨테이너 |
| --- | --- | --- |
| 기본 실행 환경 | WSL2 기반 경량 VM 또는 Hyper-V | Windows Server 기반 |
| 성능 | 경량, 빠름 | 상대적으로 무거움 |
| 실행 모드 | 단일 모드 | 프로세스 격리 / Hyper-V 격리 지원 |

사용 목적 및 제한

| 항목 | 리눅스 컨테이너 | 윈도우 컨테이너 |
| --- | --- | --- |
| 주요 사용 사례 | 오픈소스 기반 웹앱, 백엔드 등 | .NET Framework, Windows 전용 앱 등 |
| 호스트 OS 제한 | 없음 | Windows 10/11 Pro, Enterprise, Server에서만 사용 가능 |
| 파일 시스템 구조 | Linux 파일 시스템 구조 | Windows 파일 시스템 구조 |