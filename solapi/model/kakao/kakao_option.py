from collections.abc import Mapping
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.alias_generators import to_camel


class KakaoOption(BaseModel):
    pf_id: Optional[str] = None
    template_id: Optional[str] = None
    variables: Optional[dict[str, str]] = None
    disable_sms: bool = False
    image_id: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @field_validator("variables", mode="before")
    @classmethod
    def stringify_values(cls, v: Mapping[str, object]):
        if isinstance(v, Mapping):
            # 모든 value를 str로 캐스팅
            return {k: str(val) for k, val in v.items()}
