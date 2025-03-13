from enum import Enum
from typing import Any, Optional, TypedDict, Union

from solapi.requests.send.send_request import MessageParameter


# 외부 파일 import 대신 타입 정의
class KakaoOption:
    def __init__(self, options: dict[str, Any] = None):
        self.options = options or {}


class RcsOption:
    def __init__(self, options: dict[str, Any] = None):
        self.options = options or {}


class FileIds(TypedDict):
    fileIds: list[str]


class MessageType(str, Enum):
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


# TODO: 생성자 만들 때 Request 딕셔너리가 아니라 Response 딕셔너리로 받아와야함.
class Message:
    def __init__(self, parameter: MessageParameter):
        """
        Message 클래스 초기화

        Args:
            parameter: 메시지 파라미터 딕셔너리(json)
        """
        # 수신번호
        self._to: Union[str, list[str]] = parameter["to"]

        # 발신번호
        self._from_: Optional[str] = getattr(parameter, "from", None)

        # 메시지 내용
        self._text: Optional[str] = getattr(parameter, "text", None)

        # 메시지 생성일자
        self._date_created: Optional[str] = getattr(parameter, "dateCreated", None)

        # 메시지 수정일자
        self._date_updated: Optional[str] = getattr(parameter, "dateUpdated", None)

        # 메시지의 그룹 ID
        self._group_id: Optional[str] = getattr(parameter, "groupId", None)

        # 해당 메시지의 ID
        self._message_id: Optional[str] = getattr(parameter, "messageId", None)

        # MMS 전용 스토리지(이미지) ID
        self._image_id: Optional[str] = getattr(parameter, "imageId", None)

        # 메시지 유형
        self._type: Optional[MessageType] = getattr(parameter, "type", None)

        # 문자 제목(LMS, MMS 전용)
        self._subject: Optional[str] = getattr(parameter, "subject", None)

        # 메시지 타입 감지 여부(비활성화 시 반드시 타입이 명시 되어야 함)
        self._auto_type_detect: Optional[bool] = getattr(
            parameter, "autoTypeDetect", None
        )

        # 카카오 알림톡/친구톡을 위한 프로퍼티
        self._kakao_options: Optional[KakaoOption] = getattr(
            parameter, "kakaoOptions", None
        )

        # RCS 메시지를 위한 프로퍼티
        self._rcs_options: Optional[RcsOption] = getattr(parameter, "rcsOptions", None)

        # 해외 문자 발송을 위한 국가번호(예) "82", "1" 등)
        self._country: Optional[str] = getattr(parameter, "country", None)

        # 메시지 로그
        self._log: Optional[list[dict[str, Any]]] = getattr(parameter, "log", None)

        # 대체 텍스트
        self._replacements: Optional[list[dict[str, Any]]] = getattr(
            parameter, "replacements", None
        )

        # 메시지 상태 코드
        # https://developers.solapi.com/references/message-status-codes
        self._status_code: Optional[str] = getattr(parameter, "status", None)

        # 사용자를 위한 사용자만의 커스텀 값을 입력할 수 있는 필드
        # 단, 오브젝트 내 키 값 모두 문자열 형태로 입력되어야 합니다.
        self._custom_fields: Optional[dict[str, str]] = getattr(
            parameter, "customFields", None
        )

        # 팩스 옵션
        self._fax_options: Optional[FileIds] = getattr(parameter, "faxOptions", None)

    @property
    def to(self) -> Union[str, list[str]]:
        return self._to

    @to.setter
    def to(self, value: Union[str, list[str]]) -> None:
        self._to = value

    @property
    def from_(self) -> Optional[str]:
        return self._from_

    @from_.setter
    def from_(self, value: Optional[str]) -> None:
        self._from_ = value

    @property
    def text(self) -> Optional[str]:
        return self._text

    @text.setter
    def text(self, value: Optional[str]) -> None:
        self._text = value

    @property
    def date_created(self) -> Optional[str]:
        return self._date_created

    @date_created.setter
    def date_created(self, value: Optional[str]) -> None:
        self._date_created = value

    @property
    def date_updated(self) -> Optional[str]:
        return self._date_updated

    @date_updated.setter
    def date_updated(self, value: Optional[str]) -> None:
        self._date_updated = value

    @property
    def group_id(self) -> Optional[str]:
        return self._group_id

    @group_id.setter
    def group_id(self, value: Optional[str]) -> None:
        self._group_id = value

    @property
    def message_id(self) -> Optional[str]:
        return self._message_id

    @message_id.setter
    def message_id(self, value: Optional[str]) -> None:
        self._message_id = value

    @property
    def image_id(self) -> Optional[str]:
        return self._image_id

    @image_id.setter
    def image_id(self, value: Optional[str]) -> None:
        self._image_id = value

    @property
    def type(self) -> Optional[MessageType]:
        return self._type

    @type.setter
    def type(self, value: Optional[MessageType]) -> None:
        self._type = value

    @property
    def subject(self) -> Optional[str]:
        return self._subject

    @subject.setter
    def subject(self, value: Optional[str]) -> None:
        self._subject = value

    @property
    def auto_type_detect(self) -> Optional[bool]:
        return self._auto_type_detect

    @auto_type_detect.setter
    def auto_type_detect(self, value: Optional[bool]) -> None:
        self._auto_type_detect = value

    @property
    def kakao_options(self) -> Optional[KakaoOption]:
        return self._kakao_options

    @kakao_options.setter
    def kakao_options(self, value: Optional[KakaoOption]) -> None:
        self._kakao_options = value

    @property
    def rcs_options(self) -> Optional[RcsOption]:
        return self._rcs_options

    @rcs_options.setter
    def rcs_options(self, value: Optional[RcsOption]) -> None:
        self._rcs_options = value

    @property
    def country(self) -> Optional[str]:
        return self._country

    @country.setter
    def country(self, value: Optional[str]) -> None:
        self._country = value

    @property
    def log(self) -> Optional[list[dict[str, Any]]]:
        return self._log

    @log.setter
    def log(self, value: Optional[list[dict[str, Any]]]) -> None:
        self._log = value

    @property
    def replacements(self) -> Optional[list[dict[str, Any]]]:
        return self._replacements

    @replacements.setter
    def replacements(self, value: Optional[list[dict[str, Any]]]) -> None:
        self._replacements = value

    @property
    def status_code(self) -> Optional[str]:
        return self._status_code

    @status_code.setter
    def status_code(self, value: Optional[str]) -> None:
        self._status_code = value

    @property
    def custom_fields(self) -> Optional[dict[str, str]]:
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, value: Optional[dict[str, str]]) -> None:
        self._custom_fields = value

    @property
    def fax_options(self) -> Optional[FileIds]:
        return self._fax_options

    @fax_options.setter
    def fax_options(self, value: Optional[FileIds]) -> None:
        self._fax_options = value
