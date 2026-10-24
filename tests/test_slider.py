import random
from playwright.sync_api import Page
from pages.slider_page import SliderPage


def test_slider_set_via_keyboard(page: Page):
    url = "https://the-internet.herokuapp.com/horizontal_slider"
    page.goto(url)

    slider_page = SliderPage(page)

    min_value = slider_page.get_min_value()
    max_value = slider_page.get_max_value()
    step = slider_page.get_step_value()

    possible_values = []
    current = min_value
    while current <= max_value:
        possible_values.append(round(current, 2))
        current += step

    non_boundary_values = [v for v in possible_values if v != min_value and v != max_value]

    target_value = random.choice(non_boundary_values)

    slider_page.set_value_via_keyboard(target_value)

    displayed_value = slider_page.get_displayed_value()

    assert displayed_value == target_value, (
        f"Значение не совпадает! Ожидалось: {target_value}, "
        f"получено: {displayed_value}"
    )
