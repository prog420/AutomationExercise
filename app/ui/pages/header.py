from app.ui.locators import HeaderLocators
from app.ui.pages.base_page import BasePage


class Header(BasePage):
    locators = HeaderLocators()

    def is_authorized(self):
        return self.is_element_present(
            self.locators.HEADER_BUTTON_DELETE_ACCOUNT
        )

    def is_not_authorized(self):
        return self.is_not_element_present(
            self.locators.HEADER_BUTTON_DELETE_ACCOUNT
        )

    def click_header_button_login(self):
        self.find_clickable_element(
            self.locators.HEADER_BUTTON_LOGIN
        ).click()

    def click_header_button_products(self):
        self.find_clickable_element(
            self.locators.HEADER_BUTTON_PRODUCTS
        ).click()

    def click_header_button_home(self):
        self.find_clickable_element(
            self.locators.HEADER_BUTTON_HOME
        ).click()

    def click_header_button_delete_account(self):
        self.find_element(self.locators.HEADER_BUTTON_HOME)
        self.find_clickable_element(
            self.locators.HEADER_BUTTON_DELETE_ACCOUNT
        ).click()

    def click_header_button_logout(self):
        self.find_clickable_element(
            self.locators.HEADER_BUTTON_LOGOUT
        ).click()

    def click_header_button_contact_us(self):
        self.find_clickable_element(
            self.locators.HEADER_BUTTON_CONTACT_US
        ).click()
