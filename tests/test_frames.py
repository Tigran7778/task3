from pages.frames_page import FramesPage
from playwright.sync_api import expect


def test_frames_flow(page):
    base_url = "https://the-internet.herokuapp.com/nested_frames"
    page.goto(base_url)

    frames_page = FramesPage(page)

    # Левый фрейм
    left_text = frames_page.get_left_frame_text().strip()
    assert left_text == "LEFT", f"Ожидалось 'LEFT', но было: '{left_text}'"
    print(f"✅ Шаг 1 пройден: текст левого фрейма = '{left_text}'")

    # ШАГ 3: Центральный фрейм (был пропущен ранее)
    middle_text = frames_page.get_middle_frame_text().strip()
    assert middle_text == "MIDDLE", f"Ожидалось 'MIDDLE', но было: '{middle_text}'"
    print(f"✅ Шаг 2 пройден: текст центрального фрейма = '{middle_text}'")

    # ШАГ 4: Правый фрейм
    right_text = frames_page.get_right_frame_text().strip()
    assert right_text == "RIGHT", f"Ожидалось 'RIGHT', но было: '{right_text}'"
    print(f"✅ Шаг 3 пройден: текст правого фрейма = '{right_text}'")

    # ШАГ 5: Нижний фрейм
    bottom_text = frames_page.get_bottom_frame_text().strip()
    assert bottom_text == "BOTTOM", f"Ожидалось 'BOTTOM', но было: '{bottom_text}'"
    print(f"✅ Шаг 4 пройден: текст нижнего фрейма = '{bottom_text}'")
