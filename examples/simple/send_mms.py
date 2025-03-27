from os.path import abspath
from solapi import SolapiMessageService
from solapi.model import Message
from solapi.model.request.storage import FileTypeEnum

# API 키와 API Secret을 설정합니다
message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

# 이미지 파일을 업로드합니다
try:
    # 이미지 파일 업로드 (MMS 타입으로 지정)
    file_response = message_service.upload_file(
        file_path=abspath(
            "../images/example.jpg"
        ),  # 실제 이미지 파일 경로로 변경해주세요
        upload_type=FileTypeEnum.MMS,
    )

    print("파일 업로드 성공!")
    print(f"File ID: {file_response.file_id}")

    # MMS 메시지를 생성하고 발송합니다
    message = Message(
        from_="발신번호",  # 발신번호 (등록된 발신번호만 사용 가능)
        to="수신번호",  # 수신번호
        # subject="MMS 제목", # MMS 제목, 제목을 지정하지 않는다면 필요하지 않습니다.
        text="MMS 메시지 내용입니다.",
        image_id=file_response.file_id,  # 업로드된 파일의 ID를 지정
    )

    # 메시지를 발송합니다
    response = message_service.send(message)
    print("\nMMS 발송 성공!")
    print(f"Group ID: {response.group_id}")
    print(f"요청한 메시지 개수: {response.group_info.count.total}")
    print(f"성공한 메시지 개수: {response.group_info.count.registered}")

except Exception as e:
    print(f"MMS 발송 실패: {str(e)}")
