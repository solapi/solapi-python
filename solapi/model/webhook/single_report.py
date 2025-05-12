from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel
from pydantic.alias_generators import to_camel

from solapi.model.kakao.kakao_option import KakaoOption
from solapi.model.naver.naver_option import NaverOption
from solapi.model.rcs.rcs_options import RcsOption


class SingleReportData(BaseModel):
    message_id: Optional[str] = Field(
        default=None, validation_alias="messageId", serialization_alias="messageId"
    )
    group_id: Optional[str] = Field(
        default=None, validation_alias="groupId", serialization_alias="groupId"
    )
    type: Optional[str] = None
    to: Optional[str] = None
    from_: Optional[str] = Field(
        default=None, validation_alias="from", serialization_alias="from"
    )
    status_code: Optional[str] = Field(
        default=None, validation_alias="statusCode", serialization_alias="statusCode"
    )
    date_processed: Optional[str] = Field(
        default=None,
        validation_alias="dateProcessed",
        serialization_alias="dateProcessed",
    )
    date_reported: Optional[str] = Field(
        default=None,
        validation_alias="dateReported",
        serialization_alias="dateReported",
    )
    date_received: Optional[str] = Field(
        default=None,
        validation_alias="dateReceived",
        serialization_alias="dateReceived",
    )
    network_code: Optional[str] = Field(
        default=None, validation_alias="networkCode", serialization_alias="networkCode"
    )
    kakao_options: Optional[KakaoOption] = Field(
        default=None,
        validation_alias="kakaoOptions",
        serialization_alias="kakaoOptions",
    )
    rcs_options: Optional[RcsOption] = Field(
        default=None, validation_alias="rcsOptions", serialization_alias="rcsOptions"
    )
    naver_options: Optional[NaverOption] = Field(
        default=None,
        validation_alias="naverOptions",
        serialization_alias="naverOptions",
    )
    custom_fields: Optional[dict] = Field(
        default={}, validation_alias="customFields", serialization_alias="customFields"
    )
    status_message: Optional[str] = Field(
        default=None,
        validation_alias="statusMessage",
        serialization_alias="statusMessage",
    )

    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class SingleReport(BaseModel):
    event_data_id: str = None
    data: SingleReportData
    retry_count: Optional[int] = None

    model_config = ConfigDict(
        populate_by_name=True, alias_generator=to_camel, extra="ignore"
    )


class SingleReportPayload(RootModel[list[SingleReport]]):
    pass
