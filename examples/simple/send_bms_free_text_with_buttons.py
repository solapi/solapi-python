"""
카카오 BMS 자유형 TEXT 타입 + 버튼 발송 예제
텍스트와 버튼을 포함한 메시지입니다.
BMS 자유형 버튼 타입: WL(웹링크), AL(앱링크), AC(채널추가), BK(봇키워드), MD(상담요청), BC(상담톡전환), BT(챗봇전환), BF(비즈니스폼)
쿠폰 제목 형식: "N원 할인 쿠폰", "N% 할인 쿠폰", "배송비 할인 쿠폰", "OOO 무료 쿠폰", "OOO UP 쿠폰"
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.kakao.bms import (
    BmsAppButton,
    BmsBotKeywordButton,
    BmsChannelAddButton,
    BmsCoupon,
    BmsWebButton,
)
from solapi.model.message_type import MessageType

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

message = RequestMessage(
    from_="발신번호",
    to="수신번호",
    text="🎁 연말 감사 이벤트!\n\n한 해 동안 함께해주셔서 감사합니다.\n특별한 혜택으로 보답드려요!",
    type=MessageType.BMS_FREE,
    kakao_options=KakaoOption(
        pf_id="연동한 비즈니스 채널의 pfId",
        bms=Bms(
            targeting="I",
            chat_bubble_type="TEXT",
            adult=False,
            buttons=[
                BmsWebButton(name="이벤트 참여하기", link_mobile="https://example.com"),
                BmsAppButton(
                    name="앱에서 보기",
                    link_mobile="https://example.com",
                    link_android="examplescheme://path",
                    link_ios="examplescheme://path",
                ),
                BmsChannelAddButton(name="채널 추가"),
                BmsBotKeywordButton(name="이벤트 문의", chat_extra="event_inquiry"),
            ],
            coupon=BmsCoupon(
                title="10000원 할인 쿠폰",
                description="연말 감사 할인 쿠폰입니다.",
                link_mobile="https://example.com/coupon",
            ),
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
