from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class TestViewInvoice:

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

        print(" Navigated to Invoices")

    def test_view_invoice(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        self.navigate_to_invoices(browser)

        print("➡ Clicking invoice action menu...")

        # Locate the action chevron
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
        print(" Viewing invoice...")

        # --- Assertions to ensure invoice page is loaded ---
        
        # 1. Invoice Number Section
        invoice_number = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//p[contains(text(),'Invoice Number:')]"
            ))
        )
        
        # 2. "Bill To" customer name
        bill_to = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//p[text()='Bill To']/following-sibling::p"
            ))
        )

        # 3. Settlement Section Title
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



