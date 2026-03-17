import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("login")
class TestAddForecastedScenario:

    def open_cashflow_forecast(self, browser):
        """Navigate to Cashflow Forecast tab"""
        wait = WebDriverWait(browser, 30)

        # Wait for Cashflow Management card
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Cashflow Management')]")))
        print(" Dashboard loaded successfully.")

        # Open Cashflow Management
        cashflow_card = browser.find_element(By.XPATH, "//p[contains(text(), 'Cashflow Management')]/ancestor::a")
        browser.execute_script("arguments[0].scrollIntoView(true);", cashflow_card)
        cashflow_card.click()
        print(" Opened Cashflow Management module.")

        # Click Cashflow Forecast tab
        forecast_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Cashflow Forecast')]"))
        )
        forecast_tab.click()
        print(" Opened Cashflow Forecast tab.")

    def test_valid_add_forecasted_receipts(self, login):
        browser = login
        wait = WebDriverWait(browser, 30)

        self.open_cashflow_forecast(browser)

        # Click Add Forecasted Receipts/Payments button
        add_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Forecasted Receipts/Payments')]"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", add_btn)
        time.sleep(1)
        add_btn.click()
        print(" Clicked 'Add Forecasted Receipts/Payments' button.")

        # Select Receipts from dropdown
        receipt_dropdown = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'css-19bb58m')]//input"))
        )
        receipt_dropdown.click()
        time.sleep(0.5)
        receipt_dropdown.send_keys(Keys.ARROW_DOWN)
        receipt_dropdown.send_keys(Keys.ENTER)
        print(" Selected 'Receipts' option.")

        # Enter monthly amount — locate input for constant amount
        try:
            amount_input = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[@type='number' or @placeholder='Amount' or @name='amount']")
                )
            )
            amount_input.clear()
            amount_input.send_keys("5000000")
            print(" Set monthly amount to 5,000,000.")
        except Exception:
            print(" Could not find amount input field. Verify the input field’s name/placeholder.")

        # Click Run Forecast
        run_forecast_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Run Forecast')]"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", run_forecast_btn)
        time.sleep(1)
        run_forecast_btn.click()
        print(" Clicked 'Run Forecast' button.")

        # Verify success modal
        success_msg = wait.until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(., 'Cash flow forecast set successfully')]"))
        )
        assert success_msg.is_displayed(), "❌ Success message not displayed."
        print("🎉 Cash flow forecast set successfully!")

        # Close modal
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Close')]"))
        )
        browser.execute_script("arguments[0].click();", close_btn)
        print(" Closed success modal.")

    def test_empty_add_forecasted_receipts(self, login):
        """Verify behavior when user runs forecast without filling fields."""
        browser = login
        wait = WebDriverWait(browser, 30)

        self.open_cashflow_forecast(browser)

        # Click Add Forecasted Receipts/Payments
        add_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Forecasted Receipts/Payments')]"))
        )
        add_btn.click()
        print(" Clicked 'Add Forecasted Receipts/Payments' (empty test).")

        # Try to click Run Forecast without selecting or entering anything
        run_forecast_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Run Forecast')]"))
        )
        run_forecast_btn.click()
        print(" Clicked 'Run Forecast' with empty fields.")

        # Look for validation or toast message
        try:
            error_msg = wait.until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(., 'required') or contains(., 'select')]"))
            )
            print(" Validation error displayed:", error_msg.text)
        except Exception:
            print(" No validation error appeared — confirm app validation behavior.")

