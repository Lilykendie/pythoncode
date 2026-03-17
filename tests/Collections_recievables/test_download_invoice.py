import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class TestDownloadInvoice:

    def navigate_to_invoices(self, browser):
        wait = WebDriverWait(browser, 30)

        # Click Collections & Receivables
        menu = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//p[contains(text(),'Collections') or contains(text(),'Receivables')]"
        )))
        browser.execute_script("arguments[0].click();", menu)

        # Click Invoices
        invoices = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//p[text()='Invoices']"
        )))
        browser.execute_script("arguments[0].click();", invoices)

        print("💜 Navigated to Invoices")

    def test_download_invoice(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        # Navigate to Invoices page
        self.navigate_to_invoices(browser)

        print("➡ Clicking invoice action menu...")

        # Locate the action chevron
        chevron = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//td[last()]//div[@aria-haspopup='menu']"
            ))
        )

        # Try normal click → fallback to JS click
        try:
            chevron.click()
        except ElementClickInterceptedException:
            browser.execute_script("arguments[0].click();", chevron)

        # Click Download Invoice option
        download_btn = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@role='menuitem' and contains(text(), 'Download Invoice')]"
            ))
        )
        browser.execute_script("arguments[0].click();", download_btn)

        print("⬇ Download initiated...")

        print("➡ Waiting for success modal...")

        # Wait for success / confirmation modal
        success = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h2[contains(text(),'Congratulations')]"
            ))
        )
        assert success is not None

        print("🎉 Successfully downloaded invoice!")

        # Close modal
        close_btn = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(text(),'Close')]"
            ))
        )
        browser.execute_script("arguments[0].click();", close_btn)

        print(" Closed success modal")



