### Docker Desktop 설치

https://www.docker.com/products/docker-desktop/

- 도커 설치 후 로그인 및 실행
- 터미널을 열어서 `docker --version`  → 버전 잘 나오면 설치 성공

### hello-world 이미지 실행하기

```bash
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.
....
....
```

- 먼저 로컬에 hello-world 이미지가 있는지 확인
- 없으면 docker-hub에서 다운로드 함.
- 문자열만 출력하고 종료됨.
- 맨 처음 docker를 설치했을 때, 잘 동작을 하나 확인하는 용도로 쓰임.
    - Docker 엔진, 이미지 다운로드, 컨테이너 생성, 출력, 종료

### 컨테이너 목록 확인 하기

```bash
docker ps // 실행 중인 컨테이너 확인
docker ps - a // 종료된 것 까지 확인

docker inspect 컨테이너ID // 컨테이너 상세 정보 확인
```

### 간단한 웹 서버 이미지 띄워 보기

```bash
$ docker run -d -p 8080:80 nginx

$ docker ps
CONTAINER ID   IMAGE     COMMAND                   CREATED         STATUS         PORTS                                     NAMES
3e43d3c2fe95   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   romantic_mclaren

$ docker inspect 3e43d3c2fe95 // 도커 정보 상세하기 보기

$ docker logs 3e43d3c2fe95

$ docker stop 3e43d3c2fe95 // 컨테이너 종료하기
```

- localhost:8080으로 접속해서 nginx가 페이지 나오는지 확인
- -d: 백그라운드 실행
- -p 8080:80: 외부의 8080포트와 내부의 80포트 연결

### 이미지의 히스토리 보기

```bash
$ docker history hello-world
IMAGE          CREATED        CREATED BY                SIZE      COMMENT
ec153840d1e6   5 months ago   CMD ["/hello"]            0B        buildkit.dockerfile.v0
<missing>      5 months ago   COPY hello / # buildkit   12.3kB    buildkit.dockerfile.v0
```

### 이미지 목록 조회 및 삭제

```bash
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
nginx         latest    f5c017fb33c6   2 days ago     281MB
hello-world   latest    ec153840d1e6   5 months ago   17kB
```

이미지 삭제하기

```bash
$ docker rmi ec153840d1e6

Error response from daemon: conflict: unable to delete ec153840d1e6 (must be forced) - image is being used by stopped container 230d30351faa
```

- 컨테이너가 종료되었어도 사용하고 있는 컨테이너를 먼저 삭제 해야 함.

컨테이너 전체 삭제 후 이미지 삭제

```bash
$ docker rm a1fc100ab30b
a1fc100ab30b

// hello-world인 컨테이너들을 조회하고 한번에 삭제
$ docker ps -a --filter ancestor=hello-world -q | xargs docker rm
61f6d6292cde
230d30351faa
5c803b0b7c3e

$ docker rmi ec153840d1e6
Untagged: hello-world:latest
Deleted: sha256:ec153840d1e635ac434fab5e377081f17e0e15afab27beb3f726c3265039cfff
```