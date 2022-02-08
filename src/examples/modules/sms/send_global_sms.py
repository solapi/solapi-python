import json
from src.lib import message

'''
해외 문자발송 예제
'''
if __name__ == '__main__':
    data = {
        'message': {
            'to': '',  # 보내실 수신번호를 국가번호를 제외하여 입력해주세요.
            'from': '029302266',  # 반드시 사용자 개인이 등록한 번호로만 발송 가능합니다.
            'text': 'NURIGO Verification Code: 1234',  # 기본적으로 NURIGO, 1234 등을 변경하여 발송하시는 것을 권장드립니다.
            'country': ''  # 보내실 국가 코드를 입력해주세요, 예) 미국, 캐나다 -> '1', 중국 -> '86', 일본 -> '81'...
        },
    }
    res = message.send_one(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
