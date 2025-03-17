from solapi.message_service import SolapiMessageService
from solapi.model.message import Message

message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)
message = Message(from_="등록한 발신번호", to="01000000000", text="Hello World!")
response = message_service.send(message)
print(response)
