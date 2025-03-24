from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from solapi.model import Message


class GetMessagesResponse(BaseModel):
    limit: int
    message_list: dict[str, Message]
    start_key: Optional[str] = None
    next_key: Optional[str] = None

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, extra="ignore"
    )
