import pytest

from solapi.model.response.groups.get_group_messages import GetGroupMessagesResponse
from solapi.model.response.groups.get_groups import GetGroupsResponse


class TestGroup:
    """Test cases for group-related functionality."""

    def test_get_groups(self, message_service):
        """
        Test getting message groups.

        This test verifies that the get_groups method returns a valid response
        with group information.

        Args:
            message_service: The SolapiMessageService fixture
        """
        # Get groups
        response = message_service.get_groups()

        # Verify response type
        assert isinstance(response, GetGroupsResponse)

        # Verify response has required fields
        assert hasattr(response, "group_list")

        # Print group information for verification
        print(f"Number of groups: {len(response.group_list)}")

        # If there are groups, verify the structure of the first group
        if response.group_list:
            group_id = next(iter(response.group_list))
            group = response.group_list[group_id]

            print(f"Group ID: {group_id}")
            print(f"Created: {group.date_created}")
            print(f"Status: {group.status}")

            # Test get_group method with this group ID
            self.test_get_group(message_service, group_id)

    def test_get_group(self, message_service, group_id=None):
        """
        Test getting a specific message group.

        This test verifies that the get_group method returns a valid response
        with detailed information about a specific group.

        Args:
            message_service: The SolapiMessageService fixture
            group_id: Optional group ID to test. If not provided, the test will be skipped.
        """
        if group_id is None:
            pytest.skip("No group ID provided")

        # Get specific group
        response = message_service.get_group(group_id)

        # Verify response has required fields
        assert hasattr(response, "group_id")
        assert hasattr(response, "date_created")
        assert hasattr(response, "status")

        # Print group details for verification
        print(f"Group details - ID: {response.group_id}")
        print(f"Group details - Created: {response.date_created}")
        print(f"Group details - Status: {response.status}")

        # Test get_group_messages method with this group ID
        self.test_get_group_messages(message_service, group_id)

    def test_get_group_messages(self, message_service, group_id=None):
        """
        Test getting messages in a specific group.

        This test verifies that the get_group_messages method returns a valid response
        with messages belonging to a specific group.

        Args:
            message_service: The SolapiMessageService fixture
            group_id: Optional group ID to test. If not provided, the test will be skipped.
        """
        if group_id is None:
            pytest.skip("No group ID provided")

        # Get messages in the group
        response = message_service.get_group_messages(group_id)

        # Verify response type
        assert isinstance(response, GetGroupMessagesResponse)

        # Verify response has required fields
        assert hasattr(response, "messages")

        # Print message information for verification
        print(f"Number of messages in group: {len(response.messages)}")

        # If there are messages, verify the structure of the first message
        if response.messages:
            message = response.messages[0]
            print(f"Message ID: {message.message_id}")
            print(f"Status: {message.status}")
            print(f"To: {message.to}")
            print(f"From: {message.from_}")
