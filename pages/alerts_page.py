from playwright.sync_api import Page
from ui.web_element import WebElement
import random
import string


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page

        self.alert_button = WebElement(
            locator=page.get_by_role("button", name="Click for JS Alert"),
            description="Кнопка JS Alert"
        )
        self.confirm_button = WebElement(
            locator=page.get_by_role("button", name="Click for JS Confirm"),
            description="Кнопка JS Confirm"
        )
        self.prompt_button = WebElement(
            locator=page.get_by_role("button", name="Click for JS Prompt"),
            description="Кнопка JS Prompt"
        )
        self.result_section = WebElement(
            locator=page.locator("#result"),
            description="Секция результата",
            page=page
        )

    def generate_random_text(self, length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def click_js_alert(self):
        self.alert_button.click()

    def click_js_confirm(self):
        self.confirm_button.click()

    def click_js_prompt(self):
        self.prompt_button.click()

    def get_result_text(self):
        return self.result_section.get_text_content()
