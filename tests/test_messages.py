from datetime import datetime, timedelta

from solapi.model.request.messages.get_messages import GetMessagesRequest
from solapi.model.response.messages.get_messages import GetMessagesResponse


class TestMessages:
    """Test cases for message-related functionality."""

    def test_get_messages(self, message_service):
        """
        Test getting messages without any filters.

        This test verifies that the get_messages method returns a valid response
        with message information.

        Args:
            message_service: The SolapiMessageService fixture
        """
        # Get messages
        response = message_service.get_messages()

        # Verify response type
        assert isinstance(response, GetMessagesResponse)

        # Verify response has required fields
        assert hasattr(response, "message_list")

        # Print message information for verification
        print(f"Messages in response: {len(response.message_list)}")

        # If there are messages, verify the structure of the first message
        if response.message_list:
            for message in response.message_list.values():
                print(f"Message ID: {message.message_id}")
                print(f"Status: {message.status_code}")
                print(f"To: {message.to}")
                print(f"From: {message.from_}")

    def test_get_messages_with_date_filter(self, message_service):
        """
        Test getting messages with date filters.

        This test verifies that the get_messages method with date filters
        returns a valid response with filtered message information.

        Args:
            message_service: The SolapiMessageService fixture
        """
        # Create date range for the last 7 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

        # Format dates as strings
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        # Create request with date filter
        request = GetMessagesRequest(start_date=start_date_str, end_date=end_date_str)

        # Get messages with filter
        response = message_service.get_messages(request)

        # Verify response type
        assert isinstance(response, GetMessagesResponse)

        # Verify response has required fields
        assert hasattr(response, "message_list")

        # Print message information for verification
        print(f"Messages in response: {len(response.message_list)}")

        # If there are messages, verify the structure of the first message
        if response.message_list:
            for message in response.message_list.values():
                print(f"Message ID: {message.message_id}")
                print(f"Status: {message.status_code}")
                print(f"To: {message.to}")
                print(f"From: {message.from_}")
