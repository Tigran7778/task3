from playwright.sync_api import Page
from ui.web_element import WebElement


class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.slider = WebElement(
            locator=page.locator('input[type="range"]'),
            description="Горизонтальный слайдер"
        )
        self.value_display = WebElement(
            locator=page.locator('#range'),
            description="Текущее значение слайдера"
        )

    def set_value_via_keyboard(self, target_value: float) -> None:
        current_text = self.value_display.get_text_content()
        current_value = float(current_text)

        step = 0.5

        diff = target_value - current_value
        steps_count = int(abs(diff) / step)

        if diff > 0:
            key = "ArrowRight"
        else:
            key = "ArrowLeft"
        for _ in range(steps_count):
            self.slider.locator.press(key)

    def get_displayed_value(self) -> float:
        text = self.value_display.get_text_content()
        return float(text)
