import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddCustomer:

    def navigate_to_customers(self, browser):
        """Navigate to Collections & Receivables → Customers"""
        wait = WebDriverWait(browser, 30)

        # Click Collections & Receivables menu
        menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(),'Collections') or contains(text(),'Receivables')]")
        ))
        browser.execute_script("arguments[0].click();", menu)

        # Click Customers
        customers = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(),'Customers')]")
        ))
        browser.execute_script("arguments[0].click();", customers)
        print(" Navigated to Customers screen")

    def test_add_customer_valid(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        self.navigate_to_customers(browser)

        # Open Add Customer form
        add_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add a Customer')]"))
        )
        browser.execute_script("arguments[0].click();", add_btn)
        print(" Opened Add Customer modal")

        # ---- RANDOM TEST DATA ----
        rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        company = f"TestCo_{rand}"
        email = f"test{rand.lower()}@mail.com"
        phone = "+8023675489"
        code = f"CUST{rand}"

        # ---- FILL CUSTOMER FIELDS ----
        wait.until(EC.presence_of_element_located((By.NAME, "companyName"))).send_keys(company)
        browser.find_element(By.NAME, "firstName").send_keys("Dorcas")
        browser.find_element(By.NAME, "lastName").send_keys("QA")
        browser.find_element(By.NAME, "email").send_keys(email)

        phone_input = browser.find_element(
            By.XPATH, "//input[@placeholder='Enter phone number (+234)']"
        )
        phone_input.send_keys(phone)

        browser.find_element(By.NAME, "customerCode").send_keys(code)
        browser.find_element(By.NAME, "address").send_keys("Abuja Nigeria")
        print(" Filled customer fields")

        # ---- SELECT STATE (React Select ID: 4) ----
        state_box = wait.until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
        state_box.send_keys("Abuja")
        time.sleep(1)
        state_box.send_keys("\n")
        print(" Selected State")

        # ---- SELECT SALES MANAGER (React Select ID: 3) ----
        print("➡ Selecting Sales Manager")

        sales_mgr_input = wait.until(
            EC.element_to_be_clickable((By.ID, "react-select-3-input"))
        )

        browser.execute_script("arguments[0].click();", sales_mgr_input)
        sales_mgr_input.send_keys("jane")
        time.sleep(1)

        # React re-renders → RE-FETCH INPUT to avoid stale element
        sales_mgr_input = wait.until(
            EC.presence_of_element_located((By.ID, "react-select-3-input"))
        )
        sales_mgr_input.send_keys("\n")

        print(" Sales Manager selected successfully")

        # ---- SUBMIT CUSTOMER ----
        submit = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Customer')]"))
        )
        browser.execute_script("arguments[0].click();", submit)
        print(" Submitted Add Customer form")

        # ---- VERIFY SUCCESS ----
        cust_success = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Congratulations')]"))
        )
        assert cust_success is not None
        print(" Customer created successfully.")

    def test_add_customer_empty_fields(self, login):
        browser = login
        wait = WebDriverWait(browser, 30)

        self.navigate_to_customers(browser)

        add_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Add a Customer')]")
        ))
        browser.execute_script("arguments[0].click();", add_btn)

        # Try submitting empty form
        submit = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add Customer')]"))
        )
        submit.click()
        print(" Tried to submit empty form")

        time.sleep(1)

        # Should not submit
        assert not submit.is_enabled() or "disabled" in submit.get_attribute("class")

        print(" Empty field validation works")






