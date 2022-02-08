import requests
import json
from src.lib import auth, config

'''
이미지 파일 단 건 조회 예제
'''
if __name__ == '__main__':
    # [FILE_ID] 에 fileId를 넣어주세요
    res = requests.get(config.get_url('/storage/v1/files/[FILE_ID]'),
                       headers=auth.get_headers(config.api_key, config.api_secret))
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
