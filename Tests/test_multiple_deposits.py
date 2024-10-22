# Tests/test_multiple_deposits.py

import pytest
from Pages.login_page import LoginPage
from Pages.customer_page import CustomerPage
from Utils.config import CUSTOMER_USERNAME
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestMultipleDeposits:
    def test_multiple_deposits(self):
        login_page = LoginPage(self.driver)
        login_page.click_customer_login()
        login_page.select_customer(CUSTOMER_USERNAME)
        login_page.click_login()

        customer_page = CustomerPage(self.driver)

        # Assuming multiple accounts are accessible via a dropdown or similar
        # For demonstration, let's assume there are 2 accounts
        accounts = ["Account1", "Account2"]  # Replace with actual account identifiers

        for account in accounts:
            # Logic to select account
            # This will depend on the actual application UI
            # Example:
            # self.driver.find_element(By.XPATH, f"//option[text()='{account}']").click()
            # For simplicity, assuming first account is selected
            customer_page.navigate_to_deposit()
            customer_page.enter_amount(1500)
            customer_page.submit()

            # Validate deposit
            success_text = customer_page.get_text((By.XPATH, "//span[@ng-show='message']"))
            assert "Deposit Successful" in success_text, f"Deposit failed for {account}"

            # Take screenshot
            customer_page.take_screenshot(f"Test2_Deposit_{account}_Success")

        # Logout
        customer_page.logout()
