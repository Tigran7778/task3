from playwright.sync_api import sync_playwright
from pages.alerts_page import AlertsPage


def test_alerts(page):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    alerts_page = AlertsPage(page)

    page.goto(url)

    # Обработчик alert
    def handle_dialog_alert(dialog):
        print(f"Диалог: {dialog.message}")
        dialog.accept()

    # Обработчик confirm
    def handle_dialog_confirm(d):
        print(f"Диалог: {d.message}")
        d.accept()

    # Обработчик prompt с вводом случайного текста
    def handle_dialog_prompt(d):
        print(f"Prompt сообщение: {d.message}")
        nonlocal entered_text
        entered_text = alerts_page.generate_random_text()
        print(f"Вводим случайный текст: {entered_text}")
        d.accept(entered_text)

    # 1. JS Alert
    page.once("dialog", handle_dialog_alert)
    alerts_page.click_js_alert()
    print("Обработан JS Alert")

    # 2. JS Confirm — ОТМЕНА
    page.once("dialog", handle_dialog_confirm)
    alerts_page.click_js_confirm()
    print("Обработан JS Confirm (отмена)")

    # 3. JS Confirm — ПОДТВЕРЖДЕНИЕ
    page.once("dialog", handle_dialog_confirm)
    alerts_page.click_js_confirm()
    print("Обработан JS Confirm (принят)")

    # 4. JS Prompt с вводом случайного текста
    entered_text = ""
    page.once("dialog", handle_dialog_prompt)
    alerts_page.click_js_prompt()
    print("Обработан JS Prompt с вводом текста")

    # Проверяем результат
    result_text = alerts_page.get_result_text()
    print(f"Результат: {result_text}")

    # Проверка, что в результате отображается введенный текст
    expected_text = f"You entered: {entered_text}"
    assert expected_text in result_text, f"Текст не совпадает! Ожидали: '{expected_text}', получили: '{result_text}'"
