import re
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.alias_generators import to_camel

WON_DISCOUNT_PATTERN = re.compile(r"^([1-9]\d{0,7})원 할인 쿠폰$")
PERCENT_DISCOUNT_PATTERN = re.compile(r"^([1-9]\d?|100)% 할인 쿠폰$")
FREE_COUPON_PATTERN = re.compile(r"^.{1,7} 무료 쿠폰$")
UP_COUPON_PATTERN = re.compile(r"^.{1,7} UP 쿠폰$")


def _is_valid_coupon_title(title: str) -> bool:
    if title == "배송비 할인 쿠폰":
        return True

    won_match = WON_DISCOUNT_PATTERN.match(title)
    if won_match:
        num = int(won_match.group(1))
        return 1 <= num <= 99_999_999

    if PERCENT_DISCOUNT_PATTERN.match(title):
        return True

    if FREE_COUPON_PATTERN.match(title):
        return True

    return bool(UP_COUPON_PATTERN.match(title))


class BmsCoupon(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    link_mobile: Optional[str] = None
    link_pc: Optional[str] = None
    link_android: Optional[str] = None
    link_ios: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @field_validator("title")
    @classmethod
    def validate_coupon_title(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        if not _is_valid_coupon_title(v):
            raise ValueError(
                "쿠폰 제목은 다음 형식 중 하나여야 합니다: "
                '"N원 할인 쿠폰" (1~99999999), '
                '"N% 할인 쿠폰" (1~100), '
                '"배송비 할인 쿠폰", '
                '"OOO 무료 쿠폰" (7자 이내), '
                '"OOO UP 쿠폰" (7자 이내)'
            )
        return v

    @field_validator("description")
    @classmethod
    def validate_coupon_description(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        if len(v) > 12:
            raise ValueError("쿠폰 설명은 최대 12자 이하로 입력해주세요.")
        return v
