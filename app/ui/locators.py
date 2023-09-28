from selenium.webdriver.common.by import By


class BasePageLocators:
    ...


class HeaderLocators(BasePageLocators):
    HEADER_BUTTON_HOME = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/"]',
    )
    HEADER_BUTTON_PRODUCTS = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/products"]',
    )
    HEADER_BUTTON_LOGIN = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/login"]',
    )
    HEADER_BUTTON_LOGOUT = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/logout"]',
    )
    HEADER_BUTTON_DELETE_ACCOUNT = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/delete_account"]',
    )
    HEADER_BUTTON_CONTACT_US = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/contact_us"]',
    )


class FooterLocators(BasePageLocators):
    FOOTER_ALERT_SUBSCRIBED_SUCCESS = (
        By.XPATH,
        '//div[contains(@class, "alert") and '
        'contains(@class, "alert-success")]'
    )
    FOOTER_INPUT_SUBSCRIBE = (
        By.XPATH,
        '//input[@id="susbscribe_email"]'
    )
    FOOTER_BUTTON_SUBSCRIBE = (
        By.XPATH,
        '//button[@id="subscribe"]'
    )


class HomePageLocators(HeaderLocators, BasePageLocators):
    SLIDER_CAROUSEL = (
        By.XPATH,
        '//div[@id="slider-carousel"]'
    )


class LoginPageLocators(HeaderLocators, BasePageLocators):
    INPUT_LOGIN_EMAIL = (By.XPATH, '//input[@data-qa="login-email"]')
    INPUT_LOGIN_PASS = (By.XPATH, '//input[@data-qa="login-password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@data-qa="login-button"]')

    INPUT_SIGNUP_NAME = (By.XPATH, '//input[@data-qa="signup-name"]')
    INPUT_SIGNUP_EMAIL = (By.XPATH, '//input[@data-qa="signup-email"]')
    BUTTON_SIGNUP = (By.XPATH, '//button[@data-qa="signup-button"]')


class SignupPageLocators(HeaderLocators, BasePageLocators):
    # Account Information
    RADIO_BTN_MR = (By.XPATH, '//input[@id="id_gender1"]')
    RADIO_BTN_MRS = (By.XPATH, '//input[@id="id_gender2"]')
    INPUT_NAME = (By.XPATH, '//input[@data-qa="name"]')
    INPUT_EMAIL = (By.XPATH, '//input[@data-qa="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@data-qa="password"]')
    SELECT_BIRTH_DAY = (By.XPATH, '//select[@data-qa="days"]')
    SELECT_BIRTH_MONTH = (By.XPATH, '//select[@data-qa="months"]')
    SELECT_BIRTH_YEAR = (By.XPATH, '//select[@data-qa="years"]')
    CHECKBOX_NEWSLETTER = (By.XPATH, '//input[@id="newsletter"]')
    CHECKBOX_SPECIAL_OFFERS = (By.XPATH, '//input[@id="optin"]')
    # Address Information
    INPUT_FIRST_NAME = (By.XPATH, '//input[@data-qa="first_name"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@data-qa="last_name"]')
    INPUT_COMPANY = (By.XPATH, '//input[@data-qa="company"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@data-qa="address"]')
    INPUT_ADDRESS_2 = (By.XPATH, '//input[@data-qa="address2"]')
    SELECT_COUNTRY = (By.XPATH, '//select[@data-qa="country"]')
    INPUT_STATE = (By.XPATH, '//input[@data-qa="state"]')
    INPUT_CITY = (By.XPATH, '//input[@data-qa="city"]')
    INPUT_ZIPCODE = (By.XPATH, '//input[@data-qa="zipcode"]')
    INPUT_MOBILE_NUMBER = (By.XPATH, '//input[@data-qa="mobile_number"]')
    # Confirmation
    BUTTON_CREATE_ACCOUNT = (By.XPATH, '//button[@data-qa="create-account"]')


class AccountCreatedPageLocators(HeaderLocators, BasePageLocators):
    LABEL_ACCOUNT_CREATED = (By.XPATH, '//h2[@data-qa="account-created"]')
    BUTTON_CONTINUE = (By.XPATH, '//a[@data-qa="continue-button"]')


class AccountDeletedPageLocators(HeaderLocators, BasePageLocators):
    LABEL_ACCOUNT_DELETED = (By.XPATH, '//h2[@data-qa="account-deleted"]')
    BUTTON_CONTINUE = (By.XPATH, '//a[@data-qa="continue-button"]')


class ContactUsPageLocators(HeaderLocators, BasePageLocators):
    CONTACT_FORM = (
        By.XPATH, '//div[@class="contact-form"]'
    )
    INPUT_FORM_NAME = (
        By.XPATH, '//input[@class="form-control" and @data-qa="name"]'
    )
    INPUT_FORM_EMAIL = (
        By.XPATH, '//input[@class="form-control" and @data-qa="email"]'
    )
    INPUT_FORM_SUBJECT = (
        By.XPATH, '//input[@class="form-control" and @data-qa="subject"]'
    )
    INPUT_FORM_MESSAGE = (
        By.XPATH, '//textarea[@class="form-control" and @data-qa="message"]'
    )
    INPUT_FORM_FILE = (
        By.XPATH, '//input[@class="form-control" and @type="file"]'
    )
    BUTTON_FORM_SUBMIT = (
        By.XPATH, '//input[@data-qa="submit-button"]'
    )
    LABEL_SUCCESS = (
        By.XPATH, '//div[contains(@class, "status") '
                  'and contains(@class, "alert-success")]'
    )
    BUTTON_RETURN_HOME = (
        By.XPATH, '//div[@id="form-section"]'
                  '/a[contains(@class, "btn-success")]'
    )


class ProductsPageLocators(HeaderLocators, BasePageLocators):
    LABEL_PAGE_TITLE = (
        By.XPATH,
        '//h2[contains(@class, "title") and contains(@class, "text-center")]'
    )
    PRODUCT_CARD = (
        By.XPATH,
        '//div[@class="product-image-wrapper"]'
    )
    BUTTON_VIEW_PRODUCT = (
        By.XPATH,
        '//div[@class="product-image-wrapper"]'
        '//a[contains(@href, "product_details")]'
    )
    BUTTON_ADD_TO_CART = (
        By.XPATH,
        '//div[@class="product-image-wrapper"]'
        '//div[contains(@class, "productinfo")]'
        '//a[contains(@class, "add-to-cart")]'
    )
    INPUT_SEARCH_PRODUCT = (
        By.XPATH,
        '//input[@id="search_product"]'
    )
    BUTTON_SEARCH_PRODUCT = (
        By.XPATH,
        '//button[@id="submit_search"]'
    )


class ProductPageLocators(HeaderLocators, BasePageLocators):
    PRODUCT_INFORMATION = (
        By.XPATH,
        '//div[@class="product-information"]'
    )
    PRODUCT_NAME = (
        By.XPATH,
        '//div[@class="product-information"]//h2'
    )
    INPUT_PRODUCT_QUANTITY = (
        By.XPATH,
        '//input[@id="quantity"]'
    )
    BUTTON_ADD_TO_CART = (
        By.XPATH,
        '//button[contains(@class, "cart")]'
    )
    BUTTON_MODAL_VIEW_CART = (
        By.XPATH,
        '//div[@id="cartModal"]//a[@href="/view_cart"]'
    )
    BUTTON_MODAL_CONTINUE_SHOPPING = (
        By.XPATH,
        '//div[@id="cartModal"]//button[contains(@class, "btn-success")]'
    )
