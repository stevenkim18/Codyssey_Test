### 컨테이너 실행시 이름을 지정했을 때와 지정하지 않았을때 차이

- 컨테이너를 생성할 때 이름을 붙일 수 있음
- 안 붙이면 자동으로 생성 됨.

```bash
❯ docker run -it --name my_ubuntu ubuntu:20.04 bash

root@21fa879a72da:/# exit
exit

❯ docker ps -a
CONTAINER ID   IMAGE          COMMAND                   CREATED         STATUS                           PORTS                  NAMES
21fa879a72da   ubuntu:20.04   "bash"                    5 seconds ago   Exited (0) 3 seconds ago                                **my_ubuntu**
ebe99fdeb2f1   nginx          "/docker-entrypoint.…"   25 hours ago    Exited (255) About an hour ago   0.0.0.0:8080->80/tcp   infallible_goldwasser
3e43d3c2fe95   nginx          "/docker-entrypoint.…"   26 hours ago    Exited (0) 25 hours ago                                 romantic_mclaren
```

ID 대신에 이름으로 삭제 가능

```bash
$ docker rm my_ubuntu
my_ubuntu
```

이름은 중복 생성은 안됨.

```bash
❯ docker run -it --name my_ubuntu ubuntu:20.04 bash
docker: Error response from daemon: Conflict. The container name "/my_ubuntu" is already in use by container "21fa879a72daa68df1e10a270393ed98c95c7de7348d474d9ca30427586256a4". You have to remove (or rename) that container to be able to reuse that name.
```

이름을 지정했을 때 장점

- 이름을 지정하지 않았을 때는 자동으로 이름을 생성
- 이름을 지정하면 이름으로 실행 삭제등 제어가 가능해서 편함(id는 외우기 힘듬)