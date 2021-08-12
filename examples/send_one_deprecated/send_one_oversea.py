import requests
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

# 해외문자 단건 발송(2건 이상은 그룹메시지를 사용하세요)
if __name__ == '__main__':
    data = {
        'message': {
            'country': '국가번호', # 국가번호를 입력하세요. 예) 미국(1), 중국(86), 일본(81)
            'to': '수신번호',
            'from': '발신번호',
            'text': 'Test Message'
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'), headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
