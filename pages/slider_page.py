from playwright.sync_api import Page
from ui.web_element import WebElement


class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.slider = WebElement(
            locator=page.locator('input[type="range"]'),
            description="Горизонтальный слайдер",
            page=page
        )
        self.value_display = WebElement(
            locator=page.locator('#range'),
            description="Текущее значение слайдера",
            page=page
        )

    def get_step_value(self) -> float:
        step_attr = self.slider.get_attribute("step")
        return float(step_attr)

    def get_min_value(self) -> float:
        min_attr = self.slider.get_attribute("min")
        return float(min_attr)

    def get_max_value(self) -> float:
        max_attr = self.slider.get_attribute("max")
        return float(max_attr)

    def set_value_via_keyboard(self, target_value: float) -> None:
        current_text = self.value_display.get_text_content()
        current_value = float(current_text)

        step = self.get_step_value()

        diff = target_value - current_value
        steps_count = int(abs(diff) / step)

        key = "ArrowRight" if diff > 0 else "ArrowLeft"
        for _ in range(steps_count):
            self.slider.press(key)

    def get_displayed_value(self) -> float:
        text = self.value_display.get_text_content()
        return float(text)