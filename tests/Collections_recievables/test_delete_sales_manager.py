
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDeleteSalesManager:

    def navigate_to_sales_managers(self, browser):
        wait = WebDriverWait(browser, 30)
        menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(),'Collections') or contains(text(),'Receivables')]")
        ))
        browser.execute_script("arguments[0].click();", menu)

        managers = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[text()='Sales Managers']")
        ))
        browser.execute_script("arguments[0].click();", managers)
        print(" Navigated to Sales Managers")

    def test_delete_sales_manager(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

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

        # Click Delete option
        delete_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='menuitem' and normalize-space()='Delete']")
            )
        )
        browser.execute_script("arguments[0].click();", delete_btn)

        # CLICK CONFIRM DELETE BUTTON
        confirm_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[contains(text(),'Delete Sales Manager')]"
        )))
        browser.execute_script("arguments[0].click();", confirm_btn)

        print("➡ Waiting for success message...")

        # VERIFY SUCCESS MODAL
        success = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//h2[contains(text(),'Congratulations')]"
        )))
        assert success is not None

        print("🎉 Successfully deleted sales manager!")

        # CLOSE SUCCESS MODAL
        close_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[contains(text(),'Close')]"
        )))
        browser.execute_script("arguments[0].click();", close_btn)
        print(" Closed success modal")




