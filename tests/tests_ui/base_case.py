import pytest
from app.ui.pages import (
    HomePage,
    LoginPage,
    SignupPage,
    AccountCreatedPage,
    AccountDeletedPage,
    ContactUsPage,
    ProductsPage,
    ProductPage,
)


class BaseCase:
    driver = None

    home_page = None
    login_page = None
    signup_page = None
    account_created_page = None
    account_deleted_page = None
    contact_us_page = None
    products_page = None
    product_page = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver

        self.home_page = HomePage(driver=self.driver)
        self.login_page = LoginPage(driver=self.driver)
        self.signup_page = SignupPage(driver=self.driver)
        self.account_created_page = AccountCreatedPage(driver=self.driver)
        self.account_deleted_page = AccountDeletedPage(driver=self.driver)
        self.contact_us_page = ContactUsPage(driver=self.driver)
        self.products_page = ProductsPage(driver=self.driver)
        self.product_page = ProductPage(driver=self.driver)
