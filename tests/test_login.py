from pages.login_page import LoginPage
from page_factory.page_factory import PageFactory


def test_login_correct(browser):
    factory = PageFactory.from_json(
        browser,
        "page_factory/page_factory.json",
        http_credentials={"username": "admin", "password": "admin"}
    )
    page = factory.create_page()
    page.goto(f"{factory.config['base_url']}/basic_auth")

    login_page = LoginPage(page)
    message = login_page.get_message_text()

    expected_text = "Congratulations! You must have the proper credentials."
    assert message == expected_text, \
        f"Текст не совпадает! Ожидалось: '{expected_text}', получено: '{message}'"
