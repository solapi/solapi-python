from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class NaverButton(BaseModel):
    button_name: Optional[str] = None
    button_type: Optional[str] = None
    link_mo: Optional[str] = None
    link_pc: Optional[str] = None
    link_and: Optional[str] = None
    link_ios: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
