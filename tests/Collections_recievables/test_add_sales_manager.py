import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddSalesManager:

    def navigate_to_sales_managers(self, browser):
        """Navigate to Collections & Receivables → Sales Managers"""
        wait = WebDriverWait(browser, 30)

        # Click Collections & Receivables menu
        menu = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p[contains(text(),'Collections') or contains(text(),'Receivables')]")
            )
        )
        browser.execute_script("arguments[0].click();", menu)

        # Click Sales Managers
        sales_mng = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p[text()='Sales Managers']")
            )
        )
        browser.execute_script("arguments[0].click();", sales_mng)

        print(" Navigated to Sales Managers")

    def test_add_sales_manager_valid(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        self.navigate_to_sales_managers(browser)

        # Click Add Sales Manager
        add_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add a Sales Manager')]"))
        )
        browser.execute_script("arguments[0].click();", add_btn)
        print(" Opened Add Sales Manager modal")

        # ---- RANDOM TEST DATA ----
        rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        first = f"Mary{rand}"
        last = f"Atieno{rand}"
        phone = "+8022345678"
        code = f"SM{rand}"
        email = f"sales{rand.lower()}@mail.com"

        # ---- FILL FORM ----
        wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first)
        browser.find_element(By.NAME, "lastName").send_keys(last)

        phone_input = browser.find_element(
            By.XPATH, "//input[@placeholder='Enter phone number (+234)']"
        )
        phone_input.clear()
        phone_input.send_keys(phone)

        browser.find_element(By.NAME, "agentCode").send_keys(code)
        browser.find_element(By.NAME, "agentEmail").send_keys(email)

        print(" Filled Sales Manager fields")

        # ---- SUBMIT ----
        submit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add Sales Manager')]"))
        )
        browser.execute_script("arguments[0].click();", submit_btn)
        print(" Submitted Sales Manager form")

        # ---- VERIFY SUCCESS ----
        success_heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Congratulations')]")
            )
        )
        assert success_heading is not None
        print(" Sales Manager created successfully!")

        # Close success modal
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Close')]"))
        )
        browser.execute_script("arguments[0].click();", close_btn)
        print(" Closed success modal")

    def test_add_sales_manager_empty_fields(self, login):
        browser = login
        wait = WebDriverWait(browser, 30)

        self.navigate_to_sales_managers(browser)

        # Click Add Sales Manager
        add_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add a Sales Manager')]"))
        )
        browser.execute_script("arguments[0].click();", add_btn)
        print(" Opened Add Sales Manager modal")

        # Wait for form to load
        first_name = wait.until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )

        # Ensure fields are empty
        assert first_name.get_attribute("value") == ""

        # Locate submit button
        submit_btn = browser.find_element(
            By.XPATH, "//button[contains(text(),'Add Sales Manager')]"
        )

        # Try submitting empty form
        browser.execute_script("arguments[0].click();", submit_btn)
        print(" Tried to submit empty form")

        time.sleep(1)

        # Validation: button should not allow submit
        assert not submit_btn.is_enabled() or "disabled" in submit_btn.get_attribute("class")

        print(" Empty field validation working")
