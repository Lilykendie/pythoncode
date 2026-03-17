import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCreatePaymentLink:

    def navigate_to_payment_links(self, browser):
        wait = WebDriverWait(browser, 40)

        # Open Collections & Receivables
        menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(),'Collections')]")
        ))
        browser.execute_script("arguments[0].click();", menu)

        # Open Payment Links
        payment_links = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(),'Payment Links')]")
        ))
        browser.execute_script("arguments[0].click();", payment_links)

        print(" Navigated to Payment Links")

    def select_customer(self, browser, customer_name):
        wait = WebDriverWait(browser, 40)

        # Click react-select wrapper
        wrapper = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'css-19bb58m')]")
        ))
        browser.execute_script("arguments[0].click();", wrapper)
        time.sleep(1)

        # Type customer name
        react_input = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@id,'react-select') and @type='text']")))
        react_input.send_keys(customer_name)
        time.sleep(1)

        # Select dropdown option
        option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(@id,'react-select') and text()='{customer_name}']")))
        browser.execute_script("arguments[0].click();", option)

        print(f" Selected customer: {customer_name}")

    def test_create_payment_link(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        self.navigate_to_payment_links(browser)

        # Open modal
        create_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Create a payment link')]")))
        browser.execute_script("arguments[0].click();", create_btn)
        print(" Opened Create Payment Link Modal ")
        time.sleep(1)

        # Select customer
        self.select_customer(browser, "Highway Supermarkets")

        # Fill payment link name
        wait.until(EC.element_to_be_clickable(
            (By.NAME, "linkName"))).send_keys("Kompany ltd")

        # ⭐ FIXED — Select ONLY visible description input
        desc = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//input[@name='description' and not(contains(@class,'hidden')) and not(@style)]"
        )))
        desc.clear()
        desc.send_keys("make payments before due date")
        print(" Filled description field")

        # Fill amount
        amount = wait.until(EC.element_to_be_clickable(
            (By.NAME, "amount")))
        amount.clear()
        amount.send_keys("1000")

        # Submit
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Create Payment Link')]"))
        )
        browser.execute_script("arguments[0].click();", submit_button)
        print(" Submitted Payment Link Form")

        # Assert success
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(.,'Payment link generated successfully')]")
        ))
        print(" Payment Link Created Successfully!")









