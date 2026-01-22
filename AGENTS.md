# SOLAPI-PYTHON KNOWLEDGE BASE

**Generated:** 2026-01-21
**Commit:** b77fdd9
**Branch:** main

## OVERVIEW

Python SDK for SOLAPI messaging platform. Sends SMS/LMS/MMS/Kakao/Naver/RCS messages in Korea. Thin wrapper around REST API using httpx + Pydantic v2.

## STRUCTURE

```
solapi-python/
├── solapi/              # Main package (single export: SolapiMessageService)
│   ├── services/        # message_service.py - all API operations
│   ├── model/           # Pydantic models (see solapi/model/AGENTS.md)
│   ├── lib/             # authenticator.py, fetcher.py
│   └── error/           # MessageNotReceivedError only
├── tests/               # pytest integration tests
├── examples/            # Feature-based usage examples
└── debug/               # Dev test scripts (not part of package)
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Send messages | `solapi/services/message_service.py` | All 10 API methods in single class |
| Request models | `solapi/model/request/` | Pydantic BaseModel with validators |
| Response models | `solapi/model/response/` | Separate from request models |
| Kakao/Naver/RCS | `solapi/model/{kakao,naver,rcs}/` | Domain-specific models |
| Authentication | `solapi/lib/authenticator.py` | HMAC-SHA256 signature |
| HTTP client | `solapi/lib/fetcher.py` | httpx with 3 retries |
| Test fixtures | `tests/conftest.py` | env-based credentials |
| Usage examples | `examples/simple/` | Copy-paste ready |

## CONVENTIONS

### Pydantic Everywhere
- ALL models extend `BaseModel`
- Field aliases: `Field(alias="camelCase")` for API compatibility
- Validators: `@field_validator` for normalization (e.g., phone numbers)

### Model Organization (Domain-Driven)
```
model/
├── request/       # Outbound API payloads
├── response/      # Inbound API responses
├── kakao/         # Kakao-specific (option, button)
├── naver/         # Naver-specific
├── rcs/           # RCS-specific
└── webhook/       # Delivery reports
```

### Naming
- Files: `snake_case.py`
- Classes: `PascalCase`
- Request suffix: `*Request` (e.g., `SendMessageRequest`)
- Response suffix: `*Response` (e.g., `SendMessageResponse`)

### Code Style (Ruff)
- Line length: 88
- Quote style: double
- Import sorting: isort (I rule)
- Target: Python 3.9+

### Tidy First Principles
- Never mix refactoring and feature changes in the same commit
- Tidy related code before making behavioral changes
- Tidying: guard clauses, dead code removal, rename, extract conditionals
- Separate tidying commits from feature commits

## ANTI-PATTERNS (THIS PROJECT)

### NEVER
- Add CLI/console scripts - this is library-only
- Create multiple service classes - all goes in `SolapiMessageService`
- Mix request/response models - they're deliberately separate
- Use dataclasses or TypedDict for API models - Pydantic only
- Hardcode credentials - use env vars

### VERSION SYNC REQUIRED
```python
# solapi/model/request/__init__.py
VERSION = "python/5.0.3"  # MUST update on every release!
```
Also update `pyproject.toml` version.

## UNIQUE PATTERNS

### Single Service Class
```python
# All API methods in one class (318 lines)
class SolapiMessageService:
    def send(...)           # SMS/LMS/MMS/Kakao/Naver/RCS
    def upload_file(...)    # Storage
    def get_balance(...)    # Account
    def get_groups(...)     # Message groups
    def get_messages(...)   # Message history
    def cancel_scheduled_message(...)
```

### Minimal Error Handling
- Only `MessageNotReceivedError` exists
- API errors raised as generic `Exception` with errorCode, errorMessage

### Authentication Flow
```
SolapiMessageService.__init__(api_key, api_secret)
  → Authenticator.get_auth_info()
  → HMAC-SHA256 signature
  → Authorization header
```

## COMMANDS

```bash
# Install
pip install solapi

# Dev setup
pip install -e ".[dev]"

# Lint & format
ruff check --fix .
ruff format .

# Test (requires env vars)
export SOLAPI_API_KEY="..."
export SOLAPI_API_SECRET="..."
export SOLAPI_SENDER="..."
export SOLAPI_RECIPIENT="..."
pytest

# Build
python -m build
```

## ENV VARS (Testing)

| Variable | Purpose |
|----------|---------|
| `SOLAPI_API_KEY` | API authentication |
| `SOLAPI_API_SECRET` | API authentication |
| `SOLAPI_SENDER` | Registered sender number |
| `SOLAPI_RECIPIENT` | Test recipient number |
| `SOLAPI_KAKAO_PF_ID` | Kakao business channel |
| `SOLAPI_KAKAO_TEMPLATE_ID` | Kakao template |

## NOTES

- No CI/CD pipeline - testing/linting is local only
- uv workspace includes Django webhook example
- Tests are integration tests (hit real API)
- Korean comments in some files (i18n TODO exists)
