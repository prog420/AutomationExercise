import allure
import pytest
from tests.tests_ui.base_case import BaseCase
from utils.user_importer import import_user


@allure.suite("Smoke")
@allure.epic("Authorization")
@allure.feature("Authorization with email and password")
class TestAuth(BaseCase):
    @allure.title("AE-2: User can authorize with valid email and password")
    @allure.link("https://app.qase.io/case/AE-2")
    @pytest.mark.parametrize(
        "user", import_user(file_name="tests/tests_data/AE-2.xlsx")
    )
    def test_ae_2_user_can_authorize(self, user_manager, user):
        # Arrange
        user_manager.create_user(user)
        # Act
        self.home_page.open()
        self.home_page.click_header_button_login()
        self.login_page.authorize(email=user.email, password=user.password)
        # Assert
        assert self.login_page.is_authorized()

    @allure.title("AE-3: User can't authorize with incorrect password.")
    @allure.link("https://app.qase.io/case/AE-3")
    @pytest.mark.parametrize(
        "user", import_user(file_name="tests/tests_data/AE-3.xlsx")
    )
    def test_ae_3_user_cant_authorize_with_incorrect_pass(
            self, user_manager, user
    ):
        # Arrange
        user_manager.create_user(user)
        # Act
        self.home_page.open()
        self.home_page.click_header_button_login()
        self.login_page.authorize(
            email=user.email, password=user.password + "incorrect"
        )
        # Assert
        assert self.login_page.is_not_authorized()

    @allure.title("AE-4: Logout User")
    @allure.link("https://app.qase.io/case/AE-4")
    @pytest.mark.parametrize(
        "user", import_user(file_name="tests/tests_data/AE-4.xlsx")
    )
    def test_ae_4_user_can_log_out(self, user_manager, user):
        # Arrange
        user_manager.create_user(user)
        # Act
        self.home_page.open()
        self.home_page.click_header_button_login()
        self.login_page.authorize(email=user.email, password=user.password)
        self.home_page.click_header_button_logout()
        # Assert
        assert self.login_page.is_not_authorized()
