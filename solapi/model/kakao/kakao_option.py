from collections.abc import Mapping
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.alias_generators import to_camel

from solapi.model.request.kakao.bms import Bms


class KakaoOption(BaseModel):
    pf_id: Optional[str] = None
    template_id: Optional[str] = None
    variables: Optional[dict[str, str]] = None
    disable_sms: bool = False
    image_id: Optional[str] = None
    bms: Optional[Bms] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @field_validator("variables", mode="before")
    @classmethod
    def stringify_values(cls, v: Mapping[str, object]):
        if isinstance(v, Mapping):
            # 키값을 #{변수명} 형태로 변환하고 모든 value를 str로 캐스팅
            processed_dict = {}
            for k, val in v.items():
                # 키가 이미 #{변수명} 형태가 아니면 자동으로 감싸기
                if not (k.startswith("#{") and k.endswith("}")):
                    processed_key = f"#{{{k}}}"
                else:
                    processed_key = k
                processed_dict[processed_key] = str(val)
            return processed_dict
