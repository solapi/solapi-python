from typing import Optional

from pydantic import BaseModel, Field

from solapi.responses.common_response import GroupMessageResponse


class FailedMessage(BaseModel):
    to: str = Field(..., alias="to")
    # 'from'는 예약어이므로 내부 변수는 from_로 사용하고, alias로 "from"을 매핑합니다.
    from_: str = Field(..., alias="from")
    type: str = Field(..., alias="type")
    status_message: str = Field(..., alias="statusMessage")
    country: str = Field(..., alias="country")
    message_id: str = Field(..., alias="messageId")
    status_code: str = Field(..., alias="statusCode")
    account_id: str = Field(..., alias="accountId")
    custom_fields: Optional[dict[str, str]] = Field(None, alias="customFields")

    class Config:
        allow_population_by_field_name = True


class MessageResponseItem(BaseModel):
    message_id: str = Field(..., alias="messageId")
    status_code: str = Field(..., alias="statusCode")
    custom_fields: Optional[dict[str, str]] = Field(None, alias="customFields")
    status_message: str = Field(..., alias="statusMessage")

    class Config:
        allow_population_by_field_name = True


class DetailGroupMessageResponse(BaseModel):
    failed_message_list: list[FailedMessage] = Field(..., alias="failedMessageList")
    group_info: GroupMessageResponse = Field(..., alias="groupInfo")
    message_list: Optional[list[MessageResponseItem]] = Field(None, alias="messageList")

    class Config:
        allow_population_by_field_name = True
