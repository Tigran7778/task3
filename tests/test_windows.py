from pages.windows_page import WindowsPage
from playwright.sync_api import BrowserContext, Page


def test_multiple_windows_flow(page: Page, context: BrowserContext):
    base_url = "https://the-internet.herokuapp.com/windows"
    target_text = "New Window"

    mw_page = WindowsPage(page)
    page.goto(base_url)

    original_page = page  # Сохраняем ссылку на первую вкладку

    # Нажать на ссылку Click Here
    mw_page.click_open_new_window()

    # Переключиться на новую вкладку
    new_page_1 = mw_page.get_new_page_from_context(context)

    # Получить текст, отображаемый на странице
    text_1 = mw_page.get_displayed_text(new_page_1)
    assert target_text in text_1, f"Ожидался текст '{target_text}', но было: {text_1}"
    print(f"Шаг 4 пройден: найден текст '{target_text}'")

    # Вернуться на вкладку из шага 1
    original_page.bring_to_front()

    # Нажать на ссылку Click Here (на главной вкладке)
    mw_page.click_open_new_window()

    # Переключиться на новую вкладку
    new_page_2 = mw_page.get_new_page_from_context(context)

    # Получить текст, отображаемый на странице
    text_2 = mw_page.get_displayed_text(new_page_2)
    assert target_text in text_2, f"Ожидался текст '{target_text}', но было: {text_2}"
    print(f"Шаг 8 пройден: найден текст '{target_text}'")

    # Вернуться на вкладку из шага 1
    original_page.bring_to_front()

    # Закрыть вкладку, открытую на шаге 3
    mw_page.close_page(new_page_1)

    # Закрыть вкладку, открытую на шаге 7
    mw_page.close_page(new_page_2)

    # Проверить количество открытых вкладок
    remaining_count = mw_page.get_page_count(context)
    assert remaining_count == 1, f"Ожидается 1 вкладка, но открыто: {remaining_count}"
