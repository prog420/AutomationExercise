from app.ui.locators import ProductPageLocators
from app.ui.pages.base_page import BasePage
from app.ui.pages.header import Header


class ProductPage(Header, BasePage):
    url = "https://www.automationexercise.com/product_details/"
    locators = ProductPageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.PRODUCT_INFORMATION)

    def is_product_opened(self, product_name: str) -> bool:
        opened_product = self.find_element(self.locators.PRODUCT_NAME)
        return opened_product.text == product_name
