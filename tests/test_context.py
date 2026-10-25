from pages.context_page import ContextPage


def test_context_click(page):
    url = "https://the-internet.herokuapp.com/context_menu"
    page.goto(url)

    context_page = ContextPage(page)

    def handle_dialog(dialog):
        assert dialog.message == "You selected a context menu"
        dialog.accept()

    page.once("dialog", handle_dialog)
    context_page.perform_context_click()
