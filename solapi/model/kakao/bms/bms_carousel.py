from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from solapi.model.kakao.bms.bms_button import BmsLinkButton
from solapi.model.kakao.bms.bms_commerce import BmsCommerce
from solapi.model.kakao.bms.bms_coupon import BmsCoupon


class BmsCarouselHead(BaseModel):
    header: Optional[str] = None
    content: Optional[str] = None
    image_id: Optional[str] = None
    link_mobile: Optional[str] = None
    link_pc: Optional[str] = None
    link_android: Optional[str] = None
    link_ios: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsCarouselTail(BaseModel):
    link_mobile: Optional[str] = None
    link_pc: Optional[str] = None
    link_android: Optional[str] = None
    link_ios: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsCarouselFeedItem(BaseModel):
    header: Optional[str] = None
    content: Optional[str] = None
    image_id: Optional[str] = None
    image_link: Optional[str] = None
    buttons: Optional[list[BmsLinkButton]] = None
    coupon: Optional[BmsCoupon] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsCarouselFeedSchema(BaseModel):
    items: Optional[list[BmsCarouselFeedItem]] = Field(default=None, alias="list")
    tail: Optional[BmsCarouselTail] = None

    model_config = ConfigDict(populate_by_name=True)


class BmsCarouselCommerceItem(BaseModel):
    commerce: Optional[BmsCommerce] = None
    image_id: Optional[str] = None
    image_link: Optional[str] = None
    buttons: Optional[list[BmsLinkButton]] = None
    additional_content: Optional[str] = None
    coupon: Optional[BmsCoupon] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsCarouselCommerceSchema(BaseModel):
    head: Optional[BmsCarouselHead] = None
    items: Optional[list[BmsCarouselCommerceItem]] = Field(default=None, alias="list")
    tail: Optional[BmsCarouselTail] = None

    model_config = ConfigDict(populate_by_name=True)
