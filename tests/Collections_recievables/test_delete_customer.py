import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException


class TestDeleteCustomer:

    def navigate_to_customers(self, browser):
        wait = WebDriverWait(browser, 30)

        # Click Collections & Receivables
        menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(),'Collections') or contains(text(),'Receivables')]")
        ))
        browser.execute_script("arguments[0].click();", menu)

        # Click Customers
        customers = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[text()='Customers']")
        ))
        browser.execute_script("arguments[0].click();", customers)

        print(" Navigated to Customers")

    def test_delete_customer(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        # Navigate to Customers page
        self.navigate_to_customers(browser)

        print("Clicking customer action menu...")

        # Locate the action chevron
        chevron = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//td[last()]//div[@aria-haspopup='menu']")
            )
        )

        # Try normal click → fallback to JS click
        try:
            chevron.click()
        except ElementClickInterceptedException:
            browser.execute_script("arguments[0].click();", chevron)

        # Click Delete option
        delete_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='menuitem' and normalize-space()='Delete']")
            )
        )
        browser.execute_script("arguments[0].click();", delete_btn)

        # Click Confirm Delete button
        confirm_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Delete Customer')]")
            )
        )
        browser.execute_script("arguments[0].click();", confirm_btn)

        print("➡ Waiting for success modal...")

        # Wait for success message
        success = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Congratulations')]")
            )
        )
        assert success is not None
        print(" Successfully deleted customer!")

        # Close modal
        close_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Close')]")
            )
        )
        browser.execute_script("arguments[0].click();", close_btn)

        print(" Closed success modal")










