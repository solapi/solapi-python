from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


# TODO: Request, Response용 모델을 별도로 분리해야 함
class KakaoOption(BaseModel):
    pf_id: Optional[str] = None
    template_id: Optional[str] = None
    variables: Optional[dict[str, str]] = None
    disable_sms: bool = False
    image_id: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
