from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel

from solapi.model import KakaoOption
from solapi.model.message_type import MessageType
from solapi.model.rcs.rcs_options import RcsOption
from solapi.model.request.voice.voice_option import VoiceOption


class FileIdsType(BaseModel):
    file_ids: Optional[list[str]] = None


class Message(BaseModel):
    from_: Optional[str] = Field(
        default=None, serialization_alias="from", validation_alias="from"
    )
    to: Union[str, list[str]]
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
    voice_options: Optional[VoiceOption] = Field(
        default=None,
        serialization_alias="voiceOptions",
        validation_alias="voiceOptions",
    )

    @field_validator("from_", mode="before")
    @classmethod
    def normalize_from_phone_number(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return v.replace("-", "")

    @field_validator("to", mode="before")
    @classmethod
    def normalize_to_phone_number(
        cls, v: Union[str, list[str]]
    ) -> Union[str, list[str]]:
        if isinstance(v, str):
            return v.replace("-", "")
        elif isinstance(v, list):
            return [phone.replace("-", "") for phone in v]
        return v

    model_config = ConfigDict(
        extra="ignore",
        populate_by_name=True,
        alias_generator=to_camel,
    )
