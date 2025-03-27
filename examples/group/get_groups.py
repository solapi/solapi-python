from solapi import SolapiMessageService

# API 키와 API Secret을 설정합니다
message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

# 메시지 그룹을 생성하고 조회합니다
try:
    # 그룹 목록을 조회합니다
    groups_response = message_service.get_groups()
    print("메시지 그룹 목록:")
    for group_id, group in groups_response.group_list.items():
        print("----")
        print(f"\nGroup ID: {group_id}")
        print(f"생성 시간: {group.date_created}")
        print(f"메시지 수: {group.count.total}")
        print(f"상태: {group.status}")
        print(f"처리 로그: {group.log}")
        print("----")

except Exception as e:
    print(f"그룹 조회 실패: {str(e)}")
