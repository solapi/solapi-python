import platform
from typing import Optional

from pydantic import BaseModel, Field

from solapi.model.message import Message


class SendRequestConfig(BaseModel):
    app_id: Optional[str] = Field(default=None, serialization_alias="appId")
    allow_duplicates: bool = Field(default=False, serialization_alias="allowDuplicates")
    show_message_list: bool = Field(
        default=False, serialization_alias="showMessageList"
    )
    scheduled_date: Optional[str] = Field(
        default=None, serialization_alias="scheduledDate"
    )


class SendMessageRequest(BaseModel):
    messages: list[Message]
    scheduled_date: Optional[str] = Field(
        default=None, serialization_alias="scheduledDate"
    )
    show_message_list: Optional[bool] = Field(
        default=False, serialization_alias="showMessageList"
    )
    allow_duplicates: bool = Field(default=False, serialization_alias="allowDuplicates")
    app_id: Optional[str] = Field(default=None, serialization_alias="appId")

    # NOTE: Python SDK 버전 업데이트 할 때마다 변경해줘야 함
    agent: dict[str, str] = {
        "sdkVersion": "python/5.0.0",
        "osPlatform": f"{platform.platform()} | {platform.python_version()}",
    }
