from playwright.sync_api import Page, expect
import pytest

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.random_data_util import RandomDataUtil

@pytest.mark.sanity
def test_user_registration(page):
    home_page = HomePage(page)
    registration_page=RegistrationPage(page)
    random_data = RandomDataUtil()

    home_page.click_my_account()
    home_page.click_register()

    first_name = random_data.get_first_name()
    last_name = random_data.get_last_name()
    email=random_data.get_email()
    phone_number = random_data.get_phone_number()
    password = random_data.get_password()

    registration_page.enter_first_name(first_name)
    registration_page.enter_last_name(last_name)
    registration_page.enter_email(email)
    registration_page.enter_telephone(phone_number)
    registration_page.enter_password(password)
    registration_page.enter_confirm_password(password)
    page.wait_for_timeout(2000)

    registration_page.select_privacy_policy()
    registration_page.click_continue()
    page.wait_for_timeout(3000)

    conf_msg = registration_page.get_confirmation_msg()
    expect(conf_msg).to_have_text("Your Account Has Been Created!")

