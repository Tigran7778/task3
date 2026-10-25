from playwright.sync_api import Page
from ui.web_element import WebElement


class UploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_input_selector = WebElement(
            locator=page.locator('//*[@id="file-upload"]'),
            description="Выбор файла",
            page=page
        )
        self.result_message = WebElement(
            locator=page.locator('//h3[text()="File Uploaded!"]'),
            description="Текст File Uploaded!",
            page=page
        )
        self.upload_button_selector = WebElement(
            locator=page.locator('//*[@id="file-submit"]'),
            description="Кнопка upload",
            page=page
        )
        self.uploaded_file_name = WebElement(
            locator=page.locator('//*[@id="uploaded-files"]'),
            description="Имя файла",
            page=page
        )

    def upload_file(self, file_path: str) -> None:
        self.file_input_selector.set_input_files(file_path)
        self.upload_button_selector.click()

    def get_result_message(self) -> str:
        return self.result_message.get_inner_text()

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_name.get_inner_text()
