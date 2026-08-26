from pages.scroll_page import ScrollPage


def test_scroll_until_10_blocks(page):
    url = "https://the-internet.herokuapp.com/infinite_scroll"
    page.goto(url)

    scroll_page = ScrollPage(page)
    success, count = scroll_page.wait_until_count(min_count=10)

    assert success, f"Не набрали 10 блоков. Сейчас: {count}"
    print(f"✅ Пройдено! Найдено блоков: {count}")
