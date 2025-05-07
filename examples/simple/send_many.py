from solapi import SolapiMessageService
from solapi.model import RequestMessage, SendRequestConfig

# API 키와 API Secret을 설정합니다
message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

# 여러 메시지를 생성합니다
messages = [
    RequestMessage(from_="발신번호", to="수신번호1", text="첫 번째 메시지입니다."),
    RequestMessage(from_="발신번호", to="수신번호2", text="두 번째 메시지입니다."),
    RequestMessage(from_="발신번호", to="수신번호3", text="세 번째 메시지입니다."),
]

# SendRequestConfig를 사용하여 중복 수신번호 허용 설정
config = SendRequestConfig(
    allow_duplicates=True  # 중복 수신번호 허용
)

# 메시지를 발송합니다
try:
    response = message_service.send(messages, config)
    print("메시지 발송 성공!")
    print(f"Group ID: {response.group_info.group_id}")
    print(f"요청한 메시지 개수: {response.group_info.count.total}")
    print(f"성공한 메시지 개수: {response.group_info.count.registered}")

    # 실패한 메시지가 있는 경우
    if response.failed_message_list:
        print("\n실패한 메시지 목록:")
        for failed in response.failed_message_list:
            print(f"수신번호: {failed.message.to}")
            print(f"실패 사유: {failed.error.message}\n")
except Exception as e:
    print(f"메시지 발송 실패: {str(e)}")
