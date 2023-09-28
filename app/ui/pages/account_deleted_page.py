from app.ui.locators import AccountDeletedPageLocators
from app.ui.pages import BasePage, Header
from app.models.user import User


class AccountDeletedPage(Header, BasePage):
    url = "https://www.automationexercise.com/delete_account"
    locators = AccountDeletedPageLocators()

    def is_account_deleted(self) -> bool:
        return self.is_element_present(self.locators.LABEL_ACCOUNT_DELETED)

    def click_button_continue(self):
        self.find_clickable_element(self.locators.BUTTON_CONTINUE).click()
