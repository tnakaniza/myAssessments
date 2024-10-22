# Tests/test_deposit_logout.py

import pytest
from Pages.login_page import LoginPage
from Pages.customer_page import CustomerPage
from Utils.config import CUSTOMER_USERNAME
import os

@pytest.mark.usefixtures("setup")
class TestDepositLogout:
    def test_deposit_logout(self):
        login_page = LoginPage(self.driver)
        login_page.click_customer_login()
        login_page.select_customer(CUSTOMER_USERNAME)
        login_page.click_login()

        customer_page = CustomerPage(self.driver)
        customer_page.navigate_to_deposit()
        customer_page.enter_amount(1500)
        customer_page.submit()

        # Validate deposit
        success_text = customer_page.get_text((By.XPATH, "//span[@ng-show='message']"))
        assert "Deposit Successful" in success_text, "Deposit failed"

        # Take screenshot
        customer_page.take_screenshot("Test1_Deposit_Success")

        # Logout
        customer_page.logout()
