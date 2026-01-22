"""
카카오 BMS 자유형 CAROUSEL_COMMERCE 타입 발송 예제
캐러셀 커머스 형식으로, 여러 상품을 슬라이드로 보여주는 구조입니다.
이미지 업로드 시 fileType은 'BMS_CAROUSEL_COMMERCE_LIST'를 사용해야 합니다. (2:1 비율 이미지 필수)
head + list(상품카드들) + tail 구조입니다.
head 없이 2-6개 아이템, head 포함 시 1-5개 아이템 가능합니다.
가격 정보(regularPrice, discountPrice, discountRate, discountFixed)는 숫자 타입입니다.
캐러셀 커머스 버튼은 WL, AL 타입만 지원합니다.
쿠폰 제목 형식: "N원 할인 쿠폰", "N% 할인 쿠폰", "배송비 할인 쿠폰", "OOO 무료 쿠폰", "OOO UP 쿠폰"
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from pathlib import Path

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.kakao.bms import (
    BmsAppButton,
    BmsCarouselCommerceItem,
    BmsCarouselCommerceSchema,
    BmsCarouselHead,
    BmsCarouselTail,
    BmsCommerce,
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
        upload_type=FileTypeEnum.BMS_CAROUSEL_COMMERCE_LIST,
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
                chat_bubble_type="CAROUSEL_COMMERCE",
                adult=False,
                additional_content="🔥 이번 주 한정 특가!",
                carousel=BmsCarouselCommerceSchema(
                    head=BmsCarouselHead(
                        header="홍길동님을 위한 추천",
                        content="최근 관심 상품과 비슷한 아이템을 모았어요!",
                        image_id=image_id,
                        link_mobile="https://example.com/recommend",
                    ),
                    items=[
                        BmsCarouselCommerceItem(
                            image_id=image_id,
                            commerce=BmsCommerce(
                                title="에어프라이어 대용량 5.5L",
                                regular_price=159000,
                                discount_price=119000,
                                discount_rate=25,
                            ),
                            additional_content="⚡ 무료배송",
                            image_link="https://example.com/airfryer",
                            buttons=[
                                BmsWebButton(
                                    name="지금 구매",
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
                                title="10000원 할인 쿠폰",
                                description="첫 구매 고객 전용",
                                link_mobile="https://example.com/coupon",
                            ),
                        ),
                        BmsCarouselCommerceItem(
                            image_id=image_id,
                            commerce=BmsCommerce(
                                title="스마트 로봇청소기 프로",
                                regular_price=499000,
                                discount_price=399000,
                                discount_fixed=100000,
                            ),
                            buttons=[
                                BmsWebButton(
                                    name="상세 보기",
                                    link_mobile="https://example.com",
                                    link_pc="https://example.com",
                                ),
                            ],
                        ),
                    ],
                    tail=BmsCarouselTail(
                        link_mobile="https://example.com/all-products",
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
