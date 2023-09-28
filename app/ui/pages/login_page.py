from app.ui.locators import LoginPageLocators
from app.ui.pages import BasePage, Header
from app.models.user import User


class LoginPage(Header, BasePage):
    url = "https://www.automationexercise.com/login"
    locators = LoginPageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.BUTTON_LOGIN)

    def authorize(self, email: str, password: str):
        input_login_email = self.find_element(self.locators.INPUT_LOGIN_EMAIL)
        input_login_email.clear()
        input_login_email.send_keys(email)

        input_login_pass = self.find_element(self.locators.INPUT_LOGIN_PASS)
        input_login_pass.clear()
        input_login_pass.send_keys(password)

        self.find_clickable_element(self.locators.BUTTON_LOGIN).click()

    def signup(self, user: User):
        input_name = self.find_clickable_element(self.locators.INPUT_SIGNUP_NAME)
        input_name.clear()
        input_name.send_keys(user.name)

        input_email = self.find_clickable_element(self.locators.INPUT_SIGNUP_EMAIL)
        input_email.clear()
        input_email.send_keys(user.email)

        self.find_clickable_element(self.locators.BUTTON_SIGNUP).click()
