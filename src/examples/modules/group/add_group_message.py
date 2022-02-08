import json
from src.lib import message

if __name__ == '__main__':
    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    data = {
        'messages': [
            {
                'to': '수신번호 입력',
                'from': '발신번호 입력',
                'text': '예제 메시지'
            },
            {
                'to': '수신번호2 입력',
                'from': '발신번호2 입력',
                'text': '예제 메시지2'
            },
            {
                # 해외 문자
                'country': '국가번호 입력',
                'to': '현지 수신번호',
                'from': '발신번호 입력',
                'text': 'Hello There'
            }
        ]
    }
    res = message.put('/messages/v4/groups/[INPUT_GROUP_ID]/messages', data=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
