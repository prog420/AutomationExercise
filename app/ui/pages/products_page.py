from app.ui.locators import ProductsPageLocators
from app.ui.pages.base_page import BasePage
from app.ui.pages.header import Header


class ProductsPage(Header, BasePage):
    url = "https://www.automationexercise.com/products"
    locators = ProductsPageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.PRODUCT_CARD)

    def view_product(self, product_index: int = 1):
        view_product_buttons = self.find_elements(
            self.locators.BUTTON_VIEW_PRODUCT
        )
        view_product_buttons[product_index].click()

    def search_product(self, product_name: str):
        input_search = self.find_element(self.locators.INPUT_SEARCH_PRODUCT)
        input_search.clear()
        input_search.send_keys(product_name)
        self.find_element(self.locators.BUTTON_SEARCH_PRODUCT).click()
