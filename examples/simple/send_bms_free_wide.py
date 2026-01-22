"""
카카오 BMS 자유형 WIDE 타입 발송 예제
와이드 이미지를 사용하는 메시지입니다.
이미지 업로드 시 fileType은 'BMS_WIDE'를 사용해야 합니다. (2:1 비율 이미지 권장)
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from pathlib import Path

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.kakao.bms import BmsWebButton
from solapi.model.message_type import MessageType
from solapi.model.request.storage import FileTypeEnum

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

try:
    file_response = message_service.upload_file(
        file_path=str(Path(__file__).parent / "../images/example_wide.jpg"),
        upload_type=FileTypeEnum.BMS_WIDE,
    )
    print(f"파일 업로드 성공! File ID: {file_response.file_id}")

    message = RequestMessage(
        from_="발신번호",
        to="수신번호",
        text="✨ 이번 시즌 신상품을 만나보세요!\n\n트렌디한 스타일로 가을을 준비하세요.",
        type=MessageType.BMS_FREE,
        kakao_options=KakaoOption(
            pf_id="연동한 비즈니스 채널의 pfId",
            bms=Bms(
                targeting="I",
                chat_bubble_type="WIDE",
                image_id=file_response.file_id,
                buttons=[
                    BmsWebButton(
                        name="자세히 보기",
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
