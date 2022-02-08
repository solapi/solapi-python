# 그룹 추가 및 그룹 내 대량 발송 예제

create_group.py를 제외한 나머지 예제들은 모두 groupId가 있는 것을 전제로 제작 되었습니다.  
그룹 발송 시작 전 반드시 groupId를 체크 부탁드리며, groupId가 없는 경우 create_group.py 파일을 참고해주세요.

### 발송 관련 예제

```
add_group_message.py -> 그룹에 메시지 추가 예제, 즉시 발송 안됨
add_group_message_with_image -> 그룹에 사진문자 추가 예제, 즉시 발송 안됨
send_group_message.py -> 대기 상태인 그룹 건 즉시 발송 예제
```

### 예약발송 관련 예제

```
set_reservation_group.py -> 예약발송 설정 예제
cancel_reservation_group -> 예약발송 취소 예제
```

### 기타

```
create_group.py -> 그룹 생성 예제
delete_group.py -> 그룹 비활성화 예제
get_group_info.py -> 단 건 그룹 조회 예제
get_group_list.py -> 여러 그룹 건 조회 예제
```