"""
카카오 BMS 자유형 IMAGE 타입 발송 예제
이미지 업로드 후 imageId를 사용하여 발송합니다.
이미지 업로드 시 fileType은 반드시 'BMS'를 사용해야 합니다.
발신번호, 수신번호에 반드시 -, * 등 특수문자를 제거하여 기입하시기 바랍니다. 예) 01012345678
"""

from pathlib import Path

from solapi import SolapiMessageService
from solapi.model import Bms, KakaoOption, RequestMessage
from solapi.model.message_type import MessageType
from solapi.model.request.storage import FileTypeEnum

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

try:
    file_response = message_service.upload_file(
        file_path=str(Path(__file__).parent / "../images/example_square.jpg"),
        upload_type=FileTypeEnum.BMS,
    )
    print(f"파일 업로드 성공! File ID: {file_response.file_id}")

    message = RequestMessage(
        from_="발신번호",
        to="수신번호",
        text="🆕 신상품이 입고되었어요!\n지금 바로 확인해보세요.",
        type=MessageType.BMS_FREE,
        kakao_options=KakaoOption(
            pf_id="연동한 비즈니스 채널의 pfId",
            bms=Bms(
                targeting="I",
                chat_bubble_type="IMAGE",
                image_id=file_response.file_id,
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
