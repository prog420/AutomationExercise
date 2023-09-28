from app.ui.locators import FooterLocators
from app.ui.pages.base_page import BasePage


class Footer(BasePage):
    locators = FooterLocators()

    def subscribe(self, email: str):
        input_subscribe = self.find_clickable_element(
            self.locators.FOOTER_INPUT_SUBSCRIBE
        )
        input_subscribe.clear()
        input_subscribe.send_keys(email)
        self.find_clickable_element(
            self.locators.FOOTER_BUTTON_SUBSCRIBE
        ).click()

    def is_subscribed(self):
        return self.is_element_present(
            self.locators.FOOTER_ALERT_SUBSCRIBED_SUCCESS
        )
