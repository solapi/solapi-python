from solapi import SolapiMessageService
from solapi.model import Message, SendRequestConfig

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)
message = Message(from_="등록한 발신번호", to="01000000000", text="Hello World!")
response = message_service.send(message)
print(response)

# 또는 list Type으로 여러건의 메시지를 발송할 수 있습니다! allow_duplicates를 True로 활성화하면 중복 수신번호를 허용합니다!
messages = [
    Message(from_="등록한 발신번호", to="01000000000", text="Hello World! 1"),
    Message(from_="등록한 발신번호", to="01000000000", text="Hello World! 2"),
    Message(from_="등록한 발신번호", to="01000000000", text="Hello World! 3"),
]
response = message_service.send(messages, SendRequestConfig(allow_duplicates=True))
print(response)
