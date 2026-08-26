from playwright.sync_api import Page


class ScrollPage:
    def __init__(self, page: Page):
        self.page = page
        self.blocks = page.locator("div.jscroll-added")

    def scroll_and_wait(self):
        # Скроллим на один экран вниз
        self.page.evaluate("window.scrollBy(0, window.innerHeight)")
        # Даём время на подгрузку (для демо-теста этого хватит)
        self.page.wait_for_timeout(1500)

    def wait_until_count(self, min_count: int, max_attempts: int = 20):
        for attempt in range(max_attempts):
            count = self.blocks.count()
            if count >= min_count:
                return True, count
            self.scroll_and_wait()
        return False, self.blocks.count()
