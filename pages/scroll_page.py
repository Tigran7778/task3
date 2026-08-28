from playwright.sync_api import Page
from ui.multi_web_element import MultiWebElement


class ScrollPage:
    def __init__(self, page: Page):
        self.page = page
        self.blocks = MultiWebElement(
            page=page,
            locator=page.locator("div.jscroll-added"),
            description="Абзацы"
        )

    def scroll_down(self):
        last_block = self.blocks.last()
        last_block.scroll_into_view_if_needed()

    def wait_until_count(self, min_count: int, max_attempts: int = 50) -> int:
        for _ in range(max_attempts):
            count = self.blocks.count()
            if count >= min_count:
                return count
            self.scroll_down()
        return self.blocks.count()
