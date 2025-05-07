import base64
from datetime import datetime
from pathlib import Path
from typing import Optional, Union
from urllib.parse import urlencode

from solapi.error.MessageNotReceiveError import MessageNotReceivedError
from solapi.lib.authenticator import AuthenticationParameter
from solapi.lib.fetcher import RequestMethod, default_fetcher
from solapi.lib.string_date_transfer import format_with_transfer
from solapi.model.request.groups.get_groups import (
    GetGroupsCrteriaType,
    GetGroupsFinalizeRequest,
    GetGroupsRequest,
)
from solapi.model.request.message import Message as RequestMessage
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
    """Solapi Message Service for handling message-related operations.

    This class provides methods to interact with the Solapi API for sending various types of messages
    (SMS, LMS, MMS, 알림톡, 친구톡, RCS, etc.), managing message groups, uploading files,
    and checking account balance.
    """

    def __init__(self, api_key: str, api_secret: str):
        """Initialize the Solapi Message Service.

        Args:
            api_key: The API key for authentication.
            api_secret: The API secret for authentication.
        """
        self.base_url = "https://api.solapi.com"
        self.auth_info: AuthenticationParameter = {
            "api_key": api_key,
            "api_secret": api_secret,
        }

    def send(
        self,
        messages: Union[list[RequestMessage], RequestMessage],
        request_config: Optional[SendRequestConfig] = None,
    ) -> SendMessageResponse:
        """Send one or more messages using the Solapi API.

        This method sends various types of messages (SMS, LMS, MMS, 알림톡, 친구톡, RCS, etc.) to recipients.
        It supports sending a single message or multiple messages in one request (대량 발송).

        Args:
            messages: A single RequestMessage object or a list of RequestMessage objects to send.
                      Each RequestMessage object contains recipient (수신번호), sender (발신번호), content (내용),
                      and other message details.
            request_config: Optional configuration for the send request.
                           Can include app_id, allow_duplicates (중복 수신번호 허용),
                           scheduled_date (예약 발송), and other settings.

        Returns:
            SendMessageResponse: The response from the API containing message status, group info,
                               and other details about the sent messages.

        Raises:
            TypeError: If messages parameter is not a RequestMessage object or list of RequestMessage objects.
            ValueError: If no valid messages are provided.
            MessageNotReceivedError: If all messages failed to be registered.
        """
        payload = []
        if isinstance(messages, RequestMessage):
            payload.append(messages)
        elif isinstance(messages, list):
            for message in messages:
                if isinstance(message, RequestMessage) is not True:
                    raise TypeError(
                        "The messages parameter must be an instance of RequestMessage."
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
        """Upload a file to the Solapi storage service.

        This method uploads a file (such as an image) to be used in MMS (사진 문자) or other message types.
        The file is encoded in base64 before being sent to the API.

        Args:
            file_path: The path to the file to be uploaded (파일 경로).
            upload_type: The type of file being uploaded, defaults to MMS (사진 문자용).
                        Other possible values are defined in FileTypeEnum.

        Returns:
            FileUploadResponse: The response from the API containing the file ID (파일 ID) and other details.

        Raises:
            FileNotFoundError: If the specified file path does not exist.
        """
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
        """Retrieve message groups (메시지 그룹) from the Solapi API.

        This method fetches message groups based on the provided query parameters.
        If no query is provided, it returns all message groups.
        메시지 그룹은 대량 발송 시 생성되는 메시지들의 묶음입니다.

        Args:
            query: Optional query parameters to filter the groups.
                  Can include group_id (그룹 ID), criteria, cond, value, and other filters.

        Returns:
            GetGroupsResponse: The response from the API containing the list of message groups
                             and other metadata.
        """
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
        """Retrieve a specific message group (메시지 그룹) by its ID.

        This method fetches detailed information about a single message group.
        특정 그룹 ID로 메시지 그룹 정보를 조회합니다.

        Args:
            group_id: The unique identifier (그룹 ID) of the message group to retrieve.

        Returns:
            GroupMessageResponse: The response from the API containing the message group details.
        """
        response = default_fetcher(
            self.auth_info,
            request={
                "url": f"{self.base_url}/messages/v4/groups/{group_id}",
                "method": RequestMethod.GET,
            },
        )
        return GroupMessageResponse.model_validate(response)

    def get_group_messages(self, group_id: str) -> GetGroupMessagesResponse:
        """Retrieve all messages within a specific group (그룹 내 메시지 목록 조회).

        This method fetches all messages that belong to the specified message group.
        특정 메시지 그룹에 속한 모든 메시지를 조회합니다.

        Args:
            group_id: The unique identifier (그룹 ID) of the message group whose messages should be retrieved.

        Returns:
            GetGroupMessagesResponse: The response from the API containing the list of messages
                                    in the group and other metadata.
        """
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
        """Retrieve messages based on query parameters (메시지 목록 조회).

        This method fetches messages that match the specified query parameters.
        If no query is provided, it returns messages based on default parameters.
        조건에 맞는 메시지 목록을 조회합니다.

        Args:
            query: Optional query parameters to filter the messages.
                  Can include criteria for message status (상태), date range (기간),
                  recipient (수신번호), sender (발신번호), etc.

        Returns:
            GetMessagesResponse: The response from the API containing the list of messages
                               and other metadata.
        """
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
        """Retrieve the account balance information (잔액 조회).

        This method fetches the current balance and point information for the account.
        계정의 현재 잔액과 포인트 정보를 조회합니다.

        Returns:
            GetBalanceResponse: The response from the API containing the account balance details
                               including cash balance (잔액) and point balance (포인트).
        """
        response = default_fetcher(
            self.auth_info,
            request={
                "url": f"{self.base_url}/cash/v1/balance",
                "method": RequestMethod.GET,
            },
        )
        return GetBalanceResponse.model_validate(response)
