from playwright.sync_api import Page
from ui.web_element import WebElement


class WindowsPage:
    def __init__(self, page: Page):
        self.page = page
        self.click_here_link = WebElement(
            page.get_by_role('link', name='Click Here'),
            description="Кнопка Click Here"
        )
        self.result_text = WebElement(
            page.get_by_role('heading', name='New Window'),
            description="Отображаемый текст"
        )

    def click_open_new_window(self):
        self.click_here_link.click()

    def get_displayed_text(self) -> str:
        return self.result_text.get_inner_text()
