from typing import TypeVar

# from authenticator import get_headers


def get_url(path):
    url: str = "https://api.solapi.com"
    return url + path


T = TypeVar("T")
R = TypeVar("R")


def fetch(request, data: T) -> R:
    return ""
