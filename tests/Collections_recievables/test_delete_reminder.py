import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class TestDeleteReminder:

    def navigate_to_reminders(self, browser):
        """Navigate to Collections & Receivables → Reminders"""
        wait = WebDriverWait(browser, 30)

        menu = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p[contains(text(),'Collections') or contains(text(),'Receivables')]")
            )
        )
        browser.execute_script("arguments[0].click();", menu)

        reminders = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Reminders']"))
        )
        browser.execute_script("arguments[0].click();", reminders)
        print(" Navigated to Reminders")

    def open_before_due_tab(self, browser):
        """Click the Before Due Date Reminders tab"""
        wait = WebDriverWait(browser, 20)

        before_due_tab = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Before Due Date Reminders')]")
            )
        )
        browser.execute_script("arguments[0].click();", before_due_tab)
        print(" Opened Before Due Tab")

    def test_delete_reminder(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        self.navigate_to_reminders(browser)
        self.open_before_due_tab(browser)

        # -------- Locate DELETE ICON (trash.svg) --------
        delete_icon = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//img[contains(@src,'trash.svg')]")
            )
        )
        browser.execute_script("arguments[0].click();", delete_icon)
        print("🗑️ Clicked Delete Icon")

        # -------- Confirm Delete Modal --------
        confirm_delete_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Delete Reminder')]")
            )
        )
        browser.execute_script("arguments[0].click();", confirm_delete_btn)
        print(" Confirmed delete")

        # -------- SUCCESS MESSAGE --------
        success_msg = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(.,'Congratulations')]")
            )
        )
        assert success_msg is not None
        print(" Reminder deleted successfully!")

        # -------- Close Success Modal --------
        close_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Close')]")
            )
        )
        browser.execute_script("arguments[0].click();", close_btn)
        print(" Closed success modal")
