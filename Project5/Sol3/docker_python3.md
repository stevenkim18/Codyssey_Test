### python3 다운

```bash
❯ docker pull python:3
3: Pulling from library/python
16155e1a57f6: Pull complete
1f8ab7c4e8b4: Pull complete
35a65abb6272: Pull complete
7be9cdb9167a: Pull complete
88f9cdd730a2: Pull complete
7898f305cd67: Pull complete
1561f28e69ee: Pull complete
Digest: sha256:28f60ab75da2183870846130cead1f6af30162148d3238348f78f89cf6160b5d
Status: Downloaded newer image for python:3
docker.io/library/python:3

❯ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    f5c017fb33c6   3 days ago     281MB
python       3         28f60ab75da2   5 weeks ago    1.47GB
```

### python3 컨테이너 생성

- bash 쉘 실행
- 컨네이너와 호스트 80 포트 연결

```bash
$ docker run -it -p 80:80 python:3 bash
```

### 새로운 터미널 창을 띄워서, 작업 폴더 → 컨테이너로 이동

```bash
docker cp . <컨테이너 이름 또는 ID>:<폴더 경로>

❯ docker cp . quirky_montalcini:/app
Successfully copied 74.7MB to quirky_montalcini:/app
```

### ⚠️ 컨테이너에서 vim 설치

```bash
apt-get update
apt-get install vim
```

### 컨테이너 내부에서 flask 앱을 열고 외부에서 접근하기

```bash
docker run -it -p 8080:80 python:3 bash
```

- 호스트의 포트는 8080으로 열고 컨테이너의 포트는 80으로 열기

```python
app.run(host="0.0.0.0", port=80)
```

- Docker 컨테이너 내부에 flask 앱에서
    - ip는 전체
    - 포트는 80은 열어야 함.

```bash
pip install flask gtts // 필요한 패키지 설치

python app.py // python앱 실행
```

### 지금 현재 있는 컨테이너를 이미지로 만들기

```bash
docker commit <현재 컨테이너 이름> <저장할 이미지 이름>
```

```bash
❯ docker commit hardcore_yalow python_david
sha256:d9e5f455d6009d62c405e5ce4f795b6e279629735ef5dae6d9fd564b94fdf4c8

❯ docker images
REPOSITORY     TAG       IMAGE ID       CREATED         SIZE
python_david   latest    d9e5f455d600   4 seconds ago   1.47GB
nginx          latest    f5c017fb33c6   3 days ago      281MB
python         3         28f60ab75da2   5 weeks ago     1.47GB
ubuntu         20.04     8feb4d8ca535   3 months ago    101MB
```

### `python:3` 로 만들어진 컨테이너 전부 삭제

```bash
❯ docker ps -a --filter ancestor=python:3 -q | xargs docker rm -f
cc6ed1e713af
7ec0ed1e216b
51c9249e9033
```

### 다시 `python:3` 컨테이너 만들기

- 당연히 아무것도 없음

### `python_david` 이미지로 컨테이너 만들기

```bash
docker run -it -p 8080:80 python_david bash
```

- 우리가 저장한 파일들이 그대로 있음.