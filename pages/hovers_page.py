from playwright.sync_api import Page, Locator
from ui.web_element import WebElement
import re


class HoversPage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.cards = WebElement(
            page.locator("//div[@class='figure']"),
            description="Карточки 3-х пользователей"
        )

    def get_user_count(self) -> int:
        return len(self.cards.locator.element_handles())

    def get_card_by_index(self, index: int) -> Locator:
        return self.cards.locator.nth(index)

    def hover_and_get_name_text(self, card: Locator) -> str:
        card.hover()

        # Находим элемент с именем внутри карточки
        name_element = card.locator(".figcaption h5")

        return name_element.inner_text()

    @staticmethod
    def validate_format(text: str) -> bool:
        """Проверяет формат 'name: userN'"""
        pattern = r"^name:\s*user\d+$"
        return re.fullmatch(pattern, text) is not None
