import json
import sys
sys.path.append('../../lib')
import message

# 활성화된 발신번호 목록 조회

if __name__ == '__main__':
  res = message.get("/senderid/v1/numbers/active")
  print(json.dumps(res.json(), indent=2, ensure_ascii=False))
