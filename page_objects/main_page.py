from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MainPage(BasePage):
    NAV_BAR_USER_BUTTON = (By.CSS_SELECTOR, '[data-testid="nav-dp-l1-user-navigation-signup-icon"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SEACRH_ICON = (By.CSS_SELECTOR, '[data-testid="nav-dp-l1-user-navigation-search"]')
    SEACRH_INPUT = (By.CSS_SELECTOR, '[data-testid="main-search-input"]')
    SEARCH_RESULT = (By.CSS_SELECTOR, '[data-testid="product-card-title"]')
    PRODUCT_SIZE = (By.CSS_SELECTOR, '[data-testid="product-size-message"]')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '[data-testid="icon-whishlist-btn"]')
    NAV_BAR_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'data-testid="nav-dp-l1-user-navigation-wishlist"')
    RINGS_LINK = (By.XPATH, "//a[@name='Rings - snail trail link']")
    RINGS_IMAGE = (By.XPATH, "//picture[@name='Image']//img[@alt='Rings Image']")
    HONEY_MINI_SIGNET_IMAGE = (By.XPATH, "//img[contains(@alt,'Honey Mini Signet in Gold Vermeil on figure')]")
    

    def click_nav_bar_user_button(self):
        self.click(self.element(MainPage.NAV_BAR_USER_BUTTON))

    def find_email_input(self):
        return self.element(MainPage.EMAIL_INPUT)

    def find_password_input(self):
        return self.element(MainPage.PASSWORD_INPUT)

    def click_continue_button(self):
        self.click(self.element(MainPage.CONTINUE_BUTTON))

    def click_search_icon(self):
        self.click(self.element(MainPage.SEACRH_ICON))

    def find_search_input_field(self):
        return self.element(MainPage.SEACRH_INPUT)

    def find_search_result(self):
        return self.element(MainPage.SEARCH_RESULT)

    def find_product_size(self):
        return self.element(MainPage.PRODUCT_SIZE)

    def find_wishlist_button(self):
        return self.element(MainPage.WISHLIST_BUTTON)

    def click_on_rings_picture(self):
        self.click(self.element(MainPage.RINGS_IMAGE))

    def find_honey_image(self):
        return self.element(MainPage.HONEY_MINI_SIGNET_IMAGE)

    def click_on_honey_image(self):
        self.click(self.element(MainPage.HONEY_MINI_SIGNET_IMAGE))
    