from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class CountResponse(BaseModel):
    total: int
    sent_total: int = Field(..., validation_alias="sentTotal")
    sent_success: int = Field(..., validation_alias="sentSuccess")
    sent_pending: int = Field(..., validation_alias="sentPending")
    sent_replacement: int = Field(..., validation_alias="sentReplacement")
    refund: int
    registered_failed: int = Field(..., validation_alias="registeredFailed")
    registered_success: int = Field(..., validation_alias="registeredSuccess")

    model_config = ConfigDict(extra="ignore")


class CommonCashResponse(BaseModel):
    requested: float
    replacement: float
    refund: float
    sum: float

    model_config = ConfigDict(extra="ignore")


class CountForChargeResponse(BaseModel):
    sms: dict[str, int]
    lms: dict[str, int]
    mms: dict[str, int]
    ata: dict[str, int]
    cta: dict[str, int]
    cti: dict[str, int]
    nsa: dict[str, int]
    rcs_sms: dict[str, int]
    rcs_lms: dict[str, int]
    rcs_mms: dict[str, int]
    rcs_tpl: dict[str, int]

    model_config = ConfigDict(extra="ignore")


class GroupMessageResponse(BaseModel):
    count: CountResponse
    count_for_charge: Any
    balance: CommonCashResponse
    point: CommonCashResponse
    app: Any
    log: Any
    status: str
    allow_duplicates: bool
    is_refunded: bool
    account_id: str
    master_account_id: Optional[str]
    api_version: str
    group_id: str
    price: Any
    date_created: Optional[datetime]
    date_updated: Optional[datetime]
    scheduled_date: Optional[datetime] = Field(default=None)
    date_sent: Optional[datetime]
    date_completed: Optional[datetime]

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="ignore",
    )
