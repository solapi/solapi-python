from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from solapi.model.naver.naver_button import NaverButton


class NaverOption(BaseModel):
    talk_id: Optional[str] = None
    template_id: Optional[str] = None
    disable_sms: Optional[bool] = None
    variables: Optional[dict[str, str]] = None
    buttons: Optional[list[NaverButton]] = None

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
