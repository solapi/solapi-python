from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class RcsMmsType(str, Enum):
    """
    사진 문자 타입. 타입: "M3", "S3", "M4", "S4", "M5", "S5", "M6", "S6" (M: 중간 사이즈. S: 작은 사이즈. 숫자: 사진 개수)
    """

    S3 = "S3"
    S4 = "S4"
    S5 = "S5"
    S6 = "S6"
    M3 = "M3"
    M4 = "M4"
    M5 = "M5"
    M6 = "M6"

    def __str__(self) -> str:
        return self.value

    def __repr__(self):
        return repr(self.value)


class RcsAdditionalBody(BaseModel):
    title: str
    description: str
    image_id: Optional[str] = None
    buttons: Optional[dict[str, str]] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class RcsButtonType(str, Enum):
    """
    'WL'(웹링크), 'ML'(지도[좌표]), 'MQ'(지도[쿼리]), 'MR'(위치공유),
    'CA'(캘린더생성), 'CL'(복사), 'DL'(전화걸기), 'MS'(메시지보내기)
    """

    WL = "WL"
    ML = "ML"
    MR = "MR"
    CA = "CA"
    CL = "CL"
    DL = "DL"
    MS = "MS"

    def __str__(self) -> str:
        return self.value

    def __repr__(self):
        return repr(self.value)


class RcsButton(BaseModel):
    button_type: RcsButtonType
    button_name: str
    link: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    label: Optional[str] = None
    query: Optional[str] = None
    title: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    text: Optional[str] = None
    phone: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class RcsOption(BaseModel):
    brand_id: Optional[str] = None
    template_id: Optional[str] = None
    copy_allowed: Optional[bool] = None
    variables: Optional[dict[str, str]] = None
    mms_type: Optional[RcsMmsType] = None
    commercial_type: Optional[bool] = None
    disable_sms: Optional[bool] = False
    additional_body: Optional[list[RcsAdditionalBody]] = None
    buttons: Optional[list[RcsButton]] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
