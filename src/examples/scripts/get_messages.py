import json
import time
import datetime
import uuid
import hmac
import hashlib
import requests

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


'''
메시지 조회 예제(알림톡, 일반 문자 등 모두 포함) 
'''
if __name__ == '__main__':
    # 반드시 관리 콘솔 내 발급 받으신 API KEY, API SECRET KEY를 입력해주세요
    api_key = 'INPUT YOUR API KEY'
    api_secret = 'INPUT YOUR SECRET KEY'

    res = requests.get(get_url('/messages/v4/list'),
                       headers=get_headers(api_key, api_secret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # limit
    res = requests.get(get_url('/messages/v4/list?limit=10'),
                       headers=get_headers(api_key, api_secret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # messageId
    res = requests.get(get_url('/messages/v4/list?messageId=XXXXXXX'),
                       headers=get_headers(api_key, api_secret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # groupId
    res = requests.get(get_url('/messages/v4/list?groupId=XXXXXXX'),
                       headers=get_headers(api_key, api_secret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 수신번호로 조회
    res = requests.get(get_url('/messages/v4/list?to=01000000001'),
                       headers=get_headers(api_key, api_secret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 발신번호로 조회
    res = requests.get(get_url('/messages/v4/list?from=029302266'),
                       headers=get_headers(api_key, api_secret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 메시지타입으로 조회
    res = requests.get(get_url('/messages/v4/list?type=SMS'),
                       headers=get_headers(api_key, api_secret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 메시지 상태 코드로 조회
    res = requests.get(get_url('/messages/v4/list?statusCode=4000'),
                       headers=get_headers(api_key, api_secret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 페이지 처리
    page1 = requests.get(get_url('/messages/v4/list?limit=5'),
                         headers=get_headers(api_key, api_secret)).json()
    print(json.dumps(page1, indent=2, ensure_ascii=False))
    if 'nextKey' in res:
        # 읽어올 데이터가 더 있음
        startKey = res['nextKey']
        page2 = requests.get(get_url('/messages/v4/list?limit=5&startKey=%s' % startKey),
                             headers=get_headers(api_key, api_secret)).json()
        print(json.dumps(page2, indent=2, ensure_ascii=False))
