import tempfile
from pathlib import Path
import pytest
from pages.upload_page import UploadPage


@pytest.fixture
def temp_txt_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp.write("Тестовый файл")
        tmp_path = tmp.name

    yield tmp_path
    Path(tmp_path).unlink(missing_ok=True)


def test_file_upload(page, temp_txt_file):
    page.goto("https://the-internet.herokuapp.com/upload")

    upload_page = UploadPage(page)
    upload_page.upload_file(temp_txt_file)

    message = upload_page.get_result_message()
    expected = "File Uploaded!"

    assert message == expected, \
        f"Сообщение не совпадает! Ожидалось: '{expected}', получено: '{message}'"
