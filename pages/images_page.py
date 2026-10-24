from playwright.sync_api import Page
from ui.multi_web_element import MultiWebElement


class ImagesPage:
    def __init__(self, page: Page):
        self.page = page
        self.images = MultiWebElement(
            page=page,
            locator=page.locator("div.large-2.columns img"),
            description="Изображения"
        )

    def wait_for_matching_images(self, max_attempts: int = 15) -> dict:
        for attempt in range(1, max_attempts + 1):
            srcs = []
            for i in range(3):
                image = self.images.nth(i)
                srcs.append(image.get_attribute("src") or "")

            if len(set(srcs)) < len(srcs):
                return {"success": True, "attempts": attempt, "srcs": srcs}

            self.page.reload()

        final_srcs = []
        for image in self.images.all():
            final_srcs.append(image.get_attribute("src") or "")

        return {"success": False, "attempts": max_attempts, "srcs": final_srcs}
