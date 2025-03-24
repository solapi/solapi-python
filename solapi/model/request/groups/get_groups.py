from datetime import datetime
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class GetGroupsRequest(BaseModel):
    start_key: Optional[str] = None
    limit: int = 20
    start_date: Optional[Union[str, datetime]] = None
    end_date: Optional[Union[str, datetime]] = None
    group_id: Optional[str] = Field(default=None, exclude=True)

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class GetGroupsCrteriaType(str, Enum):
    group_id = "groupId"
    date_created = "dateCreated"
    scheduled_date = "scheduledDate"

    def __str__(self) -> str:
        return self.value

    def __repr__(self):
        return repr(self.value)

    # TODO: count.total, count.sentTotal 추후에 추가해야 함


class GetGroupsFinalizeRequest(BaseModel):
    start_key: Optional[str] = None
    limit: int = 20
    start_date: Optional[Union[str, datetime]] = None
    end_date: Optional[Union[str, datetime]] = None
    criteria: Optional[str] = None
    cond: Optional[str] = None
    value: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
