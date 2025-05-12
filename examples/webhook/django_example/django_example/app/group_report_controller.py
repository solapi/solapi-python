import json

from django.http import HttpResponseNotAllowed, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from solapi.model.webhook.group_report import GroupReportPayload


@method_decorator(csrf_exempt, name="dispatch")
class GroupReportWebhookController(View):
    """
    POST 로만 받는 그룹 리포트(Group Report) 웹훅 엔드포인트
    CSRF 예외 처리(@csrf_exempt) 를 걸어야 외부에서 POST 요청이 들어올 때 403 에러가 나지 않습니다.
    """

    http_method_names = ["post", "options"]

    def post(self, request, *args, **kwargs):
        try:
            payload = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"error": "invalid JSON"}, status=400)

        message_response = GroupReportPayload.model_validate(payload)
        group_report = message_response.root[0]

        # 이후 필요한 프로그래밍 처리.. 아래 방식처럼 데이터를 추출해서 사용할 수 있습니다.
        print(group_report.data.group_id)

        # 혹은..
        print(group_report.data.date_created)

        # 또는..
        print(group_report.data.log)

        # 200을 리턴해야 합니다. (200이 리턴되지 않으면 특정 시간 간격을 두고 총 5번이 호출됩니다)
        return JsonResponse(group_report.model_dump(), status=200)

    def options(self, request, *args, **kwargs):
        response = JsonResponse({"status": "options OK"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST", "OPTIONS"])
