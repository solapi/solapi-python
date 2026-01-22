from typing import Annotated, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, model_validator
from pydantic.alias_generators import to_camel

BmsButtonLinkType = Literal["AC", "WL", "AL", "BK", "MD", "BC", "BT", "BF"]


class BmsWebButton(BaseModel):
    """WL: 웹 링크 버튼."""

    link_type: Literal["WL"] = "WL"
    name: str
    link_mobile: str
    link_pc: Optional[str] = None
    target_out: Optional[bool] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsAppButton(BaseModel):
    """AL: 앱 링크 버튼. linkMobile, linkAndroid, linkIos 중 하나 이상 필수."""

    link_type: Literal["AL"] = "AL"
    name: str
    link_mobile: Optional[str] = None
    link_android: Optional[str] = None
    link_ios: Optional[str] = None
    target_out: Optional[bool] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @model_validator(mode="after")
    def validate_at_least_one_link(self) -> "BmsAppButton":
        if not any([self.link_mobile, self.link_android, self.link_ios]):
            raise ValueError(
                "AL 타입 버튼은 linkMobile, linkAndroid, linkIos 중 하나 이상 필수입니다."
            )
        return self


class BmsChannelAddButton(BaseModel):
    """AC: 채널 추가 버튼."""

    link_type: Literal["AC"] = "AC"
    name: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsBotKeywordButton(BaseModel):
    """BK: 봇 키워드 버튼."""

    link_type: Literal["BK"] = "BK"
    name: str
    chat_extra: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsMessageDeliveryButton(BaseModel):
    """MD: 메시지 전달 버튼."""

    link_type: Literal["MD"] = "MD"
    name: str
    chat_extra: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsConsultButton(BaseModel):
    """BC: 상담 요청 버튼."""

    link_type: Literal["BC"] = "BC"
    name: str
    chat_extra: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsBotTransferButton(BaseModel):
    """BT: 봇 전환 버튼."""

    link_type: Literal["BT"] = "BT"
    name: str
    chat_extra: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsBusinessFormButton(BaseModel):
    """BF: 비즈니스폼 버튼."""

    link_type: Literal["BF"] = "BF"
    name: str

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


BmsButton = Annotated[
    Union[
        BmsWebButton,
        BmsAppButton,
        BmsChannelAddButton,
        BmsBotKeywordButton,
        BmsMessageDeliveryButton,
        BmsConsultButton,
        BmsBotTransferButton,
        BmsBusinessFormButton,
    ],
    "BMS 버튼 통합 타입 (linkType으로 구분)",
]

BmsLinkButton = Annotated[
    Union[BmsWebButton, BmsAppButton],
    "BMS 링크 버튼 (WL, AL만 허용) - 캐러셀 등에서 사용",
]
