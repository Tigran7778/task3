from playwright.sync_api import Page, expect
from ui.multi_web_element import MultiWebElement


class ScrollPage:
    def __init__(self, page: Page):
        self.page = page
        self.blocks = MultiWebElement(
            page=page,
            locator=page.locator("div.jscroll-added:has(br)"),
            description="Абзацы"
        )

    def get_paragraphs_count(self) -> int:
        return self.blocks.count()

    def scroll_until(self, target: int, max_attempts: int = 30) -> int:
        for _ in range(max_attempts):
            count = self.get_paragraphs_count()
            if count >= target:
                return count
            self.blocks.last().scroll_into_view_if_needed()

            expect(self.blocks.locator).to_have_count(count + 1)

        return self.get_paragraphs_count()
