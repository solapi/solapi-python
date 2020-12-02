import requests
import configparser
import json
import sys
import os.path

sys.path.append('../')

from auth import auth
import config

if __name__ == '__main__':
    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    data = {
        'messages': [
            {
                'to': '수신번호 입력',
                'from': '발신번호 입력',
                'text': '예제 메시지'
            },
            {
                'to': '수신번호2 입력',
                'from': '발신번호2 입력',
                'text': '예제 메시지2'
            },
            {
                # 해외 문자
                'country': '국가번호 입력',
                'to': '현지 수신번호',
                'from': '발신번호 입력',
                'text': 'Hello There'
            }
        ]
    }
    res = requests.put(config.getUrl('/messages/v4/groups/[INPUT_GROUP_ID]/messages'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret),
                       json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
