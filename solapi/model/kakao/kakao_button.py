from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class KakaoButton(BaseModel):
    link_mo: Optional[str] = None
    link_pc: Optional[str] = None
    button_name: Optional[str] = None
    # TODO: 추후 타입 추가 필요
    button_type: Optional[str] = None
    link_and: Optional[str] = None
    link_ios: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
