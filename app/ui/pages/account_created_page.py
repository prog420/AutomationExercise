from app.ui.locators import AccountCreatedPageLocators
from app.ui.pages import BasePage, Header
from app.models.user import User


class AccountCreatedPage(Header, BasePage):
    url = "https://www.automationexercise.com/account_created"
    locators = AccountCreatedPageLocators()

    def is_account_created(self) -> bool:
        return self.is_element_present(self.locators.LABEL_ACCOUNT_CREATED)

    def click_button_continue(self):
        self.find_clickable_element(self.locators.BUTTON_CONTINUE).click()
