import json
from src.lib import message

'''
Step 3) 인증번호 확인
Step 2 과정에서 획득한 정보를 모두 입력하여 인증 받습니다.
이 과정이 모두 끝나면 정상적으로 발신번호를 이용하실 수 있습니다.
'''
if __name__ == '__main__':
    # 전화번호 입력
    phoneNumber = '01000000001'

    # Transaction ID 입력
    transactionId = 'cc4f482bcf167f69f2b15fcfd044f509'

    # 음성으로 전달받은 인증번호
    token = '7894'

    authInfo = {
        'authType': 'ARS',
        'extras': {
            'phoneNumber': phoneNumber
        },
        'transactionId': transactionId,
        'token': token
    }

    headers = {
        'x-mfa-data': json.dumps(authInfo)
    }

    res = message.put("/senderid/v1/numbers/%s/authenticate" % phoneNumber, {}, headers)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
