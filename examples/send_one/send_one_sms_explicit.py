import requests
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

# type을 SMS로 지정한 경우 한글 45, 영어 90자를 넘으면 오류가 발생합니다.
if __name__ == '__main__':
    data = {
        'message': {
            'type': 'SMS',
            'to': '수신번호 입력',
            'from': '발신번호 입력',
            'text': '테스트 메시지'
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'), headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
