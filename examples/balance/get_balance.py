from solapi import SolapiMessageService

# API 키와 API Secret을 설정합니다
message_service = SolapiMessageService(
    api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET"
)

try:
    # 잔액을 조회합니다
    balance_response = message_service.get_balance()

    print("잔액 조회 성공!")
    print(f"현재 잔액: {balance_response.balance}원")
    print(f"포인트: {balance_response.point}P")

except Exception as e:
    print(f"잔액 조회 실패: {str(e)}")
