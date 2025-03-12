import platform
import sys
from typing import NotRequired, TypedDict


class DefaultAgentType(TypedDict):
    sdkVersion: str
    osPlatform: str
    appId: NotRequired[str]


default_agent: DefaultAgentType = {
    "sdkVersion": "python/5.0.0",
    "osPlatform": f"{platform.system().lower()} | {sys.version.split()[0]}",
}