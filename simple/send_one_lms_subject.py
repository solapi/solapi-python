import requests
import json
import sys
import os.path

sys.path.append('../')

from auth import auth
import config

# LMS 단건 발송
# 제목(subject)을 지정하지 않으면 메시지 내용(text) 앞 부분을 제목으로 사용합니다.
if __name__ == '__main__':
    data = {
        'message': {
            'to': '수신번호 입력',
            'from': '발신번호 입력',
            'subject': 'LMS 제목 입력',
            'text': '한글 45자, 영자 90자 이상 입력되면 자동으로 LMS타입의 문자메시자가 발송됩니다. type 옵션을 주어 명시적으로 타입을 지정할 수도 있습니다.'
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'), headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
