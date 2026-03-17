import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("login")
class TestCashflowSettings:

    def open_cashflow_settings(self, browser):
        wait = WebDriverWait(browser, 30)

        # Wait for Dashboard
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Cashflow Management')]")))
        print(" Dashboard loaded successfully.")

        # Click Cashflow Management module
        cashflow_card = browser.find_element(By.XPATH, "//p[contains(text(), 'Cashflow Management')]/ancestor::a")
        browser.execute_script("arguments[0].scrollIntoView(true);", cashflow_card)
        cashflow_card.click()
        print(" Clicked Cashflow Management module.")

        # Click Cashflow Analysis tab
        cashflow_analysis_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Cashflow Analysis')]"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", cashflow_analysis_tab)
        cashflow_analysis_tab.click()
        print(" Opened Cashflow Analysis tab.")

        # Click Set Cashflow Settings
        set_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Set Cashflow Settings')]"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", set_btn)
        set_btn.click()
        print(" Opened Set Cashflow Settings form.")

    def test_valid_cashflow_settings(self, login):
        browser = login
        wait = WebDriverWait(browser, 30)
        self.open_cashflow_settings(browser)

        # Wait for input field
        opening_balance = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='startingBalance']"))
        )
        opening_balance.clear()
        opening_balance.send_keys("100000")
        print(" Entered Opening Balance.")

        # Select dropdown 1 (first react-select input)
        dropdowns = browser.find_elements(By.XPATH, "//div[contains(@class, 'react-select__input-container')]//input")
        if dropdowns:
            first_dropdown = dropdowns[0]
            first_dropdown.click()
            first_dropdown.send_keys(Keys.ARROW_DOWN)
            first_dropdown.send_keys(Keys.ENTER)
            print("Selected first dropdown value.")

        # Select dropdown 2 (if available)
        if len(dropdowns) > 1:
            second_dropdown = dropdowns[1]
            second_dropdown.click()
            second_dropdown.send_keys(Keys.ARROW_DOWN)
            second_dropdown.send_keys(Keys.ENTER)
            print("Selected second dropdown value.")

        # Click Submit button
        submit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'submit') or contains(., 'Submit')]"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(1)
        submit_btn.click()
        print(" Clicked Submit button.")

                # Verify success modal
        success_modal = wait.until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(., 'Cash flow settings set successfully')]"))
        )
        assert success_modal.is_displayed(), " Success message not visible."
        print("🎉 Cash flow settings set successfully.")

        #  Close success modal (safe click)
        try:
            close_btn = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Close')]"))
            )
            browser.execute_script("arguments[0].scrollIntoView(true);", close_btn)
            time.sleep(1)
            browser.execute_script("arguments[0].click();", close_btn)
            print(" Closed success modal safely.")
        except Exception as e:
            print(f" Could not close modal automatically: {e}")







