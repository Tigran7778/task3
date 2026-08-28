from playwright.sync_api import Page, expect
from ui.web_element import WebElement


class UploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_input_selector = WebElement(
            page.locator('//*[@id="file-upload"]'),
            description="Выбор файла"
        )
        self.result_message = WebElement(
            page.locator('//h3[text()="File Uploaded!"]'),
            description="Текст File Uploaded!"
        )
        self.upload_button_selector = WebElement(
            page.locator('//*[@id="file-submit"]'),
            description="Кнопка upload"
        )
        self.uploaded_file_name = WebElement(
            page.locator('//*[@id="uploaded-files"]'),
            description="Имя файла"
        )

    def upload_file(self, file_path: str):
        self.file_input_selector.locator.set_input_files(file_path)
        self.upload_button_selector.locator.click()

    def get_result_message(self) -> str:
        return self.result_message.get_inner_text()

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_name.get_inner_text()
