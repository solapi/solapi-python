import json
from src.lib import message

if __name__ == '__main__':
    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # [INPUT_MESSAGE_ID] 에 메세지 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    data = {'messageIds':
        [
            # 배열로 id를 입력하여 한 요청에 여러개의 메세지를 제거할 수 있습니다.
            '[INPUT_MESSAGE_ID]',
            '[INPUT_MESSAGE_ID]'
        ]
    }
    res = message.delete('/messages/v4/groups/[INPUT_GROUP_ID]/messages',
                         data=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
