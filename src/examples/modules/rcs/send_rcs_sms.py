import json
from src.lib import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': '01000000001',
                'from': '029302266',  # 반드시 RCSBizCenter에 등록된 발신번호 입력
                'text': 'RCS SMS를 발송합니다.',
                'rcsOptions': {
                    'brandId': 'BR.iIr12HZe3j',  # RCSBizCenter(https://www.rcsbizcenter.com/)에서 발급받은 브랜드ID 입력
                }
            },
            {
                'to': ['01000000002', '01000000003'],  # 신번호를 array로 입력하면 같은 내용을 여러명에게 보낼 수 있습니다.
                'from': '029302266',
                'text': 'RCS SMS를 발송합니다.',
                'rcsOptions': {
                    'brandId': 'BR.iIr12HZe3j',  # RCSBizCenter(https://www.rcsbizcenter.com/)에서 발급받은 브랜드ID 입력
                    'buttons': [
                        {'buttonType': 'WL', 'buttonName': '홈페이지 바로가기', 'link': 'https://nurigo.net'}
                        # , { 'buttonType': 'ML', 'buttonName': '지도 위치 표시', 'latitude': '37.280342669603684', 'longitude': '127.11824209721874', 'label': '누리고', 'link': 'https://nurigo.net' }
                        # , { 'buttonType': 'MQ', 'buttonName': '지도 검색', 'link': 'https://nurigo.net', 'query': '(주)누리고' }
                        # , { 'buttonType': 'MR', 'buttonName': '나의 현재 위치' }
                        # , { 'buttonType': 'CA', 'buttonName': '캘린더 일정 생성', 'title': '제목', 'startTime': '2021-06-19T00:00:00.000Z', 'endTime': '2021-06-19T09:00:00.000Z', 'text': '메모' }
                        # , { 'buttonType': 'CL', 'buttonName': '텍스트 복사', 'text': '복사할 텍스트 내용' }
                        # , { 'buttonType': 'DL', 'buttonName': '전화 걸기', 'phone': '01012345678' }
                        # , { 'buttonType': 'MS', 'buttonName': '메시지 보내기', 'phone': '01012345678', 'text': '보낼 메시지 내용' }
                    ]
                }
            }
            # ...
            # 1만건까지 추가 가능
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
