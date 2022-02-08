import json
from src.lib import message

'''
예약 발송 취소 예제, 이미 예약 발송이 설정되어 있어야 합니다. 
'''
if __name__ == '__main__':
    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    res = message.delete('/messages/v4/groups/[INPUT_GROUP_ID]/schedule', data=None)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
