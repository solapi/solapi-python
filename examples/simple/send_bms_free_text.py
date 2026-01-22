"""
카카오 BMS 자유형 TEXT 타입 발송 예제
텍스트 전용 메시지로, 가장 기본적인 형태입니다.
targeting 타입 중 M, N의 경우는 카카오 측에서 인허가된 채널만 사용하실 수 있습니다.
그 외의 모든 채널은 I 타입만 사용 가능합니다.
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.message_type import MessageType

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

# 최소 구조 단건 발송 예제
message = RequestMessage(
    from_="발신번호",
    to="수신번호",
    text="안녕하세요! BMS 자유형 TEXT 메시지입니다.\n\n오늘 하루도 행복하세요!",
    type=MessageType.BMS_FREE,
    kakao_options=KakaoOption(
        pf_id="연동한 비즈니스 채널의 pfId",
        bms=Bms(
            targeting="I",
            chat_bubble_type="TEXT",
        ),
    ),
)

try:
    response = message_service.send(message)
    print("메시지 발송 성공!")
    print(f"Group ID: {response.group_info.group_id}")
    print(f"요청한 메시지 개수: {response.group_info.count.total}")
    print(f"성공한 메시지 개수: {response.group_info.count.registered_success}")
except Exception as e:
    print(f"메시지 발송 실패: {str(e)}")

# 전체 필드 단건 발송 예제 (adult, additionalContent 포함)
full_message = RequestMessage(
    from_="발신번호",
    to="수신번호",
    text="🎉 회원님, 특별한 소식이 있습니다!\n\n이번 주말 단독 할인 이벤트가 진행됩니다.\n자세한 내용은 아래 버튼을 눌러 확인해주세요.",
    type=MessageType.BMS_FREE,
    kakao_options=KakaoOption(
        pf_id="연동한 비즈니스 채널의 pfId",
        bms=Bms(
            targeting="I",
            chat_bubble_type="TEXT",
            adult=False,
            additional_content="📅 이벤트 기간: 12월 1일 ~ 12월 7일",
        ),
    ),
)

try:
    response = message_service.send(full_message)
    print("\n전체 필드 메시지 발송 성공!")
    print(f"Group ID: {response.group_info.group_id}")
except Exception as e:
    print(f"전체 필드 메시지 발송 실패: {str(e)}")

# 다건 발송 예제
messages = [
    RequestMessage(
        from_="발신번호",
        to="수신번호1",
        text="첫 번째 수신자에게 보내는 BMS 메시지입니다.",
        type=MessageType.BMS_FREE,
        kakao_options=KakaoOption(
            pf_id="연동한 비즈니스 채널의 pfId",
            bms=Bms(targeting="I", chat_bubble_type="TEXT"),
        ),
    ),
    RequestMessage(
        from_="발신번호",
        to="수신번호2",
        text="두 번째 수신자에게 보내는 BMS 메시지입니다.",
        type=MessageType.BMS_FREE,
        kakao_options=KakaoOption(
            pf_id="연동한 비즈니스 채널의 pfId",
            bms=Bms(targeting="I", chat_bubble_type="TEXT"),
        ),
    ),
]

try:
    response = message_service.send(messages)
    print("\n다건 발송 성공!")
    print(f"Group ID: {response.group_info.group_id}")
    print(f"총 메시지 개수: {response.group_info.count.total}")
except Exception as e:
    print(f"다건 발송 실패: {str(e)}")
