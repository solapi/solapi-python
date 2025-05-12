from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CountResponse(BaseModel):
    total: int
    sent_total: int
    sent_success: int
    sent_pending: int
    sent_replacement: int
    refund: int
    registered_failed: int
    registered_success: int

    model_config = ConfigDict(
        extra="ignore", alias_generator=to_camel, populate_by_name=True
    )


class CommonCashResponse(BaseModel):
    requested: float
    replacement: float
    refund: float
    sum: float

    model_config = ConfigDict(extra="ignore")


class CommonPriceTypeResponse(BaseModel):
    sms: Optional[dict[str, float]] = None
    lms: Optional[dict[str, float]] = None
    mms: Optional[dict[str, float]] = None
    ata: Optional[dict[str, float]] = None
    cta: Optional[dict[str, float]] = None
    cti: Optional[dict[str, float]] = None
    nsa: Optional[dict[str, float]] = None
    rcs_sms: Optional[dict[str, float]] = None
    rcs_lms: Optional[dict[str, float]] = None
    rcs_mms: Optional[dict[str, float]] = None
    rcs_tpl: Optional[dict[str, float]] = None
    rcs_itpl: Optional[dict[str, float]] = None
    rcs_ltpl: Optional[dict[str, float]] = None
    fax: Optional[dict[str, float]] = None
    voice: Optional[dict[str, float]] = None

    model_config = ConfigDict(extra="ignore")


class EachTypePriceResponse(BaseModel):
    sms: Optional[float] = None
    lms: Optional[float] = None
    mms: Optional[float] = None
    ata: Optional[float] = None
    cta: Optional[float] = None
    cti: Optional[float] = None
    nsa: Optional[float] = None
    rcs_sms: Optional[float] = None
    rcs_lms: Optional[float] = None
    rcs_mms: Optional[float] = None
    rcs_tpl: Optional[float] = None
    rcs_itpl: Optional[float] = None
    rcs_ltpl: Optional[float] = None
    fax: Optional[float] = None
    voice: Optional[float] = None

    model_config = ConfigDict(extra="ignore")


class AppResponse(BaseModel):
    profit: Optional[EachTypePriceResponse] = None
    app_id: Optional[str] = None

    model_config = ConfigDict(
        extra="ignore", alias_generator=to_camel, populate_by_name=True
    )


class GroupMessageResponse(BaseModel):
    count: CountResponse
    count_for_charge: CommonPriceTypeResponse
    balance: CommonCashResponse
    point: CommonCashResponse
    app: AppResponse
    log: list[dict[str, Any]]
    status: str
    allow_duplicates: bool
    is_refunded: bool
    account_id: str
    master_account_id: Optional[str]
    api_version: str
    group_id: str
    price: dict[str, EachTypePriceResponse]
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
