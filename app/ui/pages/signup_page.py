from selenium.webdriver.support.ui import Select

from app.ui.locators import SignupPageLocators
from app.ui.pages import BasePage, Header
from app.models.user import User


class SignupPage(Header, BasePage):
    url = "https://www.automationexercise.com/signup"
    locators = SignupPageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.BUTTON_CREATE_ACCOUNT)

    def create_account(self, user: User):
        self.select_mr_mrs(user.title)
        self.fill_input_name(user.name)
        self.fill_input_password(user.password)
        self.select_date_of_birth(
            year=user.years, month=user.months, day=user.days
        )
        self.click_checkbox_newsletter()
        self.click_checkbox_offer()
        self.fill_input_first_name(user.first_name)
        self.fill_input_last_name(user.last_name)
        self.fill_input_company(user.company)
        self.fill_input_address(user.address)
        self.select_country()
        self.fill_input_state(user.state)
        self.fill_input_city(user.city)
        self.fill_input_zipcode(user.zipcode)
        self.fill_input_phone(user.mobile_number)

        self.find_clickable_element(self.locators.BUTTON_CREATE_ACCOUNT).click()

    def select_mr_mrs(self, title="mr"):
        if title.lower() == "mr":
            self.find_clickable_element(self.locators.RADIO_BTN_MR).click()
        elif title.lower() == "mrs":
            self.find_clickable_element(self.locators.RADIO_BTN_MRS).click()

    def fill_input_name(self, name: str):
        name_input = self.find_clickable_element(self.locators.INPUT_NAME)
        name_input.clear()
        name_input.send_keys(name)

    def fill_input_password(self, password: str):
        input_pass = self.find_clickable_element(self.locators.INPUT_PASSWORD)
        input_pass.clear()
        input_pass.send_keys(password)

    def select_date_of_birth(self, year: str, month: str, day: str):
        select_year = Select(
            self.find_clickable_element(self.locators.SELECT_BIRTH_YEAR)
        )
        select_year.select_by_value(str(year))

        select_month = Select(
            self.find_clickable_element(self.locators.SELECT_BIRTH_MONTH)
        )
        select_month.select_by_value(str(month))

        select_day = Select(self.find_clickable_element(self.locators.SELECT_BIRTH_DAY))
        select_day.select_by_value(str(day))

    def click_checkbox_newsletter(self):
        self.find_clickable_element(self.locators.CHECKBOX_NEWSLETTER).click()

    def click_checkbox_offer(self):
        self.find_clickable_element(self.locators.CHECKBOX_SPECIAL_OFFERS).click()

    def fill_input_first_name(self, first_name: str):
        input_first_name = self.find_clickable_element(self.locators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys(first_name)

    def fill_input_last_name(self, last_name: str):
        input_last_name = self.find_clickable_element(self.locators.INPUT_LAST_NAME)
        input_last_name.clear()
        input_last_name.send_keys(last_name)

    def fill_input_company(self, company: str):
        input_company = self.find_clickable_element(self.locators.INPUT_COMPANY)
        input_company.clear()
        input_company.send_keys(company)

    def fill_input_address(self, address: str):
        input_address = self.find_clickable_element(self.locators.INPUT_ADDRESS)
        input_address.clear()
        input_address.send_keys(address)

    def select_country(self):
        select_country = Select(
            self.find_clickable_element(self.locators.SELECT_COUNTRY)
        )
        select_country.select_by_index(1)

    def fill_input_state(self, state: str):
        input_state = self.find_clickable_element(self.locators.INPUT_STATE)
        input_state.clear()
        input_state.send_keys(state)

    def fill_input_city(self, city: str):
        input_city = self.find_clickable_element(self.locators.INPUT_CITY)
        input_city.clear()
        input_city.send_keys(city)

    def fill_input_zipcode(self, zipcode: str):
        input_zipcode = self.find_clickable_element(self.locators.INPUT_ZIPCODE)
        input_zipcode.clear()
        input_zipcode.send_keys(zipcode)

    def fill_input_phone(self, phone: str):
        input_phone = self.find_clickable_element(self.locators.INPUT_MOBILE_NUMBER)
        input_phone.clear()
        input_phone.send_keys(phone)
