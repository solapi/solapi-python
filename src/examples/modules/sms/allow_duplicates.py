import json
from src.lib import message

'''
중복 수신번호 허용 예제
'''
if __name__ == '__main__':
    data = {
        'allowDuplicates': True,  # 수신번호 중복 입력을 허용합니다.
        'messages': [
            {
                'to': '01000000001',
                'from': '029302266',
                'text': '동일한 수신번호로 발송 #1'
            },
            {
                'to': '01000000001',
                'from': '029302266',
                'text': '동일한 수신번호로 발송 #2'  # 동일한 내용 입력 시 수신된 문자는 하나로 보여질 수 있습니다.
            },
            # 한 번 요청으로 최대 10,000건까지 추가 가능
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
