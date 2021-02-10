import requests
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

# 친구톡(버튼) 단건 발송
# 버튼은 총 5개까지 입력 가능
if __name__ == '__main__':
    data = {
        'message': {
            'to': '수신번호 입력',
            'from': '발신번호 입력',
            'text': '광고를 포함하여 어떤 내용이든 제한없이 발송 가능합니다.',
            'kakaoOptions': {
              'pfId': 'KA01PF200323182344986oTFz9CIabcx',       # PFID 입력
              'buttons': [
                {
                  'buttonType': 'WL',
                  'buttonName': '버튼 이름',
                  'linkMo': 'https://example.com',
                  'linkPc': 'https://example.com'
                },
                {
                  'buttonType': 'AL',
                  'buttonName': '앱실행',
                  'linkAnd': 'examplescheme://path',   # 안드로이드
                  'linkIos': 'examplescheme://path'    # iOS
                },
                {
                  'buttonType': 'BK',         # 챗봇에게 키워드를 전달합니다. 버튼이름의 키워드가 그대로 전달됩니다.
                  'buttonName': '봇키워드'
                },
                {
                  'buttonType': 'MD',         # 상담요청하기 버튼을 누르면 수신 받은 알림톡 메시지가 상담원에게 그대로 전달됩니다.
                  'buttonName': '상담요청하기'
                }
              ]
            }
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'), headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
