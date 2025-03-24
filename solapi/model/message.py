from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from solapi.model import KakaoOption
from solapi.model.rcs.rcs_options import RcsOption


class MessageType(Enum):
    """
    메시지 유형(단문 문자, 장문 문자, 알림톡 등)
    SMS: 단문 문자
    LMS: 장문 문자
    MMS: 사진 문자
    ATA: 알림톡
    CTA: 친구톡
    CTI: 사진 한장이 포함된 친구톡
    NSA: 네이버 스마트알림(톡톡)
    RCS_SMS: RCS 단문 문자
    RCS_LMS: RCS 장문 문자
    RCS_MMS: RCS 사진 문자
    RCS_TPL: RCS 템플릿
    RCS_ITPL: RCS 이미지 템플릿
    RCS_LTPL: RCS LMS 템플릿 문자
    FAX: 팩스
    VOICE: 음성문자(TTS)
    """

    SMS = "SMS"
    LMS = "LMS"
    MMS = "MMS"
    ATA = "ATA"
    CTA = "CTA"
    CTI = "CTI"
    NSA = "NSA"
    RCS_SMS = "RCS_SMS"
    RCS_LMS = "RCS_LMS"
    RCS_MMS = "RCS_MMS"
    RCS_TPL = "RCS_TPL"
    RCS_ITPL = "RCS_ITPL"
    RCS_LTPL = "RCS_LTPL"
    FAX = "FAX"
    VOICE = "VOICE"

    def __str__(self) -> str:
        return self.value

    def __repr__(self):
        return repr(self.value)


class FileIdsType(BaseModel):
    file_ids: Optional[list[str]] = None


class Message(BaseModel):
    from_: Optional[str] = Field(
        default=None, serialization_alias="from", validation_alias="from"
    )
    to: str
    text: Optional[str] = None
    image_id: Optional[str] = Field(
        default=None, serialization_alias="imageId", validation_alias="imageId"
    )
    country: str = "82"
    message_id: Optional[str] = Field(
        default=None, serialization_alias="messageId", validation_alias="messageId"
    )
    group_id: Optional[str] = Field(
        default=None, serialization_alias="groupId", validation_alias="groupId"
    )
    type: Optional[MessageType] = None
    auto_type_detect: Optional[bool] = Field(
        default=True,
        serialization_alias="autoTypeDetect",
        validation_alias="autoTypeDetect",
    )
    subject: Optional[str] = None
    replacements: Optional[list[dict[str, Any]]] = None
    custom_fields: Optional[dict[str, str]] = Field(
        default=None,
        serialization_alias="customFields",
        validation_alias="customFields",
    )
    kakao_options: Optional[KakaoOption] = Field(
        default=None,
        serialization_alias="kakaoOptions",
        validation_alias="kakaoOptions",
    )
    rcs_options: Optional[RcsOption] = Field(
        default=None, serialization_alias="rcsOptions", validation_alias="rcsOptions"
    )
    fax_options: Optional[FileIdsType] = Field(
        default=None, serialization_alias="faxOptions", validation_alias="faxOptions"
    )
    date_created: Optional[datetime] = Field(
        default=None, serialization_alias="dateCreated", validation_alias="dateCreated"
    )
    date_updated: Optional[datetime] = Field(
        default=None, serialization_alias="dateUpdated", validation_alias="dateUpdated"
    )
    log: Optional[list[dict[str, Any]]] = None
    status_code: Optional[str] = Field(
        default=None, serialization_alias="statusCode", validation_alias="statusCode"
    )

    model_config = ConfigDict(
        extra="ignore",
        populate_by_name=True,
        alias_generator=to_camel,
    )
