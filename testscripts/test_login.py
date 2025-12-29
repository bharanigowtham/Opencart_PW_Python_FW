import pytest
from playwright.sync_api import Page, expect
from config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_invalid_user_login(page):
    home_page=HomePage(page)
    login_page=LoginPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.enter_email(Config.invalid_email)
    login_page.enter_password(Config.invalid_password)
    login_page.click_login_btn()

    expect(login_page.get_login_error()).to_be_visible(timeout=3000)

