import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEditReminder:

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
        """Opens the Before Due section"""
        wait = WebDriverWait(browser, 20)

        before_due_tab = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Before Due Date Reminders')]")
            )
        )
        browser.execute_script("arguments[0].click();", before_due_tab)

        print(" Opened Before Due Tab")

    def test_edit_reminder(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        self.navigate_to_reminders(browser)
        self.open_before_due_tab(browser)

        # -------- CLICK EDIT ICON (pencil.svg) --------
        edit_icon = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//img[contains(@src,'pencil.svg')]")
            )
        )
        browser.execute_script("arguments[0].click();", edit_icon)
        print(" Clicked Edit Icon")

        # -------- EDIT TITLE FIELD --------
        title_field = wait.until(EC.element_to_be_clickable((By.NAME, "title")))
        title_field.clear()
        title_field.send_keys("Updated due date reminder")
        print(" Updated Title")

        # -------- EDIT SUBJECT FIELD --------
        subject_field = wait.until(EC.element_to_be_clickable((By.NAME, "emailSubject")))
        subject_field.clear()
        subject_field.send_keys("Updated Subject Line")
        print(" Updated Email Subject")

        # -------- EDIT MESSAGE BODY --------
        message_field = wait.until(EC.element_to_be_clickable((By.NAME, "messageBody")))
        message_field.clear()
        message_field.send_keys("Hello, your invoice is due soon. This is an updated reminder.")
        print(" Updated Message Body")

        # -------- SAVE TEMPLATE --------
        save_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Save Template')]")
            )
        )
        browser.execute_script("arguments[0].click();", save_btn)
        print(" Clicked Save Template")

        # -------- VERIFY SUCCESS --------
        success_message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(.,'Congratulations')]")
            )
        )
        assert success_message is not None
        print(" Reminder updated successfully!")

        # -------- CLOSE POPUP --------
        close_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Close')]")
            )
        )
        browser.execute_script("arguments[0].click();", close_btn)
    
        print(" Closed success modal")
