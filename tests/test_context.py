from pages.context_page import ContextPage


def test_context_click(page):
    url = "https://the-internet.herokuapp.com/context_menu"
    page.goto(url)

    # Создаем объект Page Object
    context_page = ContextPage(page)

    # Вызываем метод для контекстного клика
    context_page.perform_context_click()
