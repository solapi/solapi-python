from solapi import SolapiMessageService
from solapi.model import RequestMessage

# API 키와 API Secret을 설정합니다
message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

# 단일 메시지를 생성합니다
message = RequestMessage(
    from_="발신번호",  # 발신번호 (등록된 발신번호만 사용 가능)
    to="수신번호",  # 수신번호
    text="안녕하세요! SOLAPI Python SDK를 사용한 SMS 발송 예제입니다.",
)

# 메시지를 발송합니다
try:
    response = message_service.send(message)
    print("메시지 발송 성공!")
    print(f"Group ID: {response.group_info.group_id}")
    print(f"요청한 메시지 개수: {response.group_info.count.total}")
    print(f"성공한 메시지 개수: {response.group_info.count.registered_success}")
    print(f"실패한 메시지 개수: {response.group_info.count.registered_failed}")
except Exception as e:
    print(f"메시지 발송 실패: {str(e)}")
