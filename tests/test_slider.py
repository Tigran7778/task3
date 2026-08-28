import random
from playwright.sync_api import Page
from pages.slider_page import SliderPage


def test_slider_set_via_keyboard(page: Page):
    url = "https://the-internet.herokuapp.com/horizontal_slider"
    page.goto(url)

    slider_page = SliderPage(page)

    possible_values = [x * 0.5 for x in range(0, 11)]

    non_boundary_values = [v for v in possible_values if v != 0.0 and v != 5.0]

    target_value = random.choice(non_boundary_values)

    slider_page.set_value_via_keyboard(target_value)

    displayed_value = slider_page.get_displayed_value()

    assert displayed_value == target_value, (
        f"Значение не совпадает! Ожидалось: {target_value}, "
        f"получено: {displayed_value}"
    )
