from datetime import datetime, timedelta
from pathlib import Path

import pytest

from solapi.model import RequestMessage, SendRequestConfig
from solapi.model.kakao.kakao_option import KakaoOption
from solapi.model.request.storage import FileTypeEnum
from solapi.model.response.send_message_response import SendMessageResponse


class TestSimpleSend:
    """Test cases for simple message sending functionality."""

    def test_send_sms(self, message_service, test_phone_numbers):
        """
        Test sending a simple SMS message.

        This test verifies that the send method with a simple SMS message
        returns a valid response.

        Args:
            message_service: The SolapiMessageService fixture
            test_phone_numbers: Dictionary with sender and recipient phone numbers
        """
        # Create message
        message = RequestMessage(
            from_=test_phone_numbers["sender"],
            to=test_phone_numbers["recipient"],
            text="[테스트] SOLAPI Python SDK를 사용한 SMS 발송 테스트입니다.",
        )

        # Send message
        response = message_service.send(message)

        # Verify response type
        assert isinstance(response, SendMessageResponse)

        # Verify response has required fields
        assert hasattr(response, "group_info")
        assert hasattr(response.group_info, "group_id")
        assert hasattr(response.group_info, "count")

        # Verify message was sent successfully
        assert response.group_info.count.total > 0
        assert response.group_info.count.registered_success > 0

        # Print response information for verification
        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total messages: {response.group_info.count.total}")
        print(f"Successful messages: {response.group_info.count.registered_success}")
        print(f"Failed messages: {response.group_info.count.registered_failed}")

        return response.group_info.group_id

    def test_send_mms(self, message_service, test_phone_numbers):
        """
        Test sending an MMS message with an image.

        This test verifies that the upload_file and send methods for MMS
        return valid responses.

        Args:
            message_service: The SolapiMessageService fixture
            test_phone_numbers: Dictionary with sender and recipient phone numbers
        """
        # Get the path to the example image
        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )

        # Skip test if image doesn't exist
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        # Upload image file
        file_response = message_service.upload_file(
            file_path=str(image_path),
            upload_type=FileTypeEnum.MMS,
        )

        # Verify file upload response
        assert hasattr(file_response, "file_id")
        print(f"Uploaded file ID: {file_response.file_id}")

        # Create MMS message
        message = RequestMessage(
            from_=test_phone_numbers["sender"],
            to=test_phone_numbers["recipient"],
            text="[테스트] SOLAPI Python SDK를 사용한 MMS 발송 테스트입니다.",
            subject="MMS 테스트",
            image_id=file_response.file_id,
        )

        # Send message
        response = message_service.send(message)

        # Verify response type
        assert isinstance(response, SendMessageResponse)

        # Verify response has required fields
        assert hasattr(response, "group_info")
        assert hasattr(response.group_info, "group_id")
        assert hasattr(response.group_info, "count")

        # Verify message was sent successfully
        assert response.group_info.count.total > 0
        assert response.group_info.count.registered_success > 0

        # Print response information for verification
        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total messages: {response.group_info.count.total}")
        print(f"Successful messages: {response.group_info.count.registered_success}")
        print(f"Failed messages: {response.group_info.count.registered_failed}")

        return response.group_info.group_id

    def test_send_kakao_alimtalk(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """
        Test sending a Kakao Alimtalk message.

        This test verifies that the send method with Kakao options
        returns a valid response.

        Args:
            message_service: The SolapiMessageService fixture
            test_phone_numbers: Dictionary with sender and recipient phone numbers
            test_kakao_options: Dictionary with Kakao channel ID and template ID
        """
        # Create Kakao options
        kakao_option = KakaoOption(
            pf_id=test_kakao_options["pf_id"],
            template_id=test_kakao_options["template_id"],
        )

        # Create message
        message = RequestMessage(
            from_=test_phone_numbers["sender"],
            to=test_phone_numbers["recipient"],
            kakao_options=kakao_option,
        )

        # Send message
        try:
            response = message_service.send(message)

            # Verify response type
            assert isinstance(response, SendMessageResponse)

            # Verify response has required fields
            assert hasattr(response, "group_info")
            assert hasattr(response.group_info, "group_id")
            assert hasattr(response.group_info, "count")

            # Verify message was sent successfully
            assert response.group_info.count.total > 0
            assert response.group_info.count.registered_success > 0

            # Print response information for verification
            print(f"Group ID: {response.group_info.group_id}")
            print(f"Total messages: {response.group_info.count.total}")
            print(
                f"Successful messages: {response.group_info.count.registered_success}"
            )
            print(f"Failed messages: {response.group_info.count.registered_failed}")

            return response.group_info.group_id
        except Exception as e:
            # This test may fail if Kakao template is not properly set up
            pytest.skip(f"Kakao Alimtalk test skipped: {str(e)}")

    def test_send_many(self, message_service, test_phone_numbers):
        """
        Test sending multiple messages at once.

        This test verifies that the send method with multiple messages
        returns a valid response.

        Args:
            message_service: The SolapiMessageService fixture
            test_phone_numbers: Dictionary with sender and recipient phone numbers
        """
        # Create multiple messages
        messages = [
            RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                text="[테스트1] SOLAPI Python SDK를 사용한 대량 발송 테스트입니다.",
            ),
            RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                text="[테스트2] SOLAPI Python SDK를 사용한 대량 발송 테스트입니다.",
            ),
            RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                text="[테스트3] SOLAPI Python SDK를 사용한 대량 발송 테스트입니다.",
            ),
        ]

        # Create config with duplicates allowed
        config = SendRequestConfig(allow_duplicates=True)

        # Send messages
        response = message_service.send(messages, config)

        # Verify response type
        assert isinstance(response, SendMessageResponse)

        # Verify response has required fields
        assert hasattr(response, "group_info")
        assert hasattr(response.group_info, "group_id")
        assert hasattr(response.group_info, "count")

        # Verify messages were sent successfully
        assert response.group_info.count.total == 3
        assert response.group_info.count.registered_success > 0

        # Print response information for verification
        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total messages: {response.group_info.count.total}")
        print(f"Successful messages: {response.group_info.count.registered_success}")
        print(f"Failed messages: {response.group_info.count.registered_failed}")

        # Check for failed messages
        if response.failed_message_list:
            print("\nFailed messages:")
            for failed in response.failed_message_list:
                print(f"To: {failed.message.to}")
                print(f"Error: {failed.error.message}")

        return response.group_info.group_id

    def test_send_with_reservation(self, message_service, test_phone_numbers):
        """
        Test sending a message with a future reservation time.

        This test verifies that the send method with a scheduled date
        returns a valid response.

        Args:
            message_service: The SolapiMessageService fixture
            test_phone_numbers: Dictionary with sender and recipient phone numbers
        """
        # Create message
        message = RequestMessage(
            from_=test_phone_numbers["sender"],
            to=test_phone_numbers["recipient"],
            text="[테스트] SOLAPI Python SDK를 사용한 예약 발송 테스트입니다.",
        )

        # Create config with scheduled date (10 minutes in the future)
        scheduled_date = datetime.now() + timedelta(minutes=10)
        config = SendRequestConfig(scheduled_date=scheduled_date)

        # Send message with reservation
        response = message_service.send(message, config)

        # Verify response type
        assert isinstance(response, SendMessageResponse)

        # Verify response has required fields
        assert hasattr(response, "group_info")
        assert hasattr(response.group_info, "group_id")
        assert hasattr(response.group_info, "count")

        # Verify message was scheduled successfully
        assert response.group_info.count.total > 0
        assert response.group_info.count.registered_success > 0

        # Print response information for verification
        print(f"Group ID: {response.group_info.group_id}")
        print(f"Scheduled date: {scheduled_date}")
        print(f"Total messages: {response.group_info.count.total}")
        print(f"Successful messages: {response.group_info.count.registered_success}")
        print(f"Failed messages: {response.group_info.count.registered_failed}")

        return response.group_info.group_id
