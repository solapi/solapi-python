from solapi import SolapiMessageService
from solapi.model.request.storage import FileTypeEnum

# API 키와 API Secret을 설정합니다
message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)


def upload_file_example(file_path: str, file_type: FileTypeEnum):
    """
    파일을 업로드하는 예제 함수입니다.

    Args:
        file_path (str): 업로드할 파일의 경로
        file_type (FileTypeEnum): 파일 타입 (MMS, KAKAO, DOCUMENT 등)
    """
    try:
        # 파일 업로드
        response = message_service.upload_file(
            file_path=file_path, upload_type=file_type
        )

        print("파일 업로드 성공!")
        print(f"File ID: {response.file_id}")
        print(f"File Name: {response.name}")
        print(f"File Created: {response.date_created}")

        return response.file_id

    except Exception as e:
        print(f"파일 업로드 실패: {str(e)}")
        return None


# 예제 실행
if __name__ == "__main__":
    # MMS 이미지 업로드 예제
    # 현재 예제는 images 폴더에 있는 example.jpg 파일을 불러오지만, 실제 예제 사용시에는 이미지 파일의 경로를 변경해주세요
    mms_file_id = upload_file_example("../images/example.jpg", FileTypeEnum.MMS)
