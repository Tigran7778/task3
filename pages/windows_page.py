from playwright.sync_api import Page, BrowserContext
from ui.web_element import WebElement


class WindowsPage:
    def __init__(self, page: Page):
        self.page = page
        self.click_here_link = WebElement(
            self.page.get_by_role('link', name='Click Here'),
            description="Кнопка Click Here"
        )
        self.result_text_locator = WebElement(
            self.page.get_by_role('heading', name='New Window'),
            description="Отображаемый текст"
        )

    def click_open_new_window(self):
        self.click_here_link.click()  # Нажать на ссылку, которая открывает новую вкладку

    def get_new_page_from_context(self, context: BrowserContext):
        return context.wait_for_event("page")  # Получить новую страницу (вкладку), которая открылась после клика

    def get_displayed_text(self, page: Page) -> str:
        return page.locator('body').text_content()  # Получить текст, отображаемый на странице (ожидаем "New Window")

    def close_page(self, page_to_close: Page):
        page_to_close.close()  # Закрыть указанную вкладку

    def get_page_count(self, context: BrowserContext) -> int:
        return len(context.pages)  # Вернуть количество открытых вкладок в контексте
