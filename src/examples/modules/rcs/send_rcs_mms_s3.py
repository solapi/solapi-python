import json
from src.lib import message, storage

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    res = storage.upload_rcs_image('images/sample1.png').json()
    sample1 = res['fileId']
    res = storage.upload_rcs_image('images/sample2.png').json()
    sample2 = res['fileId']
    res = storage.upload_rcs_image('images/sample3.png').json()
    sample3 = res['fileId']

    # 카드 3개 발송 예제(각 카드별 버튼 2개까지 가능)
    data = {
        'messages': [
            {
                'to': ['01000000001', '01000000002'],  # 신번호를 array로 입력하면 같은 내용을 여러명에게 보낼 수 있습니다.
                'from': '029302266',
                'subject': 'Sample 1',
                'text': 'MMS S3 타입 발송 예제입니다.',
                'imageId': sample1,
                'rcsOptions': {
                    'mmsType': 'S3',  # S3 ~ S6 (총 이미지 1M를 넘을 수 없음)
                    'brandId': 'BR.iIr12HZe3j',  # RCSBizCenter(https://www.rcsbizcenter.com/)에서 발급받은 브랜드ID 입력
                    'buttons': [
                        {'buttonType': 'WL', 'buttonName': '버튼1', 'link': 'https://nurigo.net'},
                        {'buttonType': 'WL', 'buttonName': '버튼2', 'link': 'https://nurigo.net'}
                        # , { 'buttonType': 'ML', 'buttonName': '지도 위치 표시', 'latitude': '37.280342669603684', 'longitude': '127.11824209721874', 'label': '누리고', 'link': 'https://nurigo.net' }
                        # , { 'buttonType': 'MQ', 'buttonName': '지도 검색', 'link': 'https://nurigo.net', 'query': '(주)누리고' }
                        # , { 'buttonType': 'MR', 'buttonName': '나의 현재 위치' }
                        # , { 'buttonType': 'CA', 'buttonName': '캘린더 일정 생성', 'title': '제목', 'startTime': '2021-06-19T00:00:00.000Z', 'endTime': '2021-06-19T09:00:00.000Z', 'text': '메모' }
                        # , { 'buttonType': 'CL', 'buttonName': '텍스트 복사', 'text': '복사할 텍스트 내용' }
                        # , { 'buttonType': 'DL', 'buttonName': '전화 걸기', 'phone': '01012345678' }
                        # , { 'buttonType': 'MS', 'buttonName': '메시지 보내기', 'phone': '01012345678', 'text': '보낼 메시지 내용' }
                    ],
                    'additionalBody': [
                        {
                            'imageId': sample2,
                            'title': 'Sample 2',
                            'description': 'Description 설명',  # 총합 1,300자
                            'buttons': [{'buttonType': 'WL', 'buttonName': '버튼1', 'link': 'https://nurigo.net'},
                                        {'buttonType': 'WL', 'buttonName': '버튼2', 'link': 'https://nurigo.net'}]
                        },
                        {
                            'imageId': sample3,
                            'title': 'Sample 3',
                            'description': 'Description 설명',  # 총합 1,300자
                            'buttons': [{'buttonType': 'WL', 'buttonName': '버튼1', 'link': 'https://nurigo.net'},
                                        {'buttonType': 'WL', 'buttonName': '버튼2', 'link': 'https://nurigo.net'}]
                        }
                    ]
                }
            }
            # ...
            # 1만건까지 추가 가능
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
