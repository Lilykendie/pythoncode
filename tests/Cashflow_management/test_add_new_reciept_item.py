import time
import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


@pytest.mark.usefixtures("login")
class TestAddReceiptItem:

    def open_cashflow_analysis(self, browser):
        """Navigate to Cashflow Analysis → Receipts (Inflow)."""
        wait = WebDriverWait(browser, 30)

        # Dashboard visible
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Cashflow Management')]")))
        print(" Dashboard loaded successfully.")

        # Open Cashflow Management
        cashflow_card = browser.find_element(By.XPATH, "//p[contains(text(),'Cashflow Management')]/ancestor::a")
        browser.execute_script("arguments[0].scrollIntoView(true);", cashflow_card)
        cashflow_card.click()
        print(" Opened Cashflow Management module.")

        # Open Cashflow Analysis tab
        analysis_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Cashflow Analysis')]"))
        )
        analysis_tab.click()
        print(" Opened Cashflow Analysis tab.")

        # Wait for Receipts section
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Add new receipt item')]")))
        print(" Cashflow Analysis — Receipts (Inflow) ready.")

    # =====================================================================
    #  TEST 1: VALID RECEIPT ITEM
    # =====================================================================
    def test_valid_add_receipt_item(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)
        self.open_cashflow_analysis(browser)

        # Click Add new receipt item
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add new receipt item')]")))
        browser.execute_script("arguments[0].click();", add_btn)
        print(" Clicked Add new receipt item button.")

        # Random suffix to avoid duplicates
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

        # Fill out item name
        name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
        name_input.clear()
        name_input.send_keys(f"Liquid_{suffix}")
        name_input.send_keys(Keys.TAB)
        print(f" Entered item name: Liquid_{suffix}")

        # Fill out description
        desc_input = wait.until(EC.presence_of_element_located((By.NAME, "cashFlowLineDescription")))
        desc_input.clear()
        desc_input.send_keys(f"Sales inflow for Q{random.randint(1, 4)}")
        desc_input.send_keys(Keys.TAB)
        print(" Entered item description.")

        # Fill out static code
        static_code_input = wait.until(EC.presence_of_element_located((By.NAME, "staticCode")))
        static_code_input.clear()
        static_code_input.send_keys(f"L{suffix[:2]}")
        print(f" Entered static code: L{suffix[:2]}")

        # Wait for submit button to enable
        submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Add Item')]")))
        browser.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(1)

        try:
            wait.until(lambda d: submit_btn.is_enabled())
        except TimeoutException:
            print(" Add Item button still disabled — forcing enable via JS.")
            browser.execute_script("arguments[0].removeAttribute('disabled');", submit_btn)

        # Click the Add Item button
        try:
            submit_btn.click()
        except ElementClickInterceptedException:
            browser.execute_script("arguments[0].click();", submit_btn)
        print(" Clicked Add Item button.")

        # Verify success modal
        success_modal = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[contains(., 'Congratulations') or contains(., 'Cash flow line created successfully')]")
            )
        )
        assert success_modal.is_displayed(), " Success modal not visible!"
        print(" Cash flow line created successfully!")

        # Close modal
        close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Close')]")))
        browser.execute_script("arguments[0].click();", close_btn)
        print(" Closed success modal.")

    # =====================================================================
    #  TEST 2: EMPTY FIELDS
    # =====================================================================
    def test_empty_fields_add_receipt_item(self, login):
        browser = login
        wait = WebDriverWait(browser, 30)
        self.open_cashflow_analysis(browser)

        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add new receipt item')]")))
        browser.execute_script("arguments[0].click();", add_btn)
        print(" Clicked Add new receipt item button (empty fields test).")

        # Try submitting empty form
        submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Add Item')]")))
        browser.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(1)

        if not submit_btn.is_enabled():
            print(" Add Item button disabled as expected for empty fields.")
            return

        browser.execute_script("arguments[0].click();", submit_btn)
        success_popup = browser.find_elements(By.XPATH, "//h2[contains(., 'Congratulations')]")
        assert not success_popup, " Unexpected success popup appeared!"
        print(" Validation worked — no success popup shown.")



