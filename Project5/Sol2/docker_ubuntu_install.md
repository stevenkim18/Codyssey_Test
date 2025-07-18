### Docker 명령어로 이미지 검색

```bash
$ docker search ubuntu
NAME                             DESCRIPTION                                      STARS     OFFICIAL
ubuntu                           Ubuntu is a Debian-based Linux operating sys…   17632     [OK]
ubuntu/squid                     Squid is a caching proxy for the Web. Long-t…   117
ubuntu/nginx                     Nginx, a high-performance reverse proxy & we…   131
ubuntu/cortex                    Cortex provides storage for Prometheus. Long…   4
ubuntu/kafka                     Apache Kafka, a distributed event streaming …   55
ubuntu/apache2                   Apache, a secure & extensible open-source HT…   97
ubuntu/prometheus                Prometheus is a systems and service monitori…   73
```

### Docker Hub에서 우분투 검색

https://hub.docker.com/search?q=ubuntu

https://hub.docker.com/_/ubuntu

### 우분투 20.04 태그 확인

https://hub.docker.com/_/ubuntu/tags?name=20.04

### DockerHub에서 이미지 받기

```bash
$ docker pull ubuntu:20.04
20.04: Pulling from library/ubuntu
ecd83b6c3544: Pull complete
Digest: sha256:8feb4d8ca5354def3d8fce243717141ce31e2c428701f6682bd2fafe15388214
Status: Downloaded newer image for ubuntu:20.04
docker.io/library/ubuntu:20.04

$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    f5c017fb33c6   3 days ago     281MB
ubuntu       20.04     8feb4d8ca535   3 months ago   101MB
```

### 이미지 상세정보 확인

```bash
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    f5c017fb33c6   3 days ago     281MB
ubuntu       20.04     8feb4d8ca535   3 months ago   101MB

$ docker inspect 8feb4d8ca535
[
    {
        "Id": "sha256:8feb4d8ca5354def3d8fce243717141ce31e2c428701f6682bd2fafe15388214",
        "RepoTags": [
            "ubuntu:20.04"
        ],
        "RepoDigests": [
            "ubuntu@sha256:8feb4d8ca5354def3d8fce243717141ce31e2c428701f6682bd2fafe15388214"
        ],
        ....
        ....
```

### 이미지 히스토리 조회

```bash
$ docker history ubuntu:20.04
IMAGE          CREATED        CREATED BY                                       SIZE      COMMENT
8feb4d8ca535   3 months ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]             0B
<missing>      3 months ago   /bin/sh -c #(nop) ADD file:2c90d89e4dd4e1d24…   74.6MB
<missing>      3 months ago   /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      3 months ago   /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      3 months ago   /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH      0B
<missing>      3 months ago   /bin/sh -c #(nop)  ARG RELEASE                   0B
```

### 우분투 컨테이너 생성 후 bash 접속

```bash
docker run -it ubuntu:20.04 bash
```

- -it: -i(interactive) + -t(pseudo-TTY), 터미널 환경 제공
- bash: 실행할 명령어 (bash 쉘)

우분투 나가기

```bash
exit
```

### 컨테이너에서 임의의 파일 1개 생성

```bash
$ cd home
$ touch 1.txt
```

### bash 종료, 컨테이너 삭제

```bash
exit
docker rm 컨테이너id
```

### 다시 생성 후 확인

```bash
docker run -it ubuntu:20.04 bash
```

- 만들었던 파일이 없음.
- 컨테이너를 새로 생성하면 이미지에 있는 것들만 생성됨.
- 초기화 된것이나 마찬가지.