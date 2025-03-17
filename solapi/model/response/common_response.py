from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


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
    requested: int
    replacement: int
    refund: int
    sum: int

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
    # export type GroupMessageResponse = {
    #   count: Count;
    #   countForCharge: CountForCharge;
    #   balance: CommonCashResponse;
    #   point: CommonCashResponse;
    #   app: App;
    #   log: Log;
    #   status: string;
    #   allowDuplicates: boolean;
    #   isRefunded: boolean;
    #   accountId: string;
    #   masterAccountId: string | null;
    #   apiVersion: string;
    #   groupId: string;
    #   price: object;
    #   dateCreated: string;
    #   dateUpdated: string;
    #   scheduledDate?: string;
    #   dateSent?: string;
    #   dateCompleted?: string;
    # };
    count: CountResponse
    count_for_charge: Any = Field(..., validation_alias="countForCharge")
    balance: CommonCashResponse
    point: CommonCashResponse
    app: Any
    log: Any
    status: str
    allow_duplicates: bool = Field(..., validation_alias="allowDuplicates")
    is_refunded: bool = Field(..., validation_alias="isRefunded")
    account_id: str = Field(..., validation_alias="accountId")
    master_account_id: str = Field(..., validation_alias="masterAccountId")
    api_version: str = Field(..., validation_alias="apiVersion")
    group_id: str = Field(..., validation_alias="groupId")
    price: Any
    date_created: datetime = Field(..., validation_alias="dateCreated")
    date_updated: datetime = Field(..., validation_alias="dateUpdated")
    scheduled_date: datetime = Field(..., validation_alias="scheduledDate")
    date_sent: datetime = Field(..., validation_alias="dateSent")
    date_completed: datetime = Field(..., validation_alias="dateCompleted")

    model_config = ConfigDict(extra="ignore")
