from solapi.message_service import SolapiMessageService
from solapi.model.message import Message

test = SolapiMessageService(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
test2 = Message(from_="01012345678", to="01012345678", text="test")
test.send(test2)
