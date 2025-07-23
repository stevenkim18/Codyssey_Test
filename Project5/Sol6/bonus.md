### DockerHub를 사용하는 이유

- github처럼 별도의 공간의 중앙 저장소 역할을 함.
- 협업하기 용이 함.
- 배포나 자동 빌드(CI/CD)를 할 때 연동해서 사용할 수 있음 → 편리 함.
- 클라우드 서비스 환경(AWS GCP 등) 배포하기도 편리함.

### Container Registry 종류 중 3가지


정의

- 컨테이너의 이미지를 저장하는 중앙 저장소
- Docker 회사 이외에도 다양한 회사에서 운영하고 있음.
1. `DockerHub`
	- Docker 회사에서 운영.
	- 가장 많이 사용 됨.
1. `Amazon Elastic Container Registry (ECR)`
	- 아마존 웹 서비스(AWS)에서 운영.
	- 세계 1위 클라우드 서비스 AWS와 호환성이 좋음.
1. `Harbor (하버)`
	- VMWare에서 시작해서, 현재는 CNCF(Cloud Native Computing Foundation)의 그래듀에이티드(Graduated) 프로젝트로 관리되는 오픈 소스.
	- 엔터프라이즈급 보안을 제공하며, 쿠버네티스하고 호환성이 좋음.

그외..

- Google Container Registry (GCR)
- GitHub Container Registry (GHCR)
- 카카오, 네이버, 삼성SDS 등

### 참고 자료

- [https://radiant515.tistory.com/623](https://radiant515.tistory.com/623).

