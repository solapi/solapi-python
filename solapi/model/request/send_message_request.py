import platform
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from solapi.model.message import Message


class SendRequestConfig(BaseModel):
    app_id: Optional[str] = None
    allow_duplicates: bool = False
    show_message_list: bool = False
    scheduled_date: Optional[Union[str, datetime]] = None

    model_config = ConfigDict(
        alias_generator=to_camel, extra="ignore", populate_by_name=True
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
