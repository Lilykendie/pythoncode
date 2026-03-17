import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException


class TestDeactivateSalesManager:

    def navigate_to_sales_managers(self, browser):
        """Navigate to Collections & Receivables → Sales Managers"""
        wait = WebDriverWait(browser, 30)

        menu = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p[contains(text(),'Collections') or contains(text(),'Receivables')]")
            )
        )
        browser.execute_script("arguments[0].click();", menu)

        managers = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p[text()='Sales Managers']")
            )
        )
        browser.execute_script("arguments[0].click();", managers)

        print(" Navigated to Sales Managers")


    def test_deactivate_sales_manager(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)
        actions = ActionChains(browser)

        self.navigate_to_sales_managers(browser)

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

        # Click Deactivate option

        deactivate_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='menuitem' and normalize-space()='Deactivate']")
            )
        )
        browser.execute_script("arguments[0].click();", deactivate_btn)
        print(" Clicked Deactivate option")

        # Confirm deactivate
        confirm_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Deactivate Sales Manager')]")
            )
        )
        browser.execute_script("arguments[0].click();", confirm_btn)
        print(" Confirmed deactivation")

        # Validate success message
        success_message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Congratulations')]")
            )
        )
        assert success_message is not None
        print("🎉 Manager deactivated successfully!")

        # Close the success popup
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Close')]"))
        )
        browser.execute_script("arguments[0].click();", close_btn)
        print(" Closed success modal")
