from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class TestViewInvoice:

    def navigate_to_invoices(self, browser):
        wait = WebDriverWait(browser, 30)

        menu = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//p[contains(text(),'Collections') or contains(text(),'Receivables')]"
        )))
        browser.execute_script("arguments[0].click();", menu)

        invoices = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//p[text()='Invoices']"
        )))
        browser.execute_script("arguments[0].click();", invoices)

        print("💜 Navigated to Invoices")

    def test_view_and_share_invoice(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        self.navigate_to_invoices(browser)

        print("➡ Clicking invoice action menu...")

        chevron = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//td[last()]//div[@aria-haspopup='menu']"
            ))
        )

        try:
            chevron.click()
        except ElementClickInterceptedException:
            browser.execute_script("arguments[0].click();", chevron)

        # Click View Invoice
        view_btn = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@role='menuitem' and contains(text(),'View Invoice')]"
            ))
        )
        browser.execute_script("arguments[0].click();", view_btn)
        print("👁 Viewing invoice...")

        # --- Assertions for invoice page ---
        invoice_number = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//p[contains(text(),'Invoice Number:')]"
            ))
        )
        bill_to = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//p[text()='Bill To']/following-sibling::p"
            ))
        )
        settlement_header = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//p[contains(text(),'Settlement')]"
            ))
        )

        assert invoice_number.is_displayed()
        assert bill_to.is_displayed()
        assert settlement_header.is_displayed()
        print(" Invoice page loaded successfully!")

        # --- Click Share Invoice ---
        share_btn = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[.//p[contains(text(),'Share Invoice')]]"
            ))
        )
        browser.execute_script("arguments[0].click();", share_btn)
        print(" Share Invoice clicked!")
        # Wait for the Share Invoice modal to appear
        share_modal = wait.until(
        EC.visibility_of_element_located((
                By.XPATH, "//p[contains(text(),'Share Invoice') and ancestor::div[@role='dialog']]"
            ))
        )
        print(" Share Invoice modal appeared")
        # Optional: verify recipient email
        recipient_input = browser.find_element(
        By.XPATH, "//input[@value='del-019a91e003c47540aee7f644cdc864d4@useklak.com']"
      )
        assert recipient_input.is_displayed()

        # Optional: fill in a custom email message
        message_box = browser.find_element(
            By.XPATH, "//textarea[contains(@placeholder,'Write a message')]"
        )
        message_box.clear()
        message_box.send_keys("Automated test: sharing invoice via Selenium")

       # Locate the Share Invoice button at the bottom
        share_confirm_btn = wait.until(
        EC.presence_of_element_located((
        By.XPATH, "//button[contains(@class,'bg-purple-1000') and .//text()[contains(.,'Share Invoice')]]"
    ))
)
        # Click Share Invoice button in modal
        share_confirm_btn = wait.until(
        EC.element_to_be_clickable((
        By.XPATH, "//button[.//p[contains(text(),'Share Invoice')]]"
        ))
        )
        browser.execute_script("arguments[0].click();", share_confirm_btn)

        print(" Invoice shared successfully!")

       


