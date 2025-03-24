from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from solapi.model.response.common_response import GroupMessageResponse


class GetGroupsResponse(BaseModel):
    start_key: Optional[str] = None
    limit: Optional[int] = None
    next_key: Optional[str] = None
    group_list: dict[str, GroupMessageResponse]

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
