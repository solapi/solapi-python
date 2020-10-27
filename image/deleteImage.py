import requests
import json
import sys
import os.path

sys.path.append('../')

from auth import auth
import config

if __name__ == '__main__':
    # [IMAGE_ID] 에 이미지 아이디를 넣어주세요
    res = requests.delete(config.getUrl('/storage/v1/files/[IMAGE_ID]'),
                        headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
