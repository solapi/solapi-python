from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class KakaoFileUploadResponseProperty(BaseModel):
    daou: Optional[str] = None
    biztalk: Optional[str] = None

    model_config = ConfigDict(extra="ignore")


class FileUploadResponse(BaseModel):
    kakao: Optional[KakaoFileUploadResponseProperty] = None
    type: str
    original_name: str
    link: Optional[str] = None
    file_id: str
    name: str
    url: str
    account_id: str
    references: Optional[list[str]] = None
    date_created: Optional[datetime] = None
    date_updated: Optional[datetime] = None

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, extra="ignore"
    )
