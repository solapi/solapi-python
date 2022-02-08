import json
from src.lib import message

'''
활성화 된 발신번호 목록을 조회하는 예제
'''
if __name__ == '__main__':
    res = message.get("/senderid/v1/numbers/active")
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
