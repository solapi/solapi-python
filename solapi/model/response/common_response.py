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
    sms: dict[str, float]
    lms: dict[str, float]
    mms: dict[str, float]
    ata: dict[str, float]
    cta: dict[str, float]
    cti: dict[str, float]
    nsa: dict[str, float]
    rcs_sms: dict[str, float]
    rcs_lms: dict[str, float]
    rcs_mms: dict[str, float]
    rcs_tpl: dict[str, float]

    model_config = ConfigDict(extra="ignore")


class AppResponse(BaseModel):
    profit: CountForChargeResponse
    app_id: Optional[str] = None

    model_config = ConfigDict(
        extra="ignore", alias_generator=to_camel, populate_by_name=True
    )


class GroupMessageResponse(BaseModel):
    count: CountResponse
    count_for_charge: CountForChargeResponse
    balance: CommonCashResponse
    point: CommonCashResponse
    app: AppResponse
    log: list[dict[str, str]]
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
    scheduled_date: Optional[datetime] = None
    date_sent: Optional[datetime] = None
    date_completed: Optional[datetime] = None

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="ignore",
    )
