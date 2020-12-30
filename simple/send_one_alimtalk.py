import requests
import json
import sys
import os.path

sys.path.append('../')

from auth import auth
import config

# 알림톡 단건 발송
if __name__ == '__main__':
    data = {
        'message': {
            'to': '수신번호 입력',
            'from': '발신번호 입력',
            'text': '홍길동님 가입을 환영합니다.',
            'kakaoOptions': {
              'pfId': 'KA01PF200323182344986oTFz9CIabcx',       # PFID 입력
              'templateId': 'KA01TP200323182345741y9yF20aabcx'  # 템플릿아이디 입력
            }
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'), headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
