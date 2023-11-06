from app.ui.locators import HomePageLocators
from app.ui.pages import Header, BasePage


class HomePage(Header, BasePage):
    url = "https://www.automationexercise.com/"
    locators = HomePageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.SLIDER_CAROUSEL)
