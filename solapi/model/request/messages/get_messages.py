from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel

from solapi.lib.string_date_transfer import format_with_transfer
from solapi.model.message_type import MessageType


class GetMessagesRequest(BaseModel):
    start_key: Optional[str] = None
    limit: Optional[int] = 20
    message_id: Optional[str] = None
    message_ids: Optional[list[str]] = None
    group_id: Optional[str] = None
    from_: Optional[str] = Field(default=None, serialization_alias="from")
    to: Optional[str] = None
    type: Optional[MessageType] = None
    status_code: Optional[str] = None
    date_type: Optional[str] = "CREATED"  # or "UPDATED"
    start_date: Optional[Union[str, datetime]] = None
    end_date: Optional[Union[str, datetime]] = None

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def format_dates(
        cls, value: Union[str, datetime, None]
    ) -> Union[str, datetime, None]:
        if isinstance(value, str):
            return format_with_transfer(value)
        return value
