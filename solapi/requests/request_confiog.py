from datetime import datetime
from typing import TypedDict


class SendRequestConfig(TypedDict, total=False):
    # 예약일시
    scheduledDate: str | datetime

    # 중복 수신번호 허용 여부
    # 값 미기입시 중복 수신번호 비허용이 기본값으로 설정됩니다.
    allowDuplicates: bool

    # 특정 solapi app을 통해 발송 시 넣어줘야 할 app ID 값
    appId: str

    # send 메소드를 통해 발송 시 response에 messageList 값을 표시할 지에 대한 여부
    # 값 미기입시 기본값으로 비표시로 설정됩니다.
    showMessageList: bool
