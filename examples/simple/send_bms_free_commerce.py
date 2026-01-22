"""
카카오 BMS 자유형 COMMERCE 타입 발송 예제
커머스(상품) 메시지로, 상품 이미지와 가격 정보, 쿠폰을 포함합니다.
이미지 업로드 시 fileType은 'BMS'를 사용해야 합니다. (2:1 비율 이미지 권장)
COMMERCE 타입은 buttons가 필수입니다 (최소 1개).
가격 정보(regularPrice, discountPrice, discountRate, discountFixed)는 숫자 타입입니다.
쿠폰 제목 형식: "N원 할인 쿠폰", "N% 할인 쿠폰", "배송비 할인 쿠폰", "OOO 무료 쿠폰", "OOO UP 쿠폰"
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from pathlib import Path

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.kakao.bms import (
    BmsAppButton,
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
        upload_type=FileTypeEnum.BMS,
    )
    print(f"파일 업로드 성공! File ID: {file_response.file_id}")

    message = RequestMessage(
        from_="발신번호",
        to="수신번호",
        type=MessageType.BMS_FREE,
        kakao_options=KakaoOption(
            pf_id="연동한 비즈니스 채널의 pfId",
            bms=Bms(
                targeting="I",
                chat_bubble_type="COMMERCE",
                adult=False,
                additional_content="🚀 오늘 주문 시 내일 도착! 무료배송",
                image_id=file_response.file_id,
                commerce=BmsCommerce(
                    title="스마트 공기청정기 2024 신형",
                    regular_price=299000,
                    discount_price=209000,
                    discount_rate=30,
                ),
                buttons=[
                    BmsWebButton(
                        name="지금 구매하기",
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
                    title="포인트 UP 쿠폰",
                    description="구매 시 2배 적립",
                    link_mobile="https://example.com/coupon",
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
