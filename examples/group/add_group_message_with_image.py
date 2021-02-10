import requests
import configparser
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

if __name__ == '__main__':
    # [GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    # [IMAGE_ID] 에 이미지 아이디를 넣어주세요
    data = {
        'messages': json.dumps([
            {
                'to': '수신번호 입력',
                'from': '발신번호 입력',
                'text': '발송 예제 #1',
                'imageId': '[IMAGE_ID]'
            },
            {
                'to': '수신번호2 입력',
                'from': '발신번호2 입력',
                'text': '발송 예제 #2',
                'imageId': '[IMAGE_ID]'
            }
        ])
    }
    res = requests.put(config.getUrl('/messages/v4/groups/[GROUP_ID]/messages',
                       headers=auth.get_headers(config.apiKey, config.apiSecret),
                       json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
