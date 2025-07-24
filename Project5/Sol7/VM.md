UTM에 우분투 22:04 설치

https://solearn.tistory.com/275

### 현재 우분투 사용자 docker 권한을 주기

그룹 생성

```bash
$ sudo groupadd docker

“group ‘docker’ already exists”
```

현재 사용자를 docker 그룹에 추가

```bash
$ sudo usermod -aG docker $USER
```

현재 쉘에 적용

```bash
newgrp docker
```

- 반드시 해야 함!

잘 추가되었는지 확인.

```bash
$ groups $USER           
name : name adm cdrom sudo dip plugdev lxd docker
```