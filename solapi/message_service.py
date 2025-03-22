import base64
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

from solapi.error.MessageNotReceiveError import MessageNotReceivedError
from solapi.lib.authenticator import AuthenticationParameter
from solapi.lib.fetcher import RequestMethod, default_fetcher
from solapi.lib.string_date_transfer import format_with_transfer
from solapi.model.message import Message
from solapi.model.request.send_message_request import (
    SendMessageRequest,
    SendRequestConfig,
)
from solapi.model.request.storage import FileTypeEnum, FileUploadRequest
from solapi.model.response.send_message_response import SendMessageResponse
from solapi.model.response.storage import FileUploadResponse


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

            if request_config.scheduled_date is not None and (
                request_config.scheduled_date != ""
                or isinstance(request_config.scheduled_date, datetime)
            ):
                request.scheduled_date = format_with_transfer(
                    request_config.scheduled_date
                )

        print(request.model_dump(exclude_none=True, by_alias=True))
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
            raise MessageNotReceivedError(failed_messages) from ValueError

        return deserialized_response

    def upload_file(
        self, file_path: str, upload_type: FileTypeEnum = FileTypeEnum.MMS
    ) -> FileUploadResponse:
        path = Path(file_path)
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        request = FileUploadRequest(
            file=str(encoded_string)[2:-1],
            type=upload_type,
        ).model_dump(exclude_none=True)
        response = default_fetcher(
            self.auth_info,
            request={
                "url": f"{self.base_url}/storage/v1/files",
                "method": RequestMethod.POST,
            },
            data=request,
        )
        deserialized_response: FileUploadResponse = FileUploadResponse.model_validate(
            response
        )
        return deserialized_response

    # TODO: 조회 기능들 개발해야 함
    def get_groups(self):
        return ""

    def get_group(self, group_id: str):
        return group_id

    def get_group_messages(self, group_id: str):
        return group_id

    def get_messages(self):
        return ""

    def get_message(self, message_id: str):
        return message_id

    def get_naver_templates(self):
        return ""

    def get_balance(self):
        return ""
