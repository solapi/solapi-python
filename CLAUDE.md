# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python SDK for SOLAPI messaging platform. Sends SMS/LMS/MMS/Kakao/Naver/RCS messages in Korea. Thin wrapper around REST API using httpx + Pydantic v2.

## Commands

```bash
# Dev setup
pip install -e ".[dev]"

# Lint & format
ruff check --fix .
ruff format .

# Test (requires env vars - see below)
pytest
pytest tests/test_balance.py  # Single file
pytest -v                      # Verbose

# Build
python -m build
```

## Testing Environment Variables

Tests are integration tests that hit the real API:

| Variable | Purpose |
|----------|---------|
| `SOLAPI_API_KEY` | API authentication |
| `SOLAPI_API_SECRET` | API authentication |
| `SOLAPI_SENDER` | Registered sender number |
| `SOLAPI_RECIPIENT` | Test recipient number |
| `SOLAPI_KAKAO_PF_ID` | Kakao business channel |
| `SOLAPI_KAKAO_TEMPLATE_ID` | Kakao template |

## Architecture

### Package Structure
```
solapi/
├── services/        # message_service.py - single SolapiMessageService class
├── model/           # Pydantic models (see solapi/model/AGENTS.md)
│   ├── request/     # Outbound API payloads
│   ├── response/    # Inbound API responses (deliberately separate)
│   ├── kakao/       # Kakao channel models
│   ├── naver/       # Naver channel models
│   ├── rcs/         # RCS channel models
│   └── webhook/     # Delivery reports
├── lib/             # authenticator.py, fetcher.py
└── error/           # MessageNotReceivedError only
```

### Key Design Decisions

**Single Service Class**: All 10 API methods live in `SolapiMessageService` - do not create additional service classes.

**Request/Response Separation**: Request and response models are deliberately separate and should never be shared, even for similar fields.

**Pydantic Everywhere**: All API models use Pydantic BaseModel with field aliases for camelCase API compatibility:
```python
pf_id: str = Field(alias="pfId")
```

**Phone Number Normalization**: Use `@field_validator` to strip dashes from phone numbers.

### Version Sync Required

When releasing, update version in BOTH locations:
- `pyproject.toml` → `version = "X.Y.Z"`
- `solapi/model/request/__init__.py` → `VERSION = "python/X.Y.Z"`

## Code Style

- **Linter**: Ruff (line-length: 88, double quotes, isort)
- **Target**: Python 3.9+
- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Request/Response suffixes**: `*Request`, `*Response`

## Tidy First Principles

Follow Kent Beck's "Tidy First?" principles:

### Separate Changes
- Never mix **structural changes** (refactoring) with **behavioral changes** (features/fixes) in the same commit
- Order: tidying commit → feature commit

### Tidy First
Tidy the relevant code area before making behavioral changes:
- Use guard clauses to reduce nesting
- Remove dead code
- Rename for clarity
- Extract complex conditionals

### Small Steps
- Keep tidying changes small and safe
- One tidying per commit
- Maintain passing tests

## Key Locations

| Task | Location |
|------|----------|
| Send messages | `solapi/services/message_service.py` |
| Request models | `solapi/model/request/` |
| Response models | `solapi/model/response/` |
| Kakao/Naver/RCS | `solapi/model/{kakao,naver,rcs}/` |
| Authentication | `solapi/lib/authenticator.py` |
| HTTP client | `solapi/lib/fetcher.py` |
| Test fixtures | `tests/conftest.py` |
| Usage examples | `examples/simple/` |

## Anti-Patterns

- Do not add CLI/console scripts - this is library-only
- Do not create multiple service classes
- Do not mix request/response models
- Do not use dataclasses or TypedDict for API models - Pydantic only
- Do not hardcode credentials
