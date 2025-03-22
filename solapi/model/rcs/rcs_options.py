from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class RcsOptions(BaseModel):
    brand_id: Optional[str] = None
    template_id: Optional[str] = None
    copy_allowed: Optional[bool] = None
    variables: Optional[dict[str, str]] = None
    mms_type: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
