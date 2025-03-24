import platform
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from solapi.model.message import Message
from solapi.model.request import VERSION


class SendRequestConfig(BaseModel):
    app_id: Optional[str] = None
    allow_duplicates: bool = False
    show_message_list: bool = False
    scheduled_date: Optional[Union[str, datetime]] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class SendMessageRequest(BaseModel):
    messages: list[Message]
    scheduled_date: Optional[str] = None
    show_message_list: Optional[bool] = None
    allow_duplicates: bool = False
    app_id: Optional[str] = None

    agent: dict[str, str] = {
        "sdkVersion": VERSION,
        "osPlatform": f"{platform.platform()} | {platform.python_version()}",
    }

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
