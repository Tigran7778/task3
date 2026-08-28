from playwright.sync_api import Page
from ui.web_element import WebElement


class FramesPage:
    def __init__(self, page):
        self.page = page

        self.left_frame= WebElement(
            locator=page.frame(name="frame-left").locator("body"),
            description="Left Frame",
        )
        self.right_frame= WebElement(
            locator=page.frame(name="frame-right").locator("body"),
            description="Right Frame",
        )
        self.bottom_frame= WebElement(
            locator=page.frame(name="frame-bottom").locator("body"),
            description="Bottom Frame",
        )
        self.middle_frame= WebElement(
            locator=page.frame(name="frame-middle").locator("body"),
            description="Top Frame",
        )

    def get_left_frame_text(self) -> str:
        return self.left_frame.get_inner_text().strip()

    def get_middle_frame_text(self) -> str:
        return self.middle_frame.get_inner_text().strip()

    def get_right_frame_text(self) -> str:
        return self.right_frame.get_inner_text().strip()

    def get_bottom_frame_text(self) -> str:
        return self.bottom_frame.get_inner_text().strip()
