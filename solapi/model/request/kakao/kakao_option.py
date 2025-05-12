from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from solapi.model.kakao.kakao_button import KakaoButton


class KakaoOption(BaseModel):
    pf_id: str
    template_id: Optional[str] = None
    variables: Optional[dict[str, str]] = None
    disable_sms: bool = False
    image_id: Optional[str] = None
    buttons: Optional[list[KakaoButton]] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
