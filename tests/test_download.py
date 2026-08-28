from pathlib import Path
from pages.download_page import DownloadPage

DOWNLOAD_DIR = Path("utils/files_cache")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


def test_download_third_file(page):
    url = "https://the-internet.herokuapp.com/download"
    page.goto(url)

    file_page = DownloadPage(page)

    file_index = 2
    expected_name = file_page.get_file_name(file_index)

    download = file_page.download_file(file_index)

    file_path = DOWNLOAD_DIR / download.suggested_filename
    download.save_as(file_path)

    actual_name = download.suggested_filename
    assert actual_name == expected_name, \
        f"Имена не совпадают! Ожидалось: '{expected_name}', получено: '{actual_name}'"
