import pytest
from playwright.sync_api import Page
from pages.upload_page import UploadPage


def test_file_upload(page: Page):
    url = "https://the-internet.herokuapp.com/upload"
    page.goto(url)

    upload_page = UploadPage(page)

    file_path = "utils/test-file.txt"
    upload_page.upload_file(file_path)

    message = upload_page.get_result_message()
    assert message == "File Uploaded!", f"Unexpected message: {message}"
