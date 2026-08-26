import pytest
from pages.slider_page import SliderPage


def test_set_random_slider_value(page):
    url = "https://the-internet.herokuapp.com/horizontal_slider"
    page.goto(url)

    # Устанавливаем случайное значение через клавиатуру
    slider_page = SliderPage(page)
    target_value = slider_page.set_random_value()

    # Проверяем, что значение отобразилось корректно
    actual_value = float(slider_page.slider.get_attribute("value"))
    assert actual_value == target_value, (
        f"Значение не совпало: ожидалось {target_value}, получено {actual_value}"
    )
