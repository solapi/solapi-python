from datetime import datetime
from typing import Optional, Union

from solapi.lib.authenticator import AuthenticationParameter
from solapi.lib.fetcher import RequestMethod, default_fetcher
from solapi.lib.string_date_transfer import format_with_transfer
from solapi.model.message import Message
from solapi.model.request.send_message_request import (
    SendMessageRequest,
    SendRequestConfig,
)
from solapi.model.response.send_message_response import SendMessageResponse


class SolapiMessageService:
    def __init__(self, api_key: str, api_secret: str):
        self.base_url = "https://api.solapi.com"
        self.auth_info: AuthenticationParameter = {
            "api_key": api_key,
            "api_secret": api_secret,
        }

    def send(
        self,
        messages: Union[list[Message], Message],
        request_config: Optional[SendRequestConfig] = None,
    ) -> SendMessageResponse:
        payload = []
        if isinstance(messages, Message):
            payload.append(messages)
        elif isinstance(messages, list):
            for message in messages:
                if isinstance(message, Message) is not True:
                    raise TypeError(
                        "The messages parameter must be an instance of Message."
                    )

            payload.extend(messages)
        else:
            raise TypeError("Invalid message type")

        if len(payload) == 0:
            raise ValueError("The data must have at least one message.")

        request = SendMessageRequest(messages=payload)
        if request_config is not None:
            request.app_id = request_config.app_id
            request.allow_duplicates = request_config.allow_duplicates
            request.show_message_list = request_config.show_message_list

            if (
                request_config.scheduled_date is not None
                and request_config.scheduled_date != ""
                and isinstance(request_config.scheduled_date, datetime)
            ):
                request.scheduled_date = format_with_transfer(
                    request_config.scheduled_date
                )

        response = default_fetcher(
            self.auth_info,
            request={
                "method": RequestMethod.POST,
                "url": f"{self.base_url}/messages/v4/send-many/detail",
            },
            data=request.model_dump(exclude_none=True, by_alias=True),
        )
        deserialized_response: SendMessageResponse = SendMessageResponse.model_validate(
            response
        )

        count = deserialized_response.group_info.count
        failed_messages = deserialized_response.failed_message_list
        registered_failed_count = count.registered_failed
        if len(failed_messages) > 0 and count.total == registered_failed_count:
            raise ValueError("an error occurred")

        return deserialized_response
