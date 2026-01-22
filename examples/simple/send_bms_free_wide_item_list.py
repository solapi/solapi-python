"""
카카오 BMS 자유형 WIDE_ITEM_LIST 타입 발송 예제
와이드 아이템 리스트 형식으로, 메인 아이템(2:1 비율)과 서브 아이템(1:1 비율)으로 구성됩니다.
메인 아이템: fileType은 'BMS_WIDE_MAIN_ITEM_LIST' (2:1 비율 이미지 필수)
서브 아이템: fileType은 'BMS_WIDE_SUB_ITEM_LIST' (1:1 비율 이미지 필수, 최소 3개 필요)
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from pathlib import Path

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.kakao.bms import BmsMainWideItem, BmsSubWideItem, BmsWebButton
from solapi.model.message_type import MessageType
from solapi.model.request.storage import FileTypeEnum

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

try:
    main_file_response = message_service.upload_file(
        file_path=str(Path(__file__).parent / "../images/example_wide.jpg"),
        upload_type=FileTypeEnum.BMS_WIDE_MAIN_ITEM_LIST,
    )
    main_image_id = main_file_response.file_id
    print(f"메인 이미지 업로드 성공! File ID: {main_image_id}")

    sub_file_response = message_service.upload_file(
        file_path=str(Path(__file__).parent / "../images/example_square.jpg"),
        upload_type=FileTypeEnum.BMS_WIDE_SUB_ITEM_LIST,
    )
    sub_image_id = sub_file_response.file_id
    print(f"서브 이미지 업로드 성공! File ID: {sub_image_id}")

    message = RequestMessage(
        from_="발신번호",
        to="수신번호",
        type=MessageType.BMS_FREE,
        kakao_options=KakaoOption(
            pf_id="연동한 비즈니스 채널의 pfId",
            bms=Bms(
                targeting="I",
                chat_bubble_type="WIDE_ITEM_LIST",
                header="🏆 베스트 상품 모음",
                main_wide_item=BmsMainWideItem(
                    image_id=main_image_id,
                    title="이번 주 인기 상품",
                    link_mobile="https://example.com/main",
                ),
                sub_wide_item_list=[
                    BmsSubWideItem(
                        image_id=sub_image_id,
                        title="인기 1위 - 프리미엄 티셔츠",
                        link_mobile="https://example.com/item1",
                    ),
                    BmsSubWideItem(
                        image_id=sub_image_id,
                        title="인기 2위 - 캐주얼 팬츠",
                        link_mobile="https://example.com/item2",
                    ),
                    BmsSubWideItem(
                        image_id=sub_image_id,
                        title="인기 3위 - 데일리 백",
                        link_mobile="https://example.com/item3",
                    ),
                ],
                buttons=[
                    BmsWebButton(
                        name="전체 상품 보기",
                        link_mobile="https://example.com",
                    ),
                ],
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
