# Pages/customer_page.py

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class CustomerPage(BasePage):
    DEPOSIT_TAB = (By.XPATH, "//button[contains(text(),'Deposit')]")
    WITHDRAW_TAB = (By.XPATH, "//button[contains(text(),'Withdrawl')]")
    TRANSITIONS_TAB = (By.XPATH, "//button[contains(text(),'Transactions')]")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='amount']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Logout')]")
    BALANCE_FIELD = (By.XPATH, "//strong[contains(text(),'Balance')]/following-sibling::strong")

    def navigate_to_deposit(self):
        self.click(self.DEPOSIT_TAB)

    def navigate_to_withdrawl(self):
        self.click(self.WITHDRAW_TAB)

    def navigate_to_transactions(self):
        self.click(self.TRANSITIONS_TAB)

    def enter_amount(self, amount):
        self.send_keys(self.AMOUNT_INPUT, str(amount))

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_balance(self):
        balance_text = self.get_text(self.BALANCE_FIELD)
        return float(balance_text)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
