from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from solapi.model.response.common_response import GroupMessageResponse


class MessageItem(BaseModel):
    message_id: str
    status_code: str
    status_message: str
    custom_fields: Optional[dict[str, str]] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class FailedMessage(BaseModel):
    to: Optional[str]
    from_: Optional[str] = Field(
        ..., serialization_alias="from", validation_alias="from"
    )
    type: str
    status_message: str = Field(..., alias="statusMessage")
    country: Optional[str]
    message_id: str = Field(..., alias="messageId")
    status_code: str = Field(..., alias="statusCode")
    account_id: str = Field(..., alias="accountId")
    custom_fields: Optional[dict[str, str]] = Field(default=None, alias="customFields")

    model_config = ConfigDict(extra="ignore", populate_by_name=True)


class SendMessageResponse(BaseModel):
    failed_message_list: Optional[list[FailedMessage]] = None
    group_info: GroupMessageResponse
    message_list: Optional[list[MessageItem]] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
