# Solapi SDK for Python

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-370/)

lib/config.ini 파일을 아래와 같이 설정 후 examples 아래 예제 코드를 실행해 보세요.

```
[AUTH]
# 계정의 API Key와 API Secret을 입력해주세요
api_key = [API KEY]
api_secret = [API SECRET]

[SERVER]
domain = api.solapi.com
protocol = https
prefix =
```

### SOLAPI SDK 이용을 위해 아래 라이브러리 설치를 필요로 합니다.

- requests
- configparser

### 한 파일로 예제를 확인하고 싶으신 경우 examples/all_in_one.py를 참고 해주세요.