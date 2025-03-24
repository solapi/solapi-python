from enum import Enum
from typing import Optional

from pydantic import BaseModel


class FileTypeEnum(str, Enum):
    MMS = "MMS"
    KAKAO = "KAKAO"
    RCS = "RCS"
    FAX = "FAX"


class FileUploadRequest(BaseModel):
    type: FileTypeEnum
    file: str
    name: Optional[str] = None
    link: Optional[str] = None
