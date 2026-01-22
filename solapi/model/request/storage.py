from enum import Enum
from typing import Optional

from pydantic import BaseModel


class FileTypeEnum(str, Enum):
    MMS = "MMS"
    KAKAO = "KAKAO"
    RCS = "RCS"
    FAX = "FAX"
    # BMS (Brand Message Service) file types
    BMS = "BMS"
    BMS_WIDE = "BMS_WIDE"
    BMS_WIDE_MAIN_ITEM_LIST = "BMS_WIDE_MAIN_ITEM_LIST"
    BMS_WIDE_SUB_ITEM_LIST = "BMS_WIDE_SUB_ITEM_LIST"
    BMS_CAROUSEL_FEED_LIST = "BMS_CAROUSEL_FEED_LIST"
    BMS_CAROUSEL_COMMERCE_LIST = "BMS_CAROUSEL_COMMERCE_LIST"


class FileUploadRequest(BaseModel):
    type: FileTypeEnum
    file: str
    name: Optional[str] = None
    link: Optional[str] = None
