import requests
import json
import lib.auth as auth
import lib.config as config
import lib.message as message

if __name__ == '__main__':
    # [GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    # [IMAGE_ID] 에 이미지 아이디를 넣어주세요
    data = {
        'messages': json.dumps([
            {
                'to': '수신번호 입력',
                'from': '발신번호 입력',
                'text': '발송 예제 #1',
                'imageId': '[IMAGE_ID]'
            },
            {
                'to': '수신번호2 입력',
                'from': '발신번호2 입력',
                'text': '발송 예제 #2',
                'imageId': '[IMAGE_ID]'
            }
        ])
    }
    res = message.put('/messages/v4/groups/[GROUP_ID]/messages', data=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
