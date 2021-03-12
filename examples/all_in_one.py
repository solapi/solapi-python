import json
import time
import datetime
import uuid
import hmac
import hashlib
import requests

# apiKey, apiSecret 입력 필수
apiKey = 'INPUT YOUR API KEY'
apiSecret = 'INPUT YOUR SECRET KEY'

# 아래 값은 필요시 수정
protocol = 'https'
domain = 'api.solapi.com'
prefix = ''

def unique_id():
    return str(uuid.uuid1().hex)

def get_iso_datetime():
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    return datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()

def get_signature(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()

def get_headers(apiKey, apiSecret):
    date = get_iso_datetime()
    salt = unique_id()
    data = date + salt
    return {
      'Authorization': 'HMAC-SHA256 ApiKey=' + apiKey + ', Date=' + date + ', salt=' + salt + ', signature=' +
                             get_signature(apiSecret, data),
      'Content-Type': 'application/json; charset=utf-8'
    }

def getUrl(path):
  url = '%s://%s' % (protocol, domain)
  if prefix != '':
    url = url + prefix
  url = url + path
  return url

def sendMany(data):
  return requests.post(getUrl('/messages/v4/send-many'), headers=get_headers(apiKey, apiSecret), json=data)

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
  data = {
    'messages': [
      {
        'to': '01000000001',
        'from': '029302266',
        'text': '한글 45자, 영자 90자 이하 입력되면 자동으로 SMS타입의 메시지가 추가됩니다.'
      },
      {
        'to': '01000000002',
        'from': '029302266',
        'text': '한글 45자, 영자 90자 이상 입력되면 자동으로 LMS타입의 문자메시자가 발송됩니다. 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      },
      {
        'type': 'SMS',
        'to': '01000000003',
        'from': '029302266',
        'text': 'SMS 타입에 한글 45자, 영자 90자 이상 입력되면 오류가 발생합니다. 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      },
      {
        'to': [ '01000000004', '01000000005' ], # 수신번호를 array로 입력하면 같은 내용을 여러명에게 보낼 수 있습니다.
        'from': '029302266',
        'text': '한글 45자, 영자 90자 이하 입력되면 자동으로 SMS타입의 메시지가 발송됩니다.'
      },
      # 해외발송
      {
        'country': '1', # 미국(1), 일본(81), 중국(86) 등 국가번호 입력
        'to': '01000000006', # 수신번호를 array로 입력하면 같은 내용을 여러명에게 보낼 수 있습니다.
        'from': '029302266',
        'text': '한글 45자, 영자 90자 이하 입력되면 자동으로 SMS타입의 메시지가 발송됩니다.'
      },
      # 알림톡 발송
      {
        'to': '01000000004',
        'from': '029302266',
        'text': '버튼은 최대 5개까지 추가 가능하며 템플릿 내용과 마찬가지로 버튼 내용도 등록 및 검수 받은 내용 그대로 입력되어야 합니다.',
        'kakaoOptions': {
          'pfId': 'KA01PF200323182344986oTFz9CIabcx',
          'templateId': 'KA01TP200323182345741y9yF20aabcx',
          'buttons': [
            {
              'buttonType': 'WL', # 웹링크
              'buttonName': '버튼 이름',
              'linkMo': 'https://m.example.com',
              'linkPc': 'https://example.com'     # 템플릿 등록 시 모바일링크만 입력하였다면 linkPc 값은 입력하시면 안됩니다.
            },
            {
              'buttonType': 'AL', # 앱링크
              'buttonName': '실행 버튼',
              'linkAnd': 'examplescheme://',  # 안드로이드
              'linkIos': 'examplescheme://'   # iOS
            },
            {
              'buttonType': 'DS', # 배송조회
              'buttonName': '배송 조회'
            },
            {
              'buttonType': 'BK', # 봇키워드(챗봇에게 키워드를 전달합니다. 버튼이름의 키워드가 그대로 전달됩니다.)
              'buttonName': '봇키워드'
            },
            {
              'buttonType': 'MD', # 상담요청하기 (상담요청하기 버튼을 누르면 메시지 내용이 상담원에게 그대로 전달됩니다.)
              'buttonName': '상담요청하기'
            }
          ]
        }
      }
      # ...
      # 1만건까지 추가 가능
    ]
  }
  res = sendMany(data)
  print(json.dumps(res.json(), indent=2, ensure_ascii=False))
