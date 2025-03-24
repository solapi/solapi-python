from solapi.model.response.send_message_response import FailedMessage


class MessageNotReceivedError(Exception):
    def __init__(self, failed_messages: list[FailedMessage]):
        self.failed_messages = failed_messages

    def __str__(self):
        # TODO: i18n needed
        return "메시지 접수에 실패했습니다.\n자세한 내용은 MessageNotReceivedError의 failed_messages 프로퍼티를 참조해 주세요."
