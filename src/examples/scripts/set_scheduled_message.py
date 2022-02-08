import json
import time
import datetime
import uuid
import hmac
import hashlib
import requests
import platform

# 아래 값은 필요시 수정
protocol = 'https'
domain = 'api.solapi.com'
prefix = ''

# 반드시 관리 콘솔 내 발급 받으신 API KEY, API SECRET KEY를 입력해주세요
api_key = 'INPUT YOUR API KEY'
api_secret = 'INPUT YOUR SECRET KEY'


def unique_id():
    return str(uuid.uuid1().hex)


def get_iso_datetime():
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    return datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()


def get_signature(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()


def get_headers(api_key, api_secret):
    date = get_iso_datetime()
    salt = unique_id()
    combined_string = date + salt

    return {
        'Authorization': 'HMAC-SHA256 ApiKey=' + api_key + ', Date=' + date + ', salt=' + salt + ', signature=' +
                         get_signature(api_secret, combined_string),
        'Content-Type': 'application/json; charset=utf-8'
    }


def get_url(path):
    url = '%s://%s' % (protocol, domain)
    if prefix != '':
        url = url + prefix
    url = url + path
    return url


def get(url):
    return requests.get(get_url(url), headers=get_headers(api_key, api_secret))


def post(url, parameter):
    return requests.post(get_url(url), headers=get_headers(api_key, api_secret), json=parameter)


def put(url, parameter):
    return requests.put(get_url(url), headers=get_headers(api_key, api_secret), json=parameter)


def delete(url):
    return requests.delete(get_url(url), headers=get_headers(api_key, api_secret))


'''
예약발송 예제
'''
if __name__ == '__main__':
    # STEP 1 그룹 추가
    addGroupResponse = post('/messages/v4/groups', parameter={
        'sdkVersion': 'python/4.2.0',
        'osPlatform': platform.platform() + " | " + platform.python_version()
    })
    groupResponse: dict = addGroupResponse.json()
    groupId = groupResponse['groupId']

    # STEP 2 발송할 메시지 데이터 추가
    messagesDict = {
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
                'to': ['01000000004', '01000000005'],  # 수신번호를 array로 입력하면 같은 내용을 여러명에게 보낼 수 있습니다.
                'from': '029302266',
                'text': '한글 45자, 영자 90자 이하 입력되면 자동으로 SMS타입의 메시지가 발송됩니다.'
            },
            # 해외발송
            {
                'country': '1',  # 미국(1), 일본(81), 중국(86) 등 국가번호 입력, 국가 번호에 띄어쓰기가 있는 경우 붙여서 기입해야 합니다. 예) +1 809 -> '1809'
                'to': '01000000006',  # 수신번호를 array로 입력하면 같은 내용을 여러명에게 보낼 수 있습니다.
                'from': '029302266',
                'text': '한글 45자, 영자 90자 이하 입력되면 자동으로 SMS타입의 메시지가 발송됩니다.'
            },
            # 알림톡 발송
            {
                'to': '01000000004',
                'from': '029302266',
                'kakaoOptions': {
                    'pfId': 'KA01PF200323182344986oTFz9CIabcx',
                    'templateId': 'KA01TP200323182345741y9yF20aabcx',
                    # 변수: 값 형식으로 모든 변수에 대한 변수값 입력
                    'variables': {
                        '#{변수1}': '변수1의 값',
                        '#{변수2}': '변수2의 값',
                        '#{버튼링크1}': '버튼링크1의 값',
                        '#{버튼링크2}': '버튼링크2의 값',
                        '#{강조문구}': '강조문구의 값'
                    }
                }
            }
            # ...
            # 1만건까지 추가 가능
        ]
    }
    put('/messages/v4/groups/%s/messages' % groupId, parameter=messagesDict)

    # STEP 3 예약 발송일 등록
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)

    # 희망하시는 예약 날짜를 넣어주세요 년
    # datetime(년, 월, 일, 시, 분, 초)
    scheduledDate = datetime.datetime(2022, 2, 8, 15, 0, 0).replace(
        tzinfo=datetime.timezone(offset=utc_offset)).isoformat()
    scheduledDateDict = {
        'scheduledDate': scheduledDate
    }
    setScheduledGroupResponse = post('/messages/v4/groups/%s/schedule' % groupId, parameter=scheduledDateDict)
    print(json.dumps(json.loads(setScheduledGroupResponse.text), indent=2, ensure_ascii=False))

    # 예약 발송 취소를 희망하실 경우 아래 코드를 추가해주세요.
    # delete('/messages/v4/groups/%s/schedule' % groupId)
