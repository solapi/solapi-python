# SOLAPI MODEL LAYER

## OVERVIEW

Pydantic v2 models for SOLAPI REST API. Domain-driven organization by messaging channel.

## STRUCTURE

```
model/
├── request/           # Outbound payloads
│   ├── message.py     # Core Message class
│   ├── send_message_request.py
│   ├── storage.py     # File upload
│   ├── kakao/         # Kakao BMS, option
│   ├── voice/         # Voice message
│   ├── messages/      # Get messages query
│   └── groups/        # Get groups query
├── response/          # Inbound payloads
│   ├── send_message_response.py
│   ├── common_response.py
│   ├── storage.py
│   ├── balance/
│   ├── messages/
│   └── groups/
├── kakao/             # Kakao channel models
├── naver/             # Naver channel models
├── rcs/               # RCS channel models
└── webhook/           # Delivery reports
```

## WHERE TO LOOK

| Task | File | Notes |
|------|------|-------|
| Build message payload | `request/message.py` | Main `Message` class |
| Send request wrapper | `request/send_message_request.py` | Wraps messages list |
| Handle send response | `response/send_message_response.py` | Parse API response |
| Kakao options | `kakao/kakao_option.py` | PF ID, template, buttons |
| Naver options | `naver/naver_option.py` | Naver talk settings |
| RCS options | `rcs/rcs_options.py` | RCS specific fields |
| Webhook parsing | `webhook/single_report.py` | Delivery status |

## CONVENTIONS

### All Models Are Pydantic
```python
from pydantic import BaseModel, Field

class Message(BaseModel):
    to: str = Field(alias="to")  # camelCase alias for API
```

### Request vs Response Separation
- NEVER share classes between request/response
- Request: what you send to API
- Response: what API returns
- Even similar fields get separate classes

### Field Aliases for API
```python
# snake_case in Python, camelCase in JSON
pf_id: str = Field(alias="pfId")
template_id: str = Field(alias="templateId")
```

### Validators for Normalization
```python
@field_validator("to", mode="before")
@classmethod
def normalize_phone(cls, v: str) -> str:
    return v.replace("-", "")  # Strip dashes
```

### Optional Fields
```python
# Use Optional with None default
subject: Optional[str] = None
image_id: Optional[str] = Field(default=None, alias="imageId")
```

## ANTI-PATTERNS

### NEVER
- Use TypedDict for API models (Pydantic only)
- Share model between request/response
- Forget alias when API uses camelCase
- Skip validators for phone numbers

### VERSION IN THIS PACKAGE
```python
# request/__init__.py line 1-2
VERSION = "python/5.0.3"  # Sync with pyproject.toml!
```

## KEY CLASSES

### Request Side
- `Message` - Core message with to, from, text, type
- `SendMessageRequest` - Wrapper with messages list + version
- `SendRequestConfig` - app_id, scheduled_date, allow_duplicates
- `KakaoOption` - Kakao-specific (pfId, templateId, buttons)
- `FileUploadRequest` - Base64 encoded file

### Response Side
- `SendMessageResponse` - Contains group_info, failed_message_list
- `GroupMessageResponse` - Generic group response
- `GetBalanceResponse` - balance, point fields
- `FileUploadResponse` - fileId for uploaded files

## NOTES

- Korean comments exist (i18n TODO)
- Some TODOs for future field additions (kakao button types, group count fields)
- Webhook models for delivery status callbacks
