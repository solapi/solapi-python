import json
from src.lib import message

if __name__ == '__main__':
    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    res = message.post('/messages/v4/groups/[INPUT_GROUP_ID]/send', data={})
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
