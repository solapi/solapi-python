from typing import Optional

from solapi.lib.authenticator import AuthenticationParameter
from solapi.lib.fetcher import RequestMethod, default_fetcher
from solapi.lib.string_date_transfer import format_with_transfer
from solapi.requests.request_confiog import SendRequestConfig
from solapi.requests.send.send_request import (
    MessageParameter,
    MultipleDetailMessageSendingRequest,
)
from solapi.responses.send.send_repsonse import DetailGroupMessageResponse


class SolapiMessageService:
    def __init__(self, api_key: str, api_secret: str):
        self.baseUrl = "https://api.solapi.com"
        self._auth_info: AuthenticationParameter = {
            "api_key": api_key,
            "api_secret": api_secret,
        }

    # TODO: Request도 pydantic 모델로 진행
    async def send(
        self,
        messages: list[MessageParameter] | MessageParameter,
        request_config: Optional[SendRequestConfig] = None,
    ):
        payload = []
        if isinstance(messages, list):
            for value in messages:
                payload.append(value)
        else:
            payload.append(messages)
        pass

        if len(payload) == 0:
            raise Exception("데이터가 반드시 1건 이상 기입되어 있어야 합니다.")

        parameter: MultipleDetailMessageSendingRequest = {"messages": payload}
        if request_config["appId"] is not None:
            parameter.appId = request_config["appId"]
        if request_config["showMessageList"] is not None:
            parameter.showMessageList = request_config["showMessageList"]
        if request_config["scheduledDate"] is not None:
            parameter.scheduledDate = format_with_transfer(
                request_config["scheduledDate"]
            )

        response = await default_fetcher(
            self._auth_info,
            {
                "method": RequestMethod("POST"),
                "url": f"${self.baseUrl}/messages/v4/send-many/detail",
            },
            parameter,
        )
        validated_response = DetailGroupMessageResponse.model_validate(response)
        count = validated_response.group_info.count
        if (
            len(validated_response.failed_message_list) > 0
            and count.total == count.registeredFailed
        ):
            raise Exception("")

        return validated_response

