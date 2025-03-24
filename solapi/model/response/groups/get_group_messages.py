from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from solapi.model import Message


class GetGroupMessagesResponse(BaseModel):
    start_key: Optional[str] = None
    next_key: Optional[str] = None
    limit: int
    message_list: dict[str, Message] = {}

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, extra="ignore"
    )
