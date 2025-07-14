from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage

# API 키와 API Secret을 설정합니다
message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

# 카카오 알림톡 발송을 위한 옵션을 생성합니다.
kakao_option = KakaoOption(
    pf_id="계정에 등록된 카카오 비즈니스 채널ID",
    template_id="계정에 등록된 카카오 브랜드 메시지 템플릿 ID",
    # 만약에 템플릿에 변수가 있다면 아래와 같이 설정합니다.
    # 값은 반드시 문자열로 넣어주셔야 합니다!
    # variables={
    #   "#{name}": "홍길동",
    #   "#{age}": "30"
    # }
    # 브랜드 메시지 발송 대상자 설정, M, N 타입은 카카오측의 별도 인허가를 받은 대상만 사용할 수 있습니다.
    # M: 마케팅 수신 동의 대상자 및 카카오 채널 친구
    # N: 마케팅 수신 동의 대상자 및 카카오 채널 친구는 제외한 대상자
    # I: 카카오 채널 친구
    bms=Bms(targeting="M"),
)

# 단일 메시지를 생성합니다
message = RequestMessage(
    from_="발신번호",  # 발신번호 (등록된 발신번호만 사용 가능)
    to="수신번호",  # 수신번호
    kakao_options=kakao_option,
)

# 메시지를 발송합니다
try:
    response = message_service.send(message)
    print("메시지 발송 성공!")
    print(f"Group ID: {response.group_info.group_id}")
    print(f"요청한 메시지 개수: {response.group_info.count.total}")
    print(f"성공한 메시지 개수: {response.group_info.count.registered}")
except Exception as e:
    print(f"메시지 발송 실패: {str(e)}")
