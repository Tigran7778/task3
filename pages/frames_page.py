from playwright.sync_api import Page


class FramesPage:
    def __init__(self, page):
        self.page = page

    def get_left_frame_text(self) -> str:
        frame = self.page.frame(name="frame-left")
        if not frame:
            raise Exception("Фрейм 'frame-left' не найден")
        return frame.inner_text("body").strip()

    def get_middle_frame_text(self) -> str:
        # Теперь этот метод есть! И имя совпадает с заданием
        frame = self.page.frame(name="frame-middle")
        if not frame:
            raise Exception("Фрейм 'frame-middle' не найден")
        return frame.inner_text("body").strip()

    def get_right_frame_text(self) -> str:
        frame = self.page.frame(name="frame-right")
        if not frame:
            raise Exception("Фрейм 'frame-right' не найден")
        return frame.inner_text("body").strip()

    def get_bottom_frame_text(self) -> str:
        # Теперь этот метод тоже есть, и имя 'frame-bottom' как в задании
        frame = self.page.frame(name="frame-bottom")
        if not frame:
            raise Exception("Фрейм 'frame-bottom' не найден")
        return frame.inner_text("body").strip()
