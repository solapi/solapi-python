"""
카카오 BMS 자유형 CAROUSEL_FEED 타입 발송 예제
캐러셀 피드 형식으로, 여러 카드를 좌우로 슬라이드하는 구조입니다.
이미지 업로드 시 fileType은 'BMS_CAROUSEL_FEED_LIST'를 사용해야 합니다. (2:1 비율 이미지 필수)
head 없이 2-6개 아이템, head 포함 시 1-5개 아이템 가능합니다.
캐러셀 피드 버튼은 WL, AL 타입만 지원합니다.
쿠폰 제목 형식: "N원 할인 쿠폰", "N% 할인 쿠폰", "배송비 할인 쿠폰", "OOO 무료 쿠폰", "OOO UP 쿠폰"
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from pathlib import Path

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.kakao.bms import (
    BmsAppButton,
    BmsCarouselFeedItem,
    BmsCarouselFeedSchema,
    BmsCarouselTail,
    BmsCoupon,
    BmsWebButton,
)
from solapi.model.message_type import MessageType
from solapi.model.request.storage import FileTypeEnum

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

try:
    file_response = message_service.upload_file(
        file_path=str(Path(__file__).parent / "../images/example_wide.jpg"),
        upload_type=FileTypeEnum.BMS_CAROUSEL_FEED_LIST,
    )
    image_id = file_response.file_id
    print(f"파일 업로드 성공! File ID: {image_id}")

    message = RequestMessage(
        from_="발신번호",
        to="수신번호",
        type=MessageType.BMS_FREE,
        kakao_options=KakaoOption(
            pf_id="연동한 비즈니스 채널의 pfId",
            bms=Bms(
                targeting="I",
                chat_bubble_type="CAROUSEL_FEED",
                adult=False,
                carousel=BmsCarouselFeedSchema(
                    items=[
                        BmsCarouselFeedItem(
                            header="🏃 마라톤 완주 도전!",
                            content="첫 마라톤 완주를 목표로 8주 트레이닝 프로그램을 시작해보세요.",
                            image_id=image_id,
                            image_link="https://example.com/marathon",
                            buttons=[
                                BmsWebButton(
                                    name="프로그램 신청",
                                    link_mobile="https://example.com",
                                    link_pc="https://example.com",
                                ),
                                BmsAppButton(
                                    name="앱에서 보기",
                                    link_mobile="https://example.com",
                                    link_android="examplescheme://path",
                                    link_ios="examplescheme://path",
                                ),
                            ],
                            coupon=BmsCoupon(
                                title="10% 할인 쿠폰",
                                description="첫 등록 고객 전용",
                                link_mobile="https://example.com/coupon",
                            ),
                        ),
                        BmsCarouselFeedItem(
                            header="🧘 요가 입문 클래스",
                            content="초보자를 위한 기초 요가 동작을 배워보세요. 유연성과 마음의 평화를 함께!",
                            image_id=image_id,
                            buttons=[
                                BmsWebButton(
                                    name="클래스 보기",
                                    link_mobile="https://example.com",
                                    link_pc="https://example.com",
                                ),
                            ],
                        ),
                        BmsCarouselFeedItem(
                            header="💪 홈트레이닝 루틴",
                            content="장비 없이도 OK! 집에서 하는 30분 전신 운동 루틴.",
                            image_id=image_id,
                            buttons=[
                                BmsAppButton(
                                    name="영상 시청",
                                    link_mobile="https://example.com",
                                    link_android="examplescheme://path",
                                    link_ios="examplescheme://path",
                                ),
                            ],
                        ),
                    ],
                    tail=BmsCarouselTail(
                        link_mobile="https://example.com/more",
                        link_pc="https://example.com/more",
                    ),
                ),
            ),
        ),
    )

    response = message_service.send(message)
    print("메시지 발송 성공!")
    print(f"Group ID: {response.group_info.group_id}")
    print(f"요청한 메시지 개수: {response.group_info.count.total}")
    print(f"성공한 메시지 개수: {response.group_info.count.registered_success}")
except Exception as e:
    print(f"발송 실패: {str(e)}")
