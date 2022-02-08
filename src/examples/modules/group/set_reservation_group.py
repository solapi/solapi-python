import json
import time
import datetime
from src.lib import message

'''
예약 발송 예제, 미리 그룹이 추가되어 있어야 합니다.
'''
if __name__ == '__main__':
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)

    # 희망하시는 예약 날짜를 넣어주세요
    # datetime(년, 월, 일, 시, 분, 초)
    scheduledDate = datetime.datetime(2022, 2, 8, 0, 0, 0).replace(
        tzinfo=datetime.timezone(offset=utc_offset)).isoformat()
    data = {
        'scheduledDate': scheduledDate
    }

    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    res = message.post('/messages/v4/groups/[INPUT_GROUP_ID]/schedule', data=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
