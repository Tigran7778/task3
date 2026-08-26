from playwright.sync_api import Page


class ImagesPage:
    def __init__(self, page: Page):
        self.page = page
        self._selector = "div.large-2.columns img"

    def wait_for_matching_images(self, max_attempts: int = 15) -> dict:
        for attempt in range(1, max_attempts + 1):
            # Получаем src первых 3 картинок
            srcs = [
                self.page.locator(self._selector).nth(i).get_attribute("src") or ""
                for i in range(3)
            ]

            # Проверка на дубликаты
            if len(set(srcs)) < len(srcs):
                return {"success": True, "attempts": attempt, "srcs": srcs}

            # Перезагрузка и ожидание полной загрузки
            self.page.reload()
            self.page.wait_for_load_state("load")

        # Возвращаем результат даже если не нашли совпадений
        final_srcs = [
            self.page.locator(self._selector).nth(i).get_attribute("src") or ""
            for i in range(3)
        ]
        return {"success": False, "attempts": max_attempts, "srcs": final_srcs}
