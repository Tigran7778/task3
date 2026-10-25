from pathlib import Path
from pages.download_page import DownloadPage
import tempfile


def test_download_third_file(page):
    url = "https://the-internet.herokuapp.com/download"
    page.goto(url)

    file_page = DownloadPage(page)

    file_index = 2
    expected_name = file_page.get_file_name(file_index)

    download = file_page.download_file(file_index)

    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / download.suggested_filename
        download.save_as(file_path)

        assert file_path.exists(), f"Файл не был сохранен: {file_path}"
        assert file_path.stat().st_size > 0, "Файл пустой"

        actual_name = download.suggested_filename
        assert actual_name == expected_name, \
            f"Имена не совпадают! Ожидалось: '{expected_name}', получено: '{actual_name}'"
