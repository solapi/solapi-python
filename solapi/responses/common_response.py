from typing import Any, Optional

from pydantic import BaseModel, Field


class GroupMessageResponse(BaseModel):
    count: Any = Field(..., alias="count")
    count_for_charge: Any = Field(..., alias="countForCharge")
    balance: Any = Field(..., alias="balance")
    point: Any = Field(..., alias="point")
    app: Any = Field(..., alias="app")
    log: Any = Field(..., alias="log")
    status: str = Field(..., alias="status")
    allow_duplicates: bool = Field(..., alias="allowDuplicates")
    is_refunded: bool = Field(..., alias="isRefunded")
    account_id: str = Field(..., alias="accountId")
    master_account_id: Optional[str] = Field(None, alias="masterAccountId")
    api_version: str = Field(..., alias="apiVersion")
    group_id: str = Field(..., alias="groupId")
    price: dict[str, Any] = Field(..., alias="price")
    date_created: str = Field(..., alias="dateCreated")
    date_updated: str = Field(..., alias="dateUpdated")
    scheduled_date: Optional[str] = Field(None, alias="scheduledDate")
    date_sent: Optional[str] = Field(None, alias="dateSent")
    date_completed: Optional[str] = Field(None, alias="dateCompleted")

    class Config:
        populate_by_name = True

class Count(BaseModel):
    total: int = Field(..., alias="total")
    sent_total: int = Field(..., alias="sentTotal")
    sent_failed: int = Field(..., alias="sentFailed")
    sent_success: int = Field(..., alias="sentSuccess")
    sent_pending: int = Field(..., alias="sentPending")
    sent_replacement: int = Field(..., alias="sentReplacement")
    refund: int = Field(..., alias="refund")
    registered_failed: int = Field(..., alias="registeredFailed")
    registered_success: int = Field(..., alias="registeredSuccess")

    class Config:
        populate_by_name = True
