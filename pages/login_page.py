from playwright.sync_api import Page
from ui.web_element import WebElement


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def get_message(self, response_status: int) -> str:
        if response_status != 200:
            raise AssertionError(f"Ошибка! Статус: {response_status}. Проверьте http_credentials.")
        content = self.page.content()
        if "congratulations" in content.lower():
            return "Success"
        raise AssertionError(f"Страница загружена, но сообщение не найдено.\n{content[:300]}")
