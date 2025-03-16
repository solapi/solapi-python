
from solapi.message_service import SolapiMessageService
from solapi.model.message import Message

test = SolapiMessageService(api_key="", api_secret="")
test2 = Message(
    from_="029302266",
    to="01012345678",
    text="test"
)
test.send(test2)
