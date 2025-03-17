from typing import Optional

from pydantic import BaseModel, Field

from solapi.model.response.common_response import GroupMessageResponse


class FailedMessage(BaseModel):
    to: str
    from_: str = Field(..., alias="from")
    type: str
    status_message: str = Field(..., alias="statusMessage")
    country: str
    message_id: str = Field(..., alias="messageId")
    status_code: str = Field(..., alias="statusCode")
    account_id: str = Field(..., alias="accountId")
    custom_fields: Optional[dict[str, str]] = Field(
        default=None, alias="customFields"
    )


class SendMessageResponse(BaseModel):
    failed_message_list: list[FailedMessage] = Field(
        ..., alias="failedMessageList"
    )
    group_info: GroupMessageResponse = Field(..., alias="groupInfo")
    message_list: Optional[list] = Field(default=None, alias="messageList")
