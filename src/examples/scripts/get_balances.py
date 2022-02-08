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
잔액 조회 예제
'''
if __name__ == '__main__':
    # 반드시 관리 콘솔 내 발급 받으신 API KEY, API SECRET KEY를 입력해주세요.
    api_key = 'INPUT YOUR API KEY'
    api_secret = 'INPUT YOUR SECRET KEY'

    res = requests.get(get_url('/cash/v1/balance'),
                       headers=get_headers(api_key, api_secret))

    # 실제 충전금액 및 포인트는 response 내 각각 balance, point 데이터로 확인할 수 있습니다.
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
