import allure
from tests.tests_ui.base_case import BaseCase


@allure.suite("Smoke")
@allure.epic("Product Cards")
class TestProducts(BaseCase):
    @allure.title("AE-7: Verify All Products and product detail page")
    @allure.link("https://app.qase.io/case/AE-7")
    def test_ae_7_verify_products_and_details_page(self):
        # Arrange
        ...
        # Act
        self.home_page.open()
        self.home_page.click_header_button_products()
        self.products_page.view_product(product_index=0)
        # Assert
        assert self.product_page.is_opened()

    @allure.title("AE-8: Search Product")
    @allure.link("https://app.qase.io/case/AE-8")
    def test_ae_8_search_product(self):
        # Arrange
        product_name = "Winter Top"
        # Act
        self.home_page.open()
        self.home_page.click_header_button_products()
        self.products_page.search_product(product_name=product_name)
        self.products_page.view_product(product_index=0)
        # Assert
        assert self.product_page.is_product_opened(product_name=product_name)
