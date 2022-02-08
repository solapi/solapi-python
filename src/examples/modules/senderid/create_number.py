import json
from src.lib import message

'''
STEP 1) 발신번호 추가 예제
다음 과정으로 request_voicecall.py 파일을 참고 해주세요.
'''
if __name__ == '__main__':
  res = message.post("/senderid/v1/numbers", {'phoneNumber': '01000000001'})
  print(json.dumps(res.json(), indent=2, ensure_ascii=False))
