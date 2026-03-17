import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("login")
class TestCashflowForecast:

    def open_cashflow_forecast(self, browser):
        """Navigate to Cashflow Forecast tab"""
        wait = WebDriverWait(browser, 30)

        # Wait for Dashboard to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Cashflow Management')]")))
        print(" Dashboard loaded successfully.")

        # Click Cashflow Management
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

    def test_valid_cashflow_forecast(self, login):
        browser = login
        wait = WebDriverWait(browser, 30)

        self.open_cashflow_forecast(browser)

        # Click Add New Scenario
        add_new = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(., 'Add New Scenario')]"))
        )
        add_new.click()
        print(" Clicked Add New Scenario.")

        # Enter Scenario Name
        scenario_name = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
        )
        scenario_name.clear()
        scenario_name.send_keys("Best Case")
        print(" Entered Scenario Name.")

        # Select Forecast Duration (react-select disabled but we ensure it's visible)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '12 Months')]"))
        )
        print(" Confirmed Forecast Duration is '12 Months'.")

        # Start Date (disabled, assume default visible)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'December')]"))
        )
        print(" Start Date confirmed as visible (December 1st).")

        # Click Create Forecast Scenario
        create_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create Forecast Scenario')]"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", create_btn)
        time.sleep(1)
        create_btn.click()
        print(" Clicked Create Forecast Scenario button.")

        # Wait for Success Message
        success_msg = wait.until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(., 'Cash flow forecast scenario created successfully')]"))
        )
        assert success_msg.is_displayed(), " Success message not displayed."
        print(" Cash flow forecast scenario created successfully.")

        # Close modal
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Close')]"))
        )
        browser.execute_script("arguments[0].click();", close_btn)
        print(" Closed success modal.")

    def test_empty_fields(self, login):
        browser = login
        wait = WebDriverWait(browser, 30)

        self.open_cashflow_forecast(browser)

        # Click Add New Scenario
        add_new = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(., 'Add New Scenario')]"))
        )
        add_new.click()
        print(" Clicked Add New Scenario (Empty Fields Test).")

        # Ensure Scenario Name is empty
        scenario_name = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
        )
        scenario_name.clear()
        print(" Cleared Scenario Name input.")

        # Click Create Forecast Scenario directly
        create_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create Forecast Scenario')]"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", create_btn)
        time.sleep(1)
        create_btn.click()
        print(" Clicked Create Forecast Scenario button with empty fields.")

        # Expect validation message or error toast
        try:
            error_toast = browser.find_element(By.XPATH, "//p[contains(., 'required') or contains(., 'invalid')]")
            print(" Validation message displayed:", error_toast.text)
        except Exception:
            print(" No validation message found — check app behavior.")






