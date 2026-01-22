from typing import Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, model_validator
from pydantic.alias_generators import to_camel

from solapi.model.kakao.bms.bms_button import BmsButton
from solapi.model.kakao.bms.bms_carousel import (
    BmsCarouselCommerceSchema,
    BmsCarouselFeedSchema,
)
from solapi.model.kakao.bms.bms_commerce import BmsCommerce
from solapi.model.kakao.bms.bms_coupon import BmsCoupon
from solapi.model.kakao.bms.bms_option import (
    BmsChatBubbleType,
    validate_bms_required_fields,
)
from solapi.model.kakao.bms.bms_video import BmsVideo
from solapi.model.kakao.bms.bms_wide_item import BmsMainWideItem, BmsSubWideItem


class Bms(BaseModel):
    targeting: Optional[Literal["I", "M", "N"]] = None
    chat_bubble_type: Optional[BmsChatBubbleType] = None

    adult: Optional[bool] = None
    header: Optional[str] = None
    image_id: Optional[str] = None
    image_link: Optional[str] = None
    additional_content: Optional[str] = None
    content: Optional[str] = None

    carousel: Optional[Union[BmsCarouselFeedSchema, BmsCarouselCommerceSchema]] = None
    main_wide_item: Optional[BmsMainWideItem] = None
    sub_wide_item_list: Optional[list[BmsSubWideItem]] = None
    buttons: Optional[list[BmsButton]] = None
    coupon: Optional[BmsCoupon] = None
    commerce: Optional[BmsCommerce] = None
    video: Optional[BmsVideo] = None

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="ignore",
    )

    @model_validator(mode="after")
    def validate_required_fields(self) -> "Bms":
        validate_bms_required_fields(
            chat_bubble_type=self.chat_bubble_type,
            sub_wide_item_list=self.sub_wide_item_list,
            get_field_value=lambda field: getattr(self, field, None),
        )
        return self
