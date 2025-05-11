import json

from django.http import HttpResponseNotAllowed, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from solapi.model.response.send_message_response import SendMessageResponse


@method_decorator(csrf_exempt, name="dispatch")
class WebhookController(View):
    """
    POST 로만 받는 웹훅 엔드포인트
    CSRF 예외 처리(@csrf_exempt) 를 걸어야 외부에서 POST 요청이 들어올 때 403 에러가 나지 않습니다.
    """

    http_method_names = ["post", "options"]

    def post(self, request, *args, **kwargs):
        try:
            payload = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"error": "invalid JSON"}, status=400)

        message_response = SendMessageResponse.model_validate(payload)

        return JsonResponse(message_response.model_dump_json(), status=200)

    def options(self, request, *args, **kwargs):
        response = JsonResponse({"status": "options OK"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST", "OPTIONS"])
