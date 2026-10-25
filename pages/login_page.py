from playwright.sync_api import Page
from ui.web_element import WebElement


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.message = WebElement(
            locator=page.locator("p"),
            description="Сообщение на странице"
        )

    def get_message_text(self) -> str:
        return self.message.get_inner_text().strip()
