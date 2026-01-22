"""
카카오 BMS 자유형 PREMIUM_VIDEO 타입 발송 예제
프리미엄 비디오 메시지로, 카카오TV 영상 URL과 썸네일 이미지를 포함합니다.
videoUrl은 반드시 "https://tv.kakao.com/"으로 시작해야 합니다.
유효하지 않은 동영상 URL 기입 시 발송 상태가 그룹 정보를 찾을 수 없음 오류로 표시됩니다.
쿠폰 제목 형식: "N원 할인 쿠폰", "N% 할인 쿠폰", "배송비 할인 쿠폰", "OOO 무료 쿠폰", "OOO UP 쿠폰"
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from pathlib import Path

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.kakao.bms import BmsCoupon, BmsVideo, BmsWebButton
from solapi.model.message_type import MessageType
from solapi.model.request.storage import FileTypeEnum

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

message = RequestMessage(
    from_="발신번호",
    to="수신번호",
    text="🎬 이번 시즌 인기 드라마 하이라이트!\n놓치신 분들을 위한 명장면 모음입니다.",
    type=MessageType.BMS_FREE,
    kakao_options=KakaoOption(
        pf_id="연동한 비즈니스 채널의 pfId",
        bms=Bms(
            targeting="I",
            chat_bubble_type="PREMIUM_VIDEO",
            video=BmsVideo(
                video_url="https://tv.kakao.com/v/460734285",
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

try:
    file_response = message_service.upload_file(
        file_path=str(Path(__file__).parent / "../images/example_square.jpg"),
        upload_type=FileTypeEnum.KAKAO,
    )

    full_message = RequestMessage(
        from_="발신번호",
        to="수신번호",
        text="🍿 주말 영화 추천!\n\n올해 가장 화제가 된 영화를 미리 만나보세요.",
        type=MessageType.BMS_FREE,
        kakao_options=KakaoOption(
            pf_id="연동한 비즈니스 채널의 pfId",
            bms=Bms(
                targeting="I",
                chat_bubble_type="PREMIUM_VIDEO",
                adult=False,
                header="🎥 이 주의 추천 영화",
                content="2024년 최고의 액션 블록버스터! 지금 바로 예고편을 확인해보세요.",
                video=BmsVideo(
                    video_url="https://tv.kakao.com/v/460734285",
                    image_id=file_response.file_id,
                    image_link="https://example.com/movie-trailer",
                ),
                buttons=[
                    BmsWebButton(
                        name="예매하기",
                        link_mobile="https://example.com",
                        link_pc="https://example.com",
                    ),
                ],
                coupon=BmsCoupon(
                    title="10% 할인 쿠폰",
                    description="영화 예매 시 할인",
                    link_mobile="https://example.com/coupon",
                ),
            ),
        ),
    )

    response = message_service.send(full_message)
    print("\n전체 필드 메시지 발송 성공!")
    print(f"Group ID: {response.group_info.group_id}")
except Exception as e:
    print(f"전체 필드 메시지 발송 실패: {str(e)}")
