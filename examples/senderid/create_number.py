import json
import sys
sys.path.append('../../lib')
import message

#
# Step 1) 발신번호 등록
#

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
  res = message.post("/senderid/v1/numbers", { 'phoneNumber': '01000000001' })
  print(json.dumps(res.json(), indent=2, ensure_ascii=False))
