import requests
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

# 친구톡 단건 발송
if __name__ == '__main__':
    data = {
        'message': {
            'to': '수신번호 입력',
            'from': '발신번호 입력',
            'text': '광고를 포함하여 어떤 내용이든 제한없이 발송 가능합니다.',
            'kakaoOptions': {
              'pfId': 'KA01PF200323182344986oTFz9CIabcx'       # PFID 입력
            }
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'), headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
