from solapi import SolapiMessageService

# from solapi.model.request.messages.get_messages import GetMessagesRequest

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

try:
    response = message_service.get_messages(
        # 메시지를 조회할 때 아래와 같이 조건을 지정할 수 있습니다.
        # GetMessagesRequest(
        #     start_date="2025-01-01",
        #     end_date="2025-01-03"
        # )
    )
    print(response)
except Exception as e:
    print(e)
