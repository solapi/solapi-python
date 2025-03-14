from datetime import datetime
from enum import Enum
from typing import Any, Optional, TypedDict, Union

from pydantic import BaseModel, Field


# 외부 파일 import 대신 타입 정의
class KakaoOption:
    def __init__(self, options: dict[str, Any] = None):
        self.options = options or {}


class RcsOption:
    def __init__(self, options: dict[str, Any] = None):
        self.options = options or {}


class FileIds(TypedDict):
    fileIds: list[str]


class MessageType(str, Enum):
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


# TODO: 생성자 만들 때 Request 딕셔너리가 아니라 Response 딕셔너리로 받아와야함.
class Message(BaseModel):
    _to: str
    from__: Optional[str] = Field(None, alias="from")
    _text: Optional[str] = None
    _date_created: Optional[datetime] = None
    _date_updated: Optional[datetime] = None
    _group_id: Optional[str] = None
    _message_id: Optional[str] = None
    _image_id: Optional[str] = None
    _log: Optional[str] = None
    _type: Optional[str] = None
    _subject: Optional[str] = None
    # TODO: kakao options, rcs options 타이핑 해야 함
    _kakao_options: Optional[dict[str, Any]] = None
    _rcs_options: Optional[dict[str, Any]] = None
    _country: Optional[str] = None
    _auto_type_detect: Optional[bool] = None
    _status_code: Optional[str] = None
    _replacements: Optional[dict[str, Any]] = None
    _custom_fields: Optional[dict[str, Any]] = None
    _fax_options: Optional[dict[str, Any]] = None


    @property
    def to(self) -> Union[str, list[str]]:
        return self._to

    @to.setter
    def to(self, value: Union[str, list[str]]) -> None:
        self._to = value

    @property
    def from_(self) -> Optional[str]:
        return self.__dict__.get("from")

    @from_.setter
    def from_(self, value: Optional[str]) -> None:
        self.from__ = value

    @property
    def text(self) -> Optional[str]:
        return self._text

    @text.setter
    def text(self, value: Optional[str]) -> None:
        self._text = value

    @property
    def date_created(self) -> Optional[str]:
        return self._date_created

    @date_created.setter
    def date_created(self, value: Optional[str]) -> None:
        self._date_created = value

    @property
    def date_updated(self) -> Optional[str]:
        return self._date_updated

    @date_updated.setter
    def date_updated(self, value: Optional[str]) -> None:
        self._date_updated = value

    @property
    def group_id(self) -> Optional[str]:
        return self._group_id

    @group_id.setter
    def group_id(self, value: Optional[str]) -> None:
        self._group_id = value

    @property
    def message_id(self) -> Optional[str]:
        return self._message_id

    @message_id.setter
    def message_id(self, value: Optional[str]) -> None:
        self._message_id = value

    @property
    def image_id(self) -> Optional[str]:
        return self._image_id

    @image_id.setter
    def image_id(self, value: Optional[str]) -> None:
        self._image_id = value

    @property
    def type(self) -> Optional[MessageType]:
        return self._type

    @type.setter
    def type(self, value: Optional[MessageType]) -> None:
        self._type = value

    @property
    def subject(self) -> Optional[str]:
        return self._subject

    @subject.setter
    def subject(self, value: Optional[str]) -> None:
        self._subject = value

    @property
    def auto_type_detect(self) -> Optional[bool]:
        return self._auto_type_detect

    @auto_type_detect.setter
    def auto_type_detect(self, value: Optional[bool]) -> None:
        self._auto_type_detect = value

    @property
    def kakao_options(self) -> Optional[KakaoOption]:
        return self._kakao_options

    @kakao_options.setter
    def kakao_options(self, value: Optional[KakaoOption]) -> None:
        self._kakao_options = value

    @property
    def rcs_options(self) -> Optional[RcsOption]:
        return self._rcs_options

    @rcs_options.setter
    def rcs_options(self, value: Optional[RcsOption]) -> None:
        self._rcs_options = value

    @property
    def country(self) -> Optional[str]:
        return self._country

    @country.setter
    def country(self, value: Optional[str]) -> None:
        self._country = value

    @property
    def log(self) -> Optional[list[dict[str, Any]]]:
        return self._log

    @log.setter
    def log(self, value: Optional[list[dict[str, Any]]]) -> None:
        self._log = value

    @property
    def replacements(self) -> Optional[list[dict[str, Any]]]:
        return self._replacements

    @replacements.setter
    def replacements(self, value: Optional[list[dict[str, Any]]]) -> None:
        self._replacements = value

    @property
    def status_code(self) -> Optional[str]:
        return self._status_code

    @status_code.setter
    def status_code(self, value: Optional[str]) -> None:
        self._status_code = value

    @property
    def custom_fields(self) -> Optional[dict[str, str]]:
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, value: Optional[dict[str, str]]) -> None:
        self._custom_fields = value

    @property
    def fax_options(self) -> Optional[FileIds]:
        return self._fax_options

    @fax_options.setter
    def fax_options(self, value: Optional[FileIds]) -> None:
        self._fax_options = value

    class Config:
        populate_by_name = True
