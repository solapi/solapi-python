import base64
from datetime import datetime
from pathlib import Path
from typing import Optional, Union
from urllib.parse import urlencode

from solapi.error.MessageNotReceiveError import MessageNotReceivedError
from solapi.lib.authenticator import AuthenticationParameter
from solapi.lib.fetcher import RequestMethod, default_fetcher
from solapi.lib.string_date_transfer import format_with_transfer
from solapi.model.message import Message
from solapi.model.request.groups.get_groups import (
    GetGroupsCrteriaType,
    GetGroupsFinalizeRequest,
    GetGroupsRequest,
)
from solapi.model.request.messages.get_messages import GetMessagesRequest
from solapi.model.request.send_message_request import (
    SendMessageRequest,
    SendRequestConfig,
)
from solapi.model.request.storage import FileTypeEnum, FileUploadRequest
from solapi.model.response.balance.get_balance import GetBalanceResponse
from solapi.model.response.common_response import GroupMessageResponse
from solapi.model.response.groups.get_group_messages import GetGroupMessagesResponse
from solapi.model.response.groups.get_groups import GetGroupsResponse
from solapi.model.response.messages.get_messages import GetMessagesResponse
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
        if (
            failed_messages is not None
            and len(failed_messages) > 0
            and count.total == registered_failed_count
        ):
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
        return FileUploadResponse.model_validate(response)

    def get_groups(self, query: Optional[GetGroupsRequest] = None) -> GetGroupsResponse:
        request = GetGroupsFinalizeRequest()
        if query is not None:
            request = request.model_copy(update=query.model_dump(exclude_unset=True))
            if query.group_id is not None and query.group_id != "":
                request.criteria = GetGroupsCrteriaType.group_id
                request.cond = "eq"
                request.value = query.group_id

        encoded_request = urlencode(request.model_dump(exclude_none=True))
        if encoded_request != "":
            encoded_request = "?" + encoded_request

        response = default_fetcher(
            self.auth_info,
            request={
                "url": f"{self.base_url}/messages/v4/groups{encoded_request}",
                "method": RequestMethod.GET,
            },
        )
        return GetGroupsResponse.model_validate(response)

    def get_group(self, group_id: str) -> GroupMessageResponse:
        response = default_fetcher(
            self.auth_info,
            request={
                "url": f"{self.base_url}/messages/v4/groups/{group_id}",
                "method": RequestMethod.GET,
            },
        )
        return GroupMessageResponse.model_validate(response)

    def get_group_messages(self, group_id: str) -> GetGroupMessagesResponse:
        response = default_fetcher(
            self.auth_info,
            request={
                "url": f"{self.base_url}/messages/v4/groups/{group_id}/messages",
                "method": RequestMethod.GET,
            },
        )
        return GetGroupMessagesResponse.model_validate(response)

    def get_messages(
        self, query: Optional[GetMessagesRequest] = None
    ) -> GetMessagesResponse:
        request = GetMessagesRequest()
        if query is not None:
            request = request.model_copy(update=query.model_dump(exclude_unset=True))

        encoded_request = urlencode(
            request.model_dump(exclude_none=True, by_alias=True)
        )
        if encoded_request != "":
            encoded_request = "?" + encoded_request

        response = default_fetcher(
            self.auth_info,
            request={
                "url": f"{self.base_url}/messages/v4/list-old{encoded_request}",
                "method": RequestMethod.GET,
            },
        )
        return GetMessagesResponse.model_validate(response)

    def get_balance(self) -> GetBalanceResponse:
        response = default_fetcher(
            self.auth_info,
            request={
                "url": f"{self.base_url}/cash/v1/balance",
                "method": RequestMethod.GET,
            },
        )
        return GetBalanceResponse.model_validate(response)
