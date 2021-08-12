import requests
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

# 문자 단건 발송
if __name__ == '__main__':
    data = {
        'message': {
            'to': '수신번호 입력',
            'from': '발신번호 입력',
            'text': '테스트 메시지' # 한글 45자, 영어 90자 이상이면 LMS로 자동 발송
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'), headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
