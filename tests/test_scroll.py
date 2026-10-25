from pages.scroll_page import ScrollPage


def test_infinite_scroll(page):
    page.goto("https://the-internet.herokuapp.com/infinite_scroll")

    scroll_page = ScrollPage(page)
    expected_count = 10
    actual_count = scroll_page.scroll_until(target=expected_count)

    assert actual_count >= expected_count, \
        f"Ожидалось: >= {expected_count} блоков, получено: {actual_count} блоков"
