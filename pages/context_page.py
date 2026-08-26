from playwright.sync_api import Page
from ui.web_element import WebElement


class ContextPage:
    def __init__(self, page: Page):
        self.page = page

        self.target_selector = WebElement(
            self.page.locator('//*[@id="hot-spot"]'),
            description="Область действия"
        )

    def perform_context_click(self):
        self.target_selector.right_click()
