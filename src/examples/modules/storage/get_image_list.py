import requests
import json
from src.lib import auth, config

'''
이미지 파일 리스트 조회 예제
'''
if __name__ == '__main__':
    res = requests.get(config.get_url('/storage/v1/files'), headers=auth.get_headers(config.api_key, config.api_secret))
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
