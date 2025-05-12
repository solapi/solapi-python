from solapi.model.response.balance.get_balance import GetBalanceResponse


class TestBalance:
    """Test cases for balance-related functionality."""

    def test_get_balance(self, message_service):
        """
        Test getting account balance.

        This test verifies that the get_balance method returns a valid response
        with balance and point information.

        Args:
            message_service: The SolapiMessageService fixture
        """
        # Get balance
        response = message_service.get_balance()

        # Verify response type
        assert isinstance(response, GetBalanceResponse)

        # Verify response has required fields
        assert hasattr(response, "balance")
        assert hasattr(response, "point")

        # Verify balance and point are numeric values
        assert isinstance(response.balance, (int, float))
        assert isinstance(response.point, (int, float))

        # Print balance information for verification
        print(f"Current balance: {response.balance} KRW")
        print(f"Current points: {response.point} points")
