import allure
import pytest
from tests.tests_ui.base_case import BaseCase
from utils.user_importer import import_user


@allure.suite("Smoke")
@allure.feature("Contact Us Form")
class TestContactUs(BaseCase):
    @allure.title("AE-6: User can send message via Contact Us Form")
    @allure.link("https://app.qase.io/case/AE-6")
    def test_ae_6_send_message_via_contact_us_form_valid_data(self):
        # Arrange
        ...
        # Act
        self.home_page.open()
        self.home_page.click_header_button_contact_us()
        self.contact_us_page.fill_contact_form(
            name="John",
            email="john_test@mail.test",
            message="test message",
            file_path=None
        )
        self.contact_us_page.click_submit_button()
        self.contact_us_page.accept_alert()
        self.contact_us_page.click_return_home_button()
        # Assert
        assert self.home_page.is_opened()
