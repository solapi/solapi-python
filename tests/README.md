# SOLAPI Python SDK Tests

This directory contains unit tests for the SOLAPI Python SDK. The tests cover all the functionality demonstrated in the examples folder.

## Prerequisites

- Python 3.9 or higher
- pytest

## Setup

1. Install the required dependencies:
   ```bash
   pip install pytest
   ```

2. Set up environment variables for API credentials and test phone numbers:
   ```bash
   export SOLAPI_API_KEY="your_api_key"
   export SOLAPI_API_SECRET="your_api_secret"
   export SOLAPI_SENDER="your_registered_sender_number"
   export SOLAPI_RECIPIENT="recipient_phone_number"
   export SOLAPI_KAKAO_PF_ID="your_kakao_business_channel_id"
   export SOLAPI_KAKAO_TEMPLATE_ID="your_kakao_template_id"
   ```

   Alternatively, you can modify the `conftest.py` file to hardcode these values for testing purposes.

## Running Tests

To run all tests:
```bash
pytest
```

To run a specific test file:
```bash
pytest tests/test_balance.py
```

To run a specific test:
```bash
pytest tests/test_simple_send.py::TestSimpleSend::test_send_sms
```

To run tests with verbose output:
```bash
pytest -v
```

## Test Files

- `test_balance.py`: Tests for checking account balance
- `test_group.py`: Tests for message group operations
- `test_messages.py`: Tests for retrieving message information
- `test_simple_send.py`: Tests for sending various types of messages (SMS, MMS, Kakao Alimtalk, etc.)
- `test_storage.py`: Tests for file upload operations

## Notes

- The tests are designed to work with valid API credentials. If you provide invalid credentials, the tests will fail.
- Some tests (like Kakao Alimtalk) require specific setup in your SOLAPI account.
- The MMS and storage tests require the example image file to exist at `examples/images/example.jpg`.
- The tests are designed to be independent of each other, but they may create resources (like message groups) in your SOLAPI account.