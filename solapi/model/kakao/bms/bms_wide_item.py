from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class BmsMainWideItem(BaseModel):
    title: Optional[str] = None
    image_id: Optional[str] = None
    link_mobile: Optional[str] = None
    link_pc: Optional[str] = None
    link_android: Optional[str] = None
    link_ios: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BmsSubWideItem(BaseModel):
    title: Optional[str] = None
    image_id: Optional[str] = None
    link_mobile: Optional[str] = None
    link_pc: Optional[str] = None
    link_android: Optional[str] = None
    link_ios: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
