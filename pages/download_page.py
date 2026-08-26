from playwright.sync_api import Page
from ui.web_element import WebElement


class DownloadPage:
    def __init__(self, page: Page):
        self.page = page
        self.files_list = WebElement(
            page.locator(".example a[href^='download/']"),
            description="Список файлов"
        )

    def get_third_file_name(self) -> str:
        third_link = self.files_list.locator.nth(2)
        return third_link.inner_text().strip()

    def download_third_file(self):
        third_link = self.files_list.locator.nth(2)
        with self.page.expect_download() as download_info:
            third_link.click()
        return download_info.value
