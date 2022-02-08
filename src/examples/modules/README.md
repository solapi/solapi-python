# SOLAPI Python 기본 예제

src/lib/config.ini 파일을 생성하신 다음, 아래와 같이 설정 후 examples 아래 예제 코드를 실행해 보세요.

```
[AUTH]
# 계정의 API Key와 API Secret을 입력해주세요
api_key = [API KEY]
api_secret = [API SECRET]

[SERVER]
domain = api.solapi.com
protocol = https
prefix =
```

### 문자 발송 예제

```
sms/send_sms.py                 SMS 발송 예제(해외 발송 포함)
sms/send_lms.py                 LMS 발송 예제
sms/send_mms.py                 MMS 발송 예제
sms/allow_duplicates.py         수신번호 중복 허용 예제
rcs/send_rcs_sms.py             RCS SMS 발송 예제(버튼 포함)
rcs/send_rcs_lms.py             RCS LMS 발송 에제(버튼 포함)
```

### 카카오톡(알림톡, 친구톡) 발송 예제

```
kakaotalk/send_alimtalk.py            알림톡 발송 예제
kakaotalk/send_chingutalk.py          친구톡 발송 예제
```

### 네이버톡톡 발송 예제

```
send_naver.py               네이버톡톡 예제
```

### 메시지 조회

```
message_list.py             메시지 목록 조회
```

### 기타

```
senderid                    발신번호 등록 및 인증 예제
group                       그룹발송 및 예약발송 예제
storage                     MMS, 친구톡, RCS 파일(이미지) 관리
```
