import os
from pathlib import Path
from pages.download_page import DownloadPage

# Папка для сохранения скачанных файлов
DOWNLOAD_DIR = Path("utils/files_cache")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


def test_download_third_file(page):
    url = "https://the-internet.herokuapp.com/download"
    page.goto(url)

    file_page = DownloadPage(page)

    # Получить имя третьего файла
    expected_name = file_page.get_third_file_name()
    assert expected_name, "Не удалось получить имя третьего файла. Список пуст?"
    print(f"Ожидаемое имя (с экрана): '{expected_name}'")

    # Скачать третий файл
    download = file_page.download_third_file()

    # Сохраняем файл на диск
    file_path = DOWNLOAD_DIR / download.suggested_filename
    download.save_as(file_path)

    # Проверить имя скачанного файла
    # Сравниваем имя, которое мы прочитали со страницы, с именем, которое предложил браузер
    actual_name = download.suggested_filename

    print(f"Реальное имя (от браузера): '{actual_name}'")

    assert actual_name == expected_name, \
        f"Имена не совпадают! Ожидалось: '{expected_name}', получено: '{actual_name}'"

    # Проверки существования и размера
    assert file_path.exists(), f"Файл не был сохранен по пути: {file_path}"
    assert file_path.stat().st_size > 0, "Скачанный файл пуст"
