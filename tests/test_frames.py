from pages.frames_page import FramesPage
from playwright.sync_api import expect


def test_frames_flow(page):
    base_url = "https://the-internet.herokuapp.com/nested_frames"
    page.goto(base_url)

    frames_page = FramesPage(page)

    left_text = frames_page.get_left_frame_text().strip()
    assert left_text == "LEFT", f"Ожидалось 'LEFT', но было: '{left_text}'"

    middle_text = frames_page.get_middle_frame_text().strip()
    assert middle_text == "MIDDLE", f"Ожидалось 'MIDDLE', но было: '{middle_text}'"

    right_text = frames_page.get_right_frame_text().strip()
    assert right_text == "RIGHT", f"Ожидалось 'RIGHT', но было: '{right_text}'"

    bottom_text = frames_page.get_bottom_frame_text().strip()
    assert bottom_text == "BOTTOM", f"Ожидалось 'BOTTOM', но было: '{bottom_text}'"
