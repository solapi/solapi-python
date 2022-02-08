import json
from src.lib import message

'''
Step 2) 인증번호 요청
해당 전화번호로 전화를 걸어 인증번호를 알려줍니다.
리턴되는 Transaction ID와 인증번호(Token)를 기록해두어 다음 Step에서 사용합니다.
다음 과정으로 verify_token.py 파일을 참고 해주세요.
'''
if __name__ == '__main__':
    # 인증받을 등록된 전화번호 입력
    phoneNumber = '01000000001'

    authInfo = {
        'authType': 'ARS',
        'extras': {
            'phoneNumber': phoneNumber
        }
    }

    headers = {
        'x-mfa-data': json.dumps(authInfo)
    }

    res = message.put("/senderid/v1/numbers/%s/authenticate" % phoneNumber, {}, headers)
    jsonData = res.json()
    print(jsonData)
    print('Transaction ID:', jsonData['mfa']['transactionId'])
