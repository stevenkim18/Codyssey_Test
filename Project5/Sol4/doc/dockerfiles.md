### requirements.txt 파일의 역할

- 설치해야 될 python 패캐지들의 이름과 버전을 명시하고, 다시 프로젝트를 세팅할 때, 사용할 수 있다.

```python
absl-py==2.1.0
annotated-types==0.7.0
anyio==4.4.0
argon2-cffi==23.1.0
argon2-cffi-bindings==21.2.0
arrow==1.3.0
asttokens==2.4.1
astunparse==1.6.3
...
wsproto==1.2.0
xyzservices==2024.9.0
yfinance==0.2.51
zstandard==0.23.0
```

### PC의 작업 디렉토리에 requirements.txt 파일을 새로 추가하고 에디터로 현재 프로젝트에서 사용중인 flask, gunicorn, gTTS 3가지의 Python 패키지명을 명시한다.

```python
// requirements.txt
flask
gunicorn
gTTS
```

### DockerFile이란

- 도커 이미지를 빌드하고 사용하는 스크립트 파일
- 명령어 차례대로 실행함.

### DockerFile 주요 명령어

`FROM` - 베이스가 되는 이미지

```docker
FROM python:3.11-slim // python 3.11 이미지 사용
```

`WORKDIR` - 명령어를 실행할 디렉토리 경로 지정

```docker
WORKDIR /app // /app 폴더로 지정
```

****`COPY` - 호스트의 디렉토리에서 컨테이너의 디렉토리로 복사

```docker
COPY app.py /app/app.py 
COPY . .   // 현재 내 디렉토리에서 컨테이너의 작업 디렉토리로 복사
```

`RUN` - 이미지를 생성할 때 필요한 명령어 실행

```docker
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt
```

- 주로 프로그램 설치에 많이 사용됨.

`EXPOSE` - 컨테이너에서 사용할 포트 문서화

```docker
EXPOSE 80
```

- 실제로 포트가 열리는 것은 아님.
- `docker run -p` 명령어로 열어야 함.

`CMD` - 컨테이너가 시작하고 실행될 명령어

```docker
CMD ["python", "app.py"]
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80"]
```

- `main:app` - [main.py](http://main.py)파일에 app 객체를 실행하라는 의미.
- `"--bind", "0.0.0.0:80"`  - 네트워크 연결 바인딩.

### Dockerfile로 이미지 만들기

```bash
$ docker build -t <이미지 이름> <DockerFile이 있는 디렉토리>

$ docker build -t my-image .
```

```bash
$ docker build -t python_daivd .
[+] Building 6.8s (10/10) FINISHED                       docker:desktop-linux
 => [internal] load build definition from Dockerfile                     0.0s
 => => transferring dockerfile: 203B                                     0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim      1.8s
 => [auth] library/python:pull token for registry-1.docker.io            0.0s
 => [internal] load .dockerignore                                        0.0s
 => => transferring context: 80B                                         0.0s
 => [1/4] FROM docker.io/library/python:3.10-slim@sha256:9dd6774a127617  0.0s
 => => resolve docker.io/library/python:3.10-slim@sha256:9dd6774a127617  0.0s
 => [internal] load build context                                        0.0s
 => => transferring context: 1.55kB                                      0.0s
 => CACHED [2/4] WORKDIR /app                                            0.0s
 => [3/4] COPY . .                                                       0.0s
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt             3.9s
 => exporting to image                                                   0.9s 
 => => exporting layers                                                  0.7s 
 => => exporting manifest sha256:3af7a119cb56611bd30bd5d0327ad787878de9  0.0s 
 => => exporting config sha256:d09bff26d014663c71a9d6100de16d13f9404706  0.0s 
 => => exporting attestation manifest sha256:ed5e5b4dddd216276c079712e0  0.0s 
 => => exporting manifest list sha256:7d719181653a64729f7bf65146825b199  0.0s 
 => => naming to docker.io/library/python_daivd:latest                   0.0s
 => => unpacking to docker.io/library/python_daivd:latest  
```

- 이미지가 성공적으로 생성됨!

### DockerFile로 만들어진 이미지로 컨테이너 실행하기

```bash
$ docker run -p 8080:80 python_daivd
[2025-07-21 02:10:41 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2025-07-21 02:10:41 +0000] [1] [INFO] Listening at: http://0.0.0.0:80 (1)
[2025-07-21 02:10:41 +0000] [1] [INFO] Using worker: sync
[2025-07-21 02:10:41 +0000] [7] [INFO] Booting worker with pid: 7
```

- dockerfile에서 pip 설치와 명령어 실행을 넣어놔서 아무런 작업을 하지 않아도 됨.
- 바로 [localhost:8080](http://localhost:8080) 으로 접속하면 우리가 저장한 페이지 접근 가능