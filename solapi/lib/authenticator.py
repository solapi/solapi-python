import datetime
import hashlib
import hmac
import time
import uuid
from typing import TypedDict


class AuthenticationParameter(TypedDict):
    api_key: str
    api_secret: str


class Authenticator:
    def __init__(self, api_key="", api_secret_key=""):
        self.api_key = api_key
        self.api_secret_key = api_secret_key

    @staticmethod
    def unique_id() -> str:
        return uuid.uuid1().hex

    @staticmethod
    def get_iso_datetime() -> str:
        utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
        utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
        return (
            datetime.datetime.now()
            .replace(tzinfo=datetime.timezone(offset=utc_offset))
            .isoformat()
        )

    @staticmethod
    def get_signature(key: str, msg: str) -> str:
        return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()

    def get_auth_info(self) -> str:
        date = self.get_iso_datetime()
        salt = self.unique_id()
        data = date + salt
        signature = self.get_signature(self.api_secret_key, data)
        return f"HMAC-SHA256 ApiKey={self.api_key}, Date={date}, salt={salt}, signature={signature}"
