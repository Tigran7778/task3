from pages.images_page import ImagesPage
from playwright.sync_api import expect


def test_find_matching_avatars(page):
    base_url = "https://the-internet.herokuapp.com/dynamic_content"
    page.goto(base_url)

    images_page = ImagesPage(page)

    # Обновлять, пока не найдутся 2 одинаковых
    result = images_page.wait_for_matching_images(max_attempts=15)

    # Проверка: если success=False, выводим понятную ошибку
    assert result["success"], (
        f"Не удалось найти совпадающие аватары за {result['attempts']} попыток.\n"
        f"Последние SRC: {result['srcs']}"
    )
    print(f"✅ Успех! Совпадения найдены за {result['attempts']} попыток.")
