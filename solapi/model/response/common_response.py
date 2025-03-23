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
    rcs_itpl: dict[str, float]
    rcs_ltpl: dict[str, float]
    fax: dict[str, float]
    voice: dict[str, float]

    model_config = ConfigDict(extra="ignore")


class EachTypePriceResponse(BaseModel):
    sms: float
    lms: float
    mms: float
    ata: float
    cta: float
    cti: float
    nsa: float
    rcs_sms: float
    rcs_lms: float
    rcs_mms: float
    rcs_tpl: float
    rcs_itpl: float
    rcs_ltpl: float
    fax: float
    voice: float

    model_config = ConfigDict(extra="ignore")


class AppResponse(BaseModel):
    profit: EachTypePriceResponse
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
