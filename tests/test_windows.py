from pages.windows_page import WindowsPage


def test_multiple_windows(page, context):
    url = "https://the-internet.herokuapp.com/windows"
    page.goto(url)

    windows_page = WindowsPage(page)
    original_page = page
    target_text = "New Window"

    windows_page.click_open_new_window()

    new_page_1 = context.wait_for_event("page")

    windows_page_new_1 = WindowsPage(new_page_1)
    text_1 = windows_page_new_1.get_displayed_text()
    assert text_1 == target_text, \
        f"Ожидалось: '{target_text}', получено: '{text_1}'"
    original_page.bring_to_front()
    windows_page.click_open_new_window()
    new_page_2 = context.wait_for_event("page")

    windows_page_new_2 = WindowsPage(new_page_2)
    text_2 = windows_page_new_2.get_displayed_text()
    assert text_2 == target_text, \
        f"Ожидалось: '{target_text}', получено: '{text_2}'"
    original_page.bring_to_front()

    new_page_1.close()
    new_page_2.close()

    assert len(context.pages) == 1, \
        f"Ожидается 1 вкладка, открыто: {len(context.pages)}"
