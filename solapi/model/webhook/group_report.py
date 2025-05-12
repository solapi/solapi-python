from typing import Optional

from pydantic import BaseModel, ConfigDict, RootModel
from pydantic.alias_generators import to_camel

from solapi.model.response.common_response import GroupMessageResponse


class GroupReport(BaseModel):
    event_data_id: Optional[str] = None
    data: Optional[GroupMessageResponse] = None
    retry_count: Optional[int] = None

    model_config = ConfigDict(
        populate_by_name=True, alias_generator=to_camel, extra="ignore"
    )


class GroupReportPayload(RootModel[list[GroupReport]]):
    pass
