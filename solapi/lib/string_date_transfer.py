import re
import time
from datetime import datetime, timedelta, timezone
from typing import Union


class InvalidDateError(Exception):
    """날짜 형식이 유효하지 않을 때 발생하는 예외"""

    def __init__(self, message="Invalid date format", *args):
        self.message = message
        super().__init__(message, *args)

    def __str__(self):
        return self.message


def format_iso(date: datetime) -> str:
    """
    datetime 객체를 ISO 8601 형식의 문자열로 변환

    Args:
        date: 변환할 datetime 객체

    Returns:
        ISO 8601 형식의 문자열 (예: '2023-01-01T12:00:00Z')
    """
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = timedelta(seconds=-utc_offset_sec)
    return date.replace(tzinfo=timezone(offset=utc_offset)).isoformat()


def parse_iso(date_string: str) -> datetime:
    """
    ISO 8601 형식의 문자열을 datetime 객체로 변환

    Args:
        date_string: 변환할 ISO 8601 형식의 문자열

    Returns:
        변환된 datetime 객체

    Raises:
        InvalidDateError: 날짜 형식이 유효하지 않을 경우
    """
    try:
        # ISO 8601 형식 검증을 위한 간단한 정규식
        iso_pattern = re.compile(
            r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?(\.\d+)?(([+-]\d{2}:\d{2})|Z)?)?$"
        )
        if not iso_pattern.match(date_string):
            raise ValueError("Invalid ISO format")

        # 타임존 정보가 없는 경우 처리
        if (
            "Z" not in date_string
            and "+" not in date_string
            and "-" not in date_string[10:]
        ):
            date_string += "Z"

        return datetime.fromisoformat(date_string.replace("Z", "+00:00"))
    except ValueError as e:
        raise InvalidDateError("Invalid Date") from e


def string_date_transfer(value: Union[str, datetime]):
    """
    일반 문자열 날짜가 있을 경우 datetime 타입으로 변환해주는 함수

    Args:
        value: 일반 문자열 날짜 또는 datetime 타입의 날짜

    Returns:
        datetime 객체

    Raises:
        InvalidDateError: 날짜 형식이 유효하지 않을 경우
    """
    if isinstance(value, str):
        try:
            value = parse_iso(value)
        except Exception as e:
            raise InvalidDateError("Invalid Date") from e

    return value


def format_with_transfer(value: Union[str, datetime]) -> str:
    """
    string_date_transfer와 format_iso를 한번에 실행하는 함수

    Args:
        value: datetime 타입의 날짜 또는 ISO 형식의 문자열

    Returns:
        ISO 8601 형식의 문자열

    Raises:
        InvalidDateError: 날짜 형식이 유효하지 않을 경우
    """
    return format_iso(string_date_transfer(value))
