from typing import Optional, Union

from solapi.lib.authenticator import AuthenticationParameter
from solapi.lib.fetcher import RequestMethod, default_fetcher
from solapi.lib.string_date_transfer import format_with_transfer
from solapi.model.message import Message
from solapi.model.request.send_message_request import (
    SendMessageRequest,
    SendRequestConfig,
)


class SolapiMessageService:
    def __init__(self, api_key: str, api_secret: str):
        self.baseUrl = "https://api.solapi.com"
        self._auth_info: AuthenticationParameter = {
            "api_key": api_key,
            "api_secret": api_secret,
        }

    def send(
        self,
        messages: Union[list[Message], Message],
        request_config: Optional[SendRequestConfig] = None,
    ):
        payload = []
        if isinstance(messages, Message):
            payload.append(messages)
        elif isinstance(messages, list):
            payload.extend(messages)

        if len(payload) == 0:
            raise ValueError("데이터가 반드시 1건 이상 기입되어 있어야 합니다.")

        request = SendMessageRequest(messages=payload)
        if request_config is not None:
            request.app_id = request_config["app_id"]
            request.allow_duplicates = request_config["allow_duplicates"]
            request.show_message_list = request_config["show_message_list"]

            if request_config.scheduled_date != "":
                request.scheduled_date = format_with_transfer(
                    request_config.scheduled_date
                )

        print(request.model_dump(exclude_none=True, by_alias=True))

        return default_fetcher(
            self._auth_info,
            request={
                "method": RequestMethod.POST,
                "url": f"{self.baseUrl}/messages/v4/send-many/detail",
            },
            data=request.model_dump(exclude_none=True, by_alias=True),
        )
