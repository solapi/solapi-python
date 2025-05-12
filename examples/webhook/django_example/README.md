# SOLAPI Django Webhook 예제

- 해당 예제는 Django에서 SOLAPI에서 제공하는 webhook을 통해 파라미터를 수신할 때 solapi 모듈을 이용하여 메시지 리포트, 그룹 리포트 데이터를 받아오는 예제입니다.
- 해당 예제는 uv를 통해 패키지를 관리하고 있습니다. 따라서 사전에 [uv](https://docs.astral.sh/uv/getting-started/installation/)가 설치되어 있어야합니다.

## Getting Started

예제를 다운로드 받은 직후, 아래의 명령어를 Django 프로젝트 경로에서 입력해주세요.

```bash
uv sync
```

그다음 Django 서버를 실행하려면 아래의 명령어를 실행해주세요.

```bash
uv run manage.py runserver
```

이후에는 `POST http://localhost:8080/webhook/single-report` 또는 `POST http://localhost:8080/webhook/group-report`로 웹훅 데이터를 수신하여 테스트해 볼 수 있습니다.