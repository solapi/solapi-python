import json
from src.lib import message, storage

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    res = storage.upload_image('../testImage.jpg').json()
    fileId = res['fileId']
    data = {
        'messages': [
            {
                'to': '01000000001',
                'from': '029302266',
                'subject': 'MMS 제목',
                'imageId': fileId,
                'text': '이미지 아이디가 입력되면 MMS로 발송됩니다.'
            },
            {
                'to': '01000000002',
                'from': '029302266',
                'subject': 'MMS 제목',
                'imageId': fileId,
                'text': '동일한 이미지 아이디가 입력되면 동일한 이미지가 MMS로 발송됩니다.'
            },
            {
                'to': ['01000000003', '01000000004'],  # array로 입력하면 여러명에게 동일한 내용으로 발송됩니다.
                'from': '029302266',
                'subject': 'MMS 제목',
                'imageId': fileId,
                'text': '동일한 이미지 아이디가 입력되면 동일한 이미지가 MMS로 발송됩니다.'
            }
            # ...
            # 1만건까지 추가 가능
        ]
    }
    res = message.send_many(data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
