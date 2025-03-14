import platform
from typing import Any, TypedDict, Union

from solapi.model.message import Message, MessageType


class MessageParameterRequired(TypedDict):
    to: Union[str, list[str]]


MessageParameterNonRequired = TypedDict(
    "MessageParameterNonRequired",
    {
        "from": str,
        "text": str,
        "imageId": str,
        "type": MessageType,
        "subject": str,
        "autoTypeDetect": bool,
        "kakaoOptions": dict[str, Any],
        "rcsOptions": dict[str, Any],
        "country": str,
        "customFields": dict[str, str],
        "replacements": list[object],
        "faxOptions": dict[str, Any],
    },
    total=False,
)


class SdkInfo(TypedDict):
    sdkVersion: str
    osPlatform: str


class AppId(TypedDict, total=False):
    appId: str


class DefaultAgentType(SdkInfo, AppId):
    pass


# 필요한 타입 정의 (실제 환경에 맞게 구체화 가능)
RcsOptionRequest = dict[str, Any]
FileIds = dict[str, Any]


class KakaoOptionRequest(TypedDict):
    pass


class MessageParameter(MessageParameterRequired, MessageParameterNonRequired):
    pass


class DefaultMessageRequest(TypedDict):
    allowDuplicates: bool
    agent: DefaultAgentType


default_agent: DefaultAgentType = {
    "sdkVersion": "python/5.0.0",
    "osPlatform": f"{platform.platform()} | {platform.python_version()}",
}


class ScheduledDateType(TypedDict, total=False):
    scheduledDate: str


class ShowMessageListType(TypedDict, total=False):
    showMessageList: bool


class MultipleDetailMessageSendingRequest(
    TypedDict, DefaultMessageRequest, AppId, ShowMessageListType
):
    messages: list[Message]
