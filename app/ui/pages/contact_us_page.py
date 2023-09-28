from app.ui.locators import ContactUsPageLocators
from app.ui.pages.base_page import BasePage
from app.ui.pages.header import Header


class ContactUsPage(Header, BasePage):
    url = "https://www.automationexercise.com/contact_us"
    locators = ContactUsPageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.CONTACT_FORM)

    def is_message_sent(self) -> bool:
        return self.is_element_present(self.locators.LABEL_SUCCESS)

    def fill_contact_form(self, name: str = None, email: str = None,
                          message: str = None, file_path: str = None):
        self.fill_form_name(name)
        self.fill_form_email(email)
        self.fill_form_message(message)
        self.fill_form_file(file_path)

    def fill_form_name(self, name: str = None):
        if name is None:
            return
        input_name = self.find_clickable_element(
            self.locators.INPUT_FORM_NAME
        )
        input_name.clear()
        input_name.send_keys(name)

    def fill_form_email(self, email: str = None):
        if email is None:
            return
        input_email = self.find_clickable_element(
            self.locators.INPUT_FORM_EMAIL
        )
        input_email.clear()
        input_email.send_keys(email)

    def fill_form_message(self, message: str = None):
        if message is None:
            return
        input_message = self.find_clickable_element(
            self.locators.INPUT_FORM_MESSAGE
        )
        input_message.clear()
        input_message.send_keys(message)

    def fill_form_file(self, file_path: str = None):
        if file_path is None:
            return
        input_file = self.find_clickable_element(
            self.locators.INPUT_FORM_FILE
        )
        input_file.clear()
        input_file.send_keys(file_path)

    def click_submit_button(self):
        self.find_clickable_element(self.locators.BUTTON_FORM_SUBMIT).click()

    def accept_alert(self):
        if self.is_alert_present():
            self.driver.switch_to.alert.accept()

    def click_return_home_button(self):
        self.find_clickable_element(self.locators.BUTTON_RETURN_HOME).click()
