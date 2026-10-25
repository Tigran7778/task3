import pytest
from playwright.sync_api import sync_playwright
from pages.hovers_page import HoversPage


def test_user_hover_tooltips(page):
    url = "https://the-internet.herokuapp.com/hovers"
    page.goto(url)

    users_page = HoversPage(page)
    count = users_page.get_user_count()
    assert count > 0, f"Не найдено ни одной карточки пользователя (найдено: {count})"

    for i in range(count):
        card = users_page.get_card_by_index(i)
        text = users_page.hover_and_get_name_text(card)

        assert users_page.validate_format(text), (
            f"Неверный формат имени для пользователя #{i}. "
            f"Ожидался 'name: userN', получено: '{text}'"
        )
