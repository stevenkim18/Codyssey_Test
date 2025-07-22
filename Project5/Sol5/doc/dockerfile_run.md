### 도커파일로 태그로 이미지 빌드

```python
docker build -t david:v1.0 .
```

- v1.0 태그 설정

### 실행 중인 컨테이너 중지하기

```python
docker stop <컨테이너_ID 또는 이름>
```

### 컨테이너 만들기

```python
docker run -p 80:80 david:v1.0
```

- 호스트, 컨테이너 80포트를 연결

### 실행중인 컨테이너 bash 접속하기

```python
docker exec -it <컨테이너_ID 또는 이름> bash
```