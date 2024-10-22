# Tests/test_deposit_withdraw_transactions.py

import pytest
from Pages.login_page import LoginPage
from Pages.customer_page import CustomerPage
from Utils.config import CUSTOMER_USERNAME
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestDepositWithdrawTransactions:
    def test_deposit_withdraw_transactions(self):
        login_page = LoginPage(self.driver)
        login_page.click_customer_login()
        login_page.select_customer(CUSTOMER_USERNAME)
        login_page.click_login()

        customer_page = CustomerPage(self.driver)

        # Deposit 31459
        customer_page.navigate_to_deposit()
        customer_page.enter_amount(31459)
        customer_page.submit()

        # Validate deposit
        success_text = customer_page.get_text((By.XPATH, "//span[@ng-show='message']"))
        assert "Deposit Successful" in success_text, "Deposit failed"

        # Take screenshot
        customer_page.take_screenshot("Test3_Deposit_Success")

        # Open Transactions
        customer_page.navigate_to_transactions()
        transactions = self.driver.find_elements(By.XPATH,
                                                 "//table[@class='table table-bordered table-striped']/tbody/tr")
        assert len(transactions) > 0, "No transactions found"
        customer_page.take_screenshot("Test3_Transactions_After_Deposit")

        # Withdraw 31459
        customer_page.navigate_to_withdrawl()
        customer_page.enter_amount(31459)
        customer_page.submit()

        # Validate withdraw
        success_text = customer_page.get_text((By.XPATH, "//span[@ng-show='message']"))
        assert "Transaction successful" in success_text, "Withdrawal failed"

        # Validate current balance
        current_balance = customer_page.get_balance()
        assert current_balance == 0, "Balance mismatch after withdrawal"

        # Take screenshot
        customer_page.take_screenshot("Test3_Withdraw_Success")

        # Open Transactions again
        customer_page.navigate_to_transactions()
        transactions = self.driver.find_elements(By.XPATH,
                                                 "//table[@class='table table-bordered table-striped']/tbody/tr")
        assert len(transactions) > 1, "No transactions found after withdrawal"
        customer_page.take_screenshot("Test3_Transactions_After_Withdrawal")

        # Logout
        customer_page.logout()
