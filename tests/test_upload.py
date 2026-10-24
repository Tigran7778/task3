import tempfile
from pathlib import Path
import pytest
from playwright.sync_api import Page
from pages.upload_page import UploadPage


def test_file_upload(page: Page):
    url = "https://the-internet.herokuapp.com/upload"
    page.goto(url)

    upload_page = UploadPage(page)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp.write("Тестовый файл")
        tmp_path = tmp.name

    try:
        upload_page.upload_file(tmp_path)
        message = upload_page.get_result_message()
        expected = "File Uploaded!"

        assert message == expected, \
            f"Сообщение не совпадает! Ожидалось: '{expected}', получено: '{message}'"

    finally:
        Path(tmp_path).unlink(missing_ok=True)
