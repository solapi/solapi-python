import os

import pytest

from solapi import SolapiMessageService


@pytest.fixture
def api_credentials():
    """
    Fixture to provide API credentials.

    Returns:
        tuple: (api_key, api_secret)
    """
    api_key = os.environ.get("SOLAPI_API_KEY", "YOUR_API_KEY")
    api_secret = os.environ.get("SOLAPI_API_SECRET", "YOUR_API_SECRET")
    return api_key, api_secret


@pytest.fixture
def message_service(api_credentials):
    """
    Fixture to provide a configured SolapiMessageService instance.

    Args:
        api_credentials: Tuple of (api_key, api_secret)

    Returns:
        SolapiMessageService: Configured service instance
    """
    api_key, api_secret = api_credentials
    return SolapiMessageService(api_key=api_key, api_secret=api_secret)


@pytest.fixture
def test_phone_numbers():
    """
    Fixture to provide test phone numbers.

    Returns:
        dict: Dictionary containing sender and recipient phone numbers
    """
    return {
        "sender": os.environ.get("SOLAPI_SENDER", "발신번호"),
        "recipient": os.environ.get("SOLAPI_RECIPIENT", "수신번호"),
    }


@pytest.fixture
def test_kakao_options():
    """
    Fixture to provide test Kakao options.

    Returns:
        dict: Dictionary containing Kakao channel ID and template ID
    """
    return {
        "pf_id": os.environ.get(
            "SOLAPI_KAKAO_PF_ID", "계정에 등록된 카카오 비즈니스 채널ID"
        ),
        "template_id": os.environ.get(
            "SOLAPI_KAKAO_TEMPLATE_ID", "계정에 등록된 카카오 알림톡 템플릿 ID"
        ),
    }
