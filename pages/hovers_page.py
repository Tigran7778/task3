from playwright.sync_api import Page
from ui.web_element import WebElement
from ui.multi_web_element import MultiWebElement
import re


class HoversPage:
    def __init__(self, page: Page):
        self.page = page
        self.cards = MultiWebElement(
            page=page,
            locator=page.locator("//div[contains(@class, 'figure')]"),
            description="Карточки 3-х пользователей"
        )

    def _get_name_element(self, card: WebElement) -> WebElement:
        return WebElement(
            locator=card.locator.locator(".figcaption h5"),
            description="Имя в карточке"
        )

    def get_user_count(self) -> int:
        return self.cards.count()

    def get_card_by_index(self, index: int) -> WebElement:
        return self.cards.nth(index)

    def hover_and_get_name_text(self, card: WebElement) -> str:
        card.hover()
        return self._get_name_element(card).get_inner_text()

    def get_user_names(self) -> list[str]:
        names = []
        for card in self.cards:
            names.append(self._get_name_element(card).get_inner_text())
        return names

    @staticmethod
    def validate_format(text: str) -> bool:
        """Проверяет формат 'name: userN'"""
        pattern = r"^name:\s*user\d+$"
        return re.fullmatch(pattern, text) is not None
