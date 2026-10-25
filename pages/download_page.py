from playwright.sync_api import Page
from ui.multi_web_element import MultiWebElement


class DownloadPage:
    def __init__(self, page: Page):
        self.page = page
        self.files_list = MultiWebElement(
            page=page,
            locator=page.locator(".example a[href^='download/']"),
            description="Список файлов"
        )

    def get_file_name(self, index: int) -> str:
        link = self.files_list.nth(index)
        return link.get_inner_text().strip()

    def download_file(self, index: int) -> str:
        link = self.files_list.nth(index)
        with self.page.expect_download() as download_info:
            link.click()
        return download_info.value
