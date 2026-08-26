import pytest
from playwright.sync_api import sync_playwright
from pages.hovers_page import HoversPage

BASE_URL = "https://the-internet.herokuapp.com/hovers"


def test_user_hover_tooltips(page):
    page.goto(BASE_URL)

    users_page = HoversPage(page)
    count = users_page.get_user_count()

    assert count > 0, f"Не найдено ни одной карточки пользователя (найдено: {count})"

    for i in range(count):
        card = users_page.get_card_by_index(i)

        # Получить текст
        text = users_page.hover_and_get_name_text(card)

        # Проверка формата
        assert users_page.validate_format(text), (
            f"Неверный формат имени для пользователя #{i}. "
            f"Ожидался 'name: userN', получено: '{text}'"
        )
