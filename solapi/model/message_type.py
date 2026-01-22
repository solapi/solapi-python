from enum import Enum


class MessageType(Enum):
    """
    메시지 유형(단문 문자, 장문 문자, 알림톡 등)
    SMS: 단문 문자
    LMS: 장문 문자
    MMS: 사진 문자
    ATA: 알림톡
    CTA: 친구톡
    CTI: 사진 한장이 포함된 친구톡
    NSA: 네이버 스마트알림(톡톡)
    RCS_SMS: RCS 단문 문자
    RCS_LMS: RCS 장문 문자
    RCS_MMS: RCS 사진 문자
    RCS_TPL: RCS 템플릿
    RCS_ITPL: RCS 이미지 템플릿
    RCS_LTPL: RCS LMS 템플릿 문자
    FAX: 팩스
    VOICE: 음성문자(TTS)
    BMS_TEXT: 브랜드 메시지 텍스트형
    BMS_IMAGE: 브랜드 메시지 이미지형
    BMS_WIDE: 브랜드 메시지 와이드형
    BMS_WIDE_ITEM_LIST: 브랜드 메시지 와이드 아이템 리스트형
    BMS_CAROUSEL_FEED: 브랜드 메시지 캐러셀 피드형
    BMS_PREMIUM_VIDEO: 브랜드 메시지 프리미엄 비디오형
    BMS_COMMERCE: 브랜드 메시지 커머스형
    BMS_CAROUSEL_COMMERCE: 브랜드 메시지 캐러셀 커머스형
    BMS_FREE: 브랜드 메시지 자유형
    """

    SMS = "SMS"
    LMS = "LMS"
    MMS = "MMS"
    ATA = "ATA"
    CTA = "CTA"
    CTI = "CTI"
    NSA = "NSA"
    RCS_SMS = "RCS_SMS"
    RCS_LMS = "RCS_LMS"
    RCS_MMS = "RCS_MMS"
    RCS_TPL = "RCS_TPL"
    RCS_ITPL = "RCS_ITPL"
    RCS_LTPL = "RCS_LTPL"
    FAX = "FAX"
    VOICE = "VOICE"
    BMS_TEXT = "BMS_TEXT"
    BMS_IMAGE = "BMS_IMAGE"
    BMS_WIDE = "BMS_WIDE"
    BMS_WIDE_ITEM_LIST = "BMS_WIDE_ITEM_LIST"
    BMS_CAROUSEL_FEED = "BMS_CAROUSEL_FEED"
    BMS_PREMIUM_VIDEO = "BMS_PREMIUM_VIDEO"
    BMS_COMMERCE = "BMS_COMMERCE"
    BMS_CAROUSEL_COMMERCE = "BMS_CAROUSEL_COMMERCE"
    BMS_FREE = "BMS_FREE"

    def __str__(self) -> str:
        return self.value

    def __repr__(self):
        return repr(self.value)
