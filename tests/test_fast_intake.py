import pytest

from solapi.model import RequestMessage
from solapi.model.response.common_response import GroupMessageResponse
from solapi.model.response.groups.get_group_messages import GetGroupMessagesResponse
from solapi.model.response.send_message_response import SendMessageResponse
from solapi.services import message_service as message_service_module
from solapi.services.message_service import SolapiMessageService

GROUP_ID = "G4V20260101000000TESTGROUP00000"

PRICE_TYPES = [
    "sms",
    "lms",
    "mms",
    "ata",
    "nsa",
    "rcs_sms",
    "rcs_lms",
    "rcs_mms",
    "rcs_tpl",
    "rcs_itpl",
    "rcs_ltpl",
    "fax",
    "voice",
    "bms_text",
    "bms_image",
    "bms_wide",
    "bms_wide_item_list",
    "bms_carousel_feed",
    "bms_premium_video",
    "bms_commerce",
    "bms_carousel_commerce",
    "bms_free",
]


def fast_group_response() -> dict:
    count_for_charge = {price_type: {} for price_type in PRICE_TYPES}
    count_for_charge["sms"] = {"82": 1}
    cash = {
        "requested": 0,
        "replacement": 0,
        "additional": 0,
        "refund": 0,
        "sum": 0,
    }
    return {
        "_id": GROUP_ID,
        "groupId": GROUP_ID,
        "accountId": "12345678901234",
        "apiVersion": "v4-fast",
        "sdkVersion": "python/probe",
        "count": {
            "total": 1,
            "sentTotal": 0,
            "sentFailed": 0,
            "sentSuccess": 0,
            "sentPending": 1,
            "sentReplacement": 0,
            "refund": 0,
            "registeredFailed": 0,
            "registeredSuccess": 1,
        },
        "countForCharge": count_for_charge,
        "log": [{"createAt": "2026-01-01T00:00:00.000Z", "message": "created"}],
        "status": "SEND-REQUESTED",
        "dateSent": "2026-01-01T00:00:00.000Z",
        "scheduledDate": None,
        "dateCompleted": None,
        "balance": cash,
        "point": {**cash, "requested": 13, "sum": 13},
        "app": {
            "profit": {price_type: 0 for price_type in PRICE_TYPES},
            "appId": None,
            "version": None,
        },
        "price": {"82": {"sms": 13, "lms": 29, "mms": 60, "ata": 8}},
        "customFields": {},
        "masterAccountId": None,
        "allowDuplicates": False,
        "dateCreated": "2026-01-01T00:00:00.000Z",
        "dateUpdated": "2026-01-01T00:00:00.000Z",
    }


def fast_send_response() -> dict:
    return {
        "messageList": [
            {
                "messageId": "M4V20260101000000TESTMESSAGE000",
                "statusCode": "2000",
                "statusMessage": "정상 접수(이통사로 접수 예정) ",
                "customFields": {},
            }
        ],
        "failedMessageList": [],
        "groupInfo": fast_group_response(),
    }


@pytest.fixture
def fetcher_calls(monkeypatch):
    calls: list[dict] = []
    responses: list = []

    def fake_fetcher(auth_parameter, request, data=None):
        calls.append({"request": request, "data": data})
        return responses.pop(0)

    monkeypatch.setattr(message_service_module, "default_fetcher", fake_fetcher)
    calls_with_queue = {"calls": calls, "responses": responses}
    return calls_with_queue


@pytest.fixture
def service() -> SolapiMessageService:
    return SolapiMessageService(api_key="key", api_secret="secret")


class TestFastIntake:
    def test_send_uses_fast_route(self, service, fetcher_calls):
        fetcher_calls["responses"].append(fast_send_response())

        response = service.send(
            RequestMessage(from_="01000000000", to="01000000000", text="hello")
        )

        request = fetcher_calls["calls"][0]["request"]
        assert request["url"] == "https://api.solapi.com/messages/v4/send-many/fast"
        assert request["method"] == "POST"
        assert isinstance(response, SendMessageResponse)
        assert response.group_info.status == "SEND-REQUESTED"
        assert response.group_info.count.sent_pending == 1

    def test_fast_send_response_without_cta_cti_parses(self):
        payload = fast_send_response()
        assert "cta" not in payload["groupInfo"]["countForCharge"]
        assert "cti" not in payload["groupInfo"]["app"]["profit"]
        payload["groupInfo"].pop("isRefunded", None)

        response = SendMessageResponse.model_validate(payload)

        assert response.group_info.count_for_charge.cta is None
        assert response.group_info.count_for_charge.cti is None
        assert response.group_info.app.profit.cta is None
        assert response.group_info.app.profit.cti is None
        assert response.group_info.is_refunded is False
        assert response.message_list[0].custom_fields == {}

    def test_get_group_uses_fast_route(self, service, fetcher_calls):
        fetcher_calls["responses"].append(fast_group_response())

        response = service.get_group(GROUP_ID)

        request = fetcher_calls["calls"][0]["request"]
        assert (
            request["url"]
            == f"https://api.solapi.com/messages/v4/groups/fast/{GROUP_ID}"
        )
        assert request["method"] == "GET"
        assert isinstance(response, GroupMessageResponse)
        assert response.group_id == GROUP_ID
        assert response.status == "SEND-REQUESTED"

    def test_get_group_messages_uses_fast_route(self, service, fetcher_calls):
        fetcher_calls["responses"].append(
            {"startKey": None, "nextKey": None, "limit": 20, "messageList": {}}
        )

        response = service.get_group_messages(GROUP_ID)

        request = fetcher_calls["calls"][0]["request"]
        assert (
            request["url"]
            == f"https://api.solapi.com/messages/v4/groups/fast/{GROUP_ID}/messages"
        )
        assert request["method"] == "GET"
        assert isinstance(response, GetGroupMessagesResponse)
        assert response.message_list == {}
