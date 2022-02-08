import json
from src.lib import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': '01000000001',
                'from': '029302266',  # 반드시 RCSBizCenter에 등록된 발신번호 입력
                'text': '템플릿 기반 RCS를 발송합니다.',
                'rcsOptions': {
                    'brandId': 'BR.iIr12HZe3j',  # RCSBizCenter(https://www.rcsbizcenter.com/)에서 발급받은 브랜드ID 입력
                    'templateId': 'RC01TP210727075536693B1z23GR7xWQ',
                    'variables': {
                        '{{변수1}}': '변수1값',
                        '{{변수2}}': '변수2값',
                        '{{변수3}}': '변수3값'
                    }
                }
            },
            {
                'to': ['01000000002', '01000000003'],  # 신번호를 array로 입력하면 같은 내용을 여러명에게 보낼 수 있습니다.
                'from': '029302266',
                'text': '템플릿 기반 RCS를 발송합니다.',
                'rcsOptions': {
                    'brandId': 'BR.iIr12HZe3j',  # RCSBizCenter(https://www.rcsbizcenter.com/)에서 발급받은 브랜드ID 입력
                    'templateId': 'RC01TP210727075536693B1z23GR7xWQ',
                    'variables': {
                        '{{변수1}}': '변수1값',
                        '{{변수2}}': '변수2값',
                        '{{변수3}}': '변수3값'
                    }
                }
            }
            # ...
            # 1만건까지 추가 가능
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
