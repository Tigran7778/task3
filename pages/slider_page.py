from ui.web_element import WebElement
import random


class SliderPage:
    def __init__(self, page):
        self.page = page
        self.slider = WebElement(
            page.locator("//input[@type='range']"),
            description="Slider"
        )
        self.value_display = WebElement(
            page.locator("//*[@id='range']"),
            description="Value display"
        )

    def set_random_value(self):
        # 1. Получаем параметры слайдера (один раз)
        min_val = float(self.slider.get_attribute("min"))
        max_val = float(self.slider.get_attribute("max"))
        step_str = self.slider.get_attribute("step")
        step = float(step_str) if step_str else 0.5

        # 2. Генерируем целевое значение (не на границах)
        # round(value / step) * step — гарантирует, что значение кратно шагу
        target_value = random.uniform(min_val + step, max_val - step)
        target_value = round(round(target_value / step) * step, 2)

        # 3. Получаем текущее значение
        current_value = float(self.slider.get_attribute("value"))

        # 4. Вычисляем, сколько шагов нужно сделать
        diff = target_value - current_value
        steps_to_move = int(round(abs(diff) / step))

        if steps_to_move == 0:
            return current_value

        # 5. Фокусируемся и эмулируем нажатия
        self.slider.locator.focus()
        key = "ArrowRight" if diff > 0 else "ArrowLeft"

        for _ in range(steps_to_move):
            self.page.keyboard.press(key)

        # Возвращаем итоговое значение (для проверки в тесте)
        final_value = float(self.slider.get_attribute("value"))
        return final_value
