from playwright.sync_api import sync_playwright
from pages.alerts_page import AlertsPage
import random
import string


def test_alerts(page):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    alerts_page = AlertsPage(page)
    page.goto(url)

    def generate_random_text(length=8):
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    entered_text = generate_random_text()

    def handle_dialog_alert(dialog):
        dialog.accept()

    def handle_dialog_confirm(d):
        d.accept()

    def handle_dialog_prompt(d):
        d.accept(entered_text)

    page.once("dialog", handle_dialog_alert)
    alerts_page.click_js_alert()

    page.once("dialog", handle_dialog_confirm)
    alerts_page.click_js_confirm()

    page.once("dialog", handle_dialog_prompt)
    alerts_page.click_js_prompt()

    result_text = alerts_page.get_result_text()

    expected_text = f"You entered: {entered_text}"
    assert expected_text in result_text, f"Текст не совпадает! Ожидали: '{expected_text}', получили: '{result_text}'"
