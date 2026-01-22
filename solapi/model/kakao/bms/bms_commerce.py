from typing import Optional, Union

from pydantic import BaseModel, ConfigDict, field_validator, model_validator
from pydantic.alias_generators import to_camel


class BmsCommerce(BaseModel):
    title: Optional[str] = None
    regular_price: Optional[int] = None
    discount_price: Optional[int] = None
    discount_rate: Optional[int] = None
    discount_fixed: Optional[int] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @field_validator(
        "regular_price",
        "discount_price",
        "discount_rate",
        "discount_fixed",
        mode="before",
    )
    @classmethod
    def coerce_to_int(cls, v: Union[int, float, str, None]) -> Optional[int]:
        if v is None:
            return None
        if isinstance(v, str):
            v = v.strip()
            if not v:
                return None
            return int(float(v))
        return int(v)

    @model_validator(mode="after")
    def validate_price_combination(self) -> "BmsCommerce":
        if self.regular_price is None:
            return self

        has_discount_price = self.discount_price is not None
        has_discount_rate = self.discount_rate is not None
        has_discount_fixed = self.discount_fixed is not None

        # 할인 정보 없음 = 유효
        if not any([has_discount_price, has_discount_rate, has_discount_fixed]):
            return self

        # discountRate와 discountFixed는 상호 배타적
        if has_discount_rate and has_discount_fixed:
            raise ValueError(
                "discountRate와 discountFixed는 동시에 사용할 수 없습니다. "
                "할인율(discountRate) 또는 정액할인(discountFixed) 중 하나만 선택하세요."
            )

        # 할인 정보는 완전한 세트여야 함 (discountPrice + discountRate/discountFixed)
        if has_discount_price != (has_discount_rate or has_discount_fixed):
            if has_discount_price:
                raise ValueError(
                    "discountPrice를 사용하려면 discountRate(할인율) 또는 "
                    "discountFixed(정액할인) 중 하나를 함께 지정해야 합니다."
                )
            else:
                raise ValueError(
                    "discountRate 또는 discountFixed를 사용하려면 "
                    "discountPrice(할인가)도 함께 지정해야 합니다."
                )

        return self
