# Pages/login_page.py

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class LoginPage(BasePage):
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Customer Login')]")
    CUSTOMER_NAME_DROPDOWN = (By.ID, "userSelect")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")

    def click_customer_login(self):
        self.click(self.CUSTOMER_LOGIN_BUTTON)

    def select_customer(self, customer_name):
        self.send_keys(self.CUSTOMER_NAME_DROPDOWN, customer_name)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
