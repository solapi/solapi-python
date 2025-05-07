from pathlib import Path

import pytest

from solapi.model.request.storage import FileTypeEnum
from solapi.model.response.storage import FileUploadResponse


class TestStorage:
    """Test cases for storage-related functionality."""

    def test_upload_file_mms(self, message_service):
        """
        Test uploading a file for MMS.

        This test verifies that the upload_file method returns a valid response
        when uploading a file for MMS.

        Args:
            message_service: The SolapiMessageService fixture
        """
        # Get the path to the example image
        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )

        # Skip test if image doesn't exist
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        # Upload file
        response = message_service.upload_file(
            file_path=str(image_path),
            upload_type=FileTypeEnum.MMS,
        )

        # Verify response type
        assert isinstance(response, FileUploadResponse)

        # Verify response has required fields
        assert hasattr(response, "file_id")
        assert hasattr(response, "name")
        assert hasattr(response, "date_created")

        # Print file information for verification
        print(f"File ID: {response.file_id}")
        print(f"File name: {response.name}")
        print(f"File created: {response.date_created}")

        return response.file_id

    def test_upload_file_kakao(self, message_service):
        """
        Test uploading a file for Kakao.

        This test verifies that the upload_file method returns a valid response
        when uploading a file for Kakao.

        Args:
            message_service: The SolapiMessageService fixture
        """
        # Get the path to the example image
        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )

        # Skip test if image doesn't exist
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        # Upload file
        response = message_service.upload_file(
            file_path=str(image_path),
            upload_type=FileTypeEnum.KAKAO,
        )

        # Verify response type
        assert isinstance(response, FileUploadResponse)

        # Verify response has required fields
        assert hasattr(response, "file_id")
        assert hasattr(response, "name")
        assert hasattr(response, "date_created")

        # Print file information for verification
        print(f"File ID: {response.file_id}")
        print(f"File name: {response.name}")
        print(f"File created: {response.date_created}")

        return response.file_id

    def test_upload_file_document(self, message_service):
        """
        Test uploading a file as a document.

        This test verifies that the upload_file method returns a valid response
        when uploading a file as a document.

        Args:
            message_service: The SolapiMessageService fixture
        """
        # Get the path to the example image (using as a document for test purposes)
        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )

        # Skip test if image doesn't exist
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        # Upload file
        response = message_service.upload_file(
            file_path=str(image_path),
            upload_type=FileTypeEnum.DOCUMENT,
        )

        # Verify response type
        assert isinstance(response, FileUploadResponse)

        # Verify response has required fields
        assert hasattr(response, "file_id")
        assert hasattr(response, "name")
        assert hasattr(response, "date_created")

        # Print file information for verification
        print(f"File ID: {response.file_id}")
        print(f"File name: {response.name}")
        print(f"File created: {response.date_created}")

        return response.file_id
