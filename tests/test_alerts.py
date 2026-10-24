from playwright.sync_api import sync_playwright
from pages.alerts_page import AlertsPage
from faker import Faker

fake = Faker()

def test_alerts(page):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    alerts_page = AlertsPage(page)
    page.goto(url)

    entered_text = fake.password()

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
