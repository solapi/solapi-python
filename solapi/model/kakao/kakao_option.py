from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class KakaoOption(BaseModel):
    pf_id: str
    template_id: Optional[str] = None
    variables: Optional[dict[str, str]] = None
    disable_sms: bool = False
    ad_flag: bool = False
    buttons: Optional[dict[str, str]] = None
    image_id: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
