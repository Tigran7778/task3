import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from logger import setup_logger
from page_factory.page_factory import PageFactory


def test_login_correct(browser):
    factory = PageFactory.from_json(
        browser,
        "page_factory/page_factory.json",
        http_credentials={"username": "admin", "password": "admin"}
    )
    page = factory.create_page()
    response = page.goto(f"{factory.config['base_url']}/basic_auth")

    assert LoginPage(page).get_message(response.status) == "Success"
    assert "Congratulations! You must have the proper credentials." in page.content()
    print("ТЕСТ ПРОЙДЕН")
