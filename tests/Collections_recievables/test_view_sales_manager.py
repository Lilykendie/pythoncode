import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestViewSalesManager:

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
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Sales Managers']"))
        )
        browser.execute_script("arguments[0].click();", managers)

        print(" Navigated to Sales Managers")

    def open_first_dropdown(self, browser):
        """Opens the dropdown of the first sales manager row."""
        wait = WebDriverWait(browser, 40)
        actions = ActionChains(browser)

        # Find the chevron in the last column of the first row
        chevron = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//td[last()]//div[@aria-haspopup='menu'])[1]")
            )
        )

        actions.move_to_element(chevron).perform()
        time.sleep(0.3)

        browser.execute_script("arguments[0].click();", chevron)
        print("➡ Opened manager action dropdown")

    def test_view_sales_manager(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        self.navigate_to_sales_managers(browser)

        # ---- OPEN DROPDOWN ----
        self.open_first_dropdown(browser)

        # ---- CLICK VIEW ----
        view_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='menuitem' and normalize-space()='View']")
            )
        )
        browser.execute_script("arguments[0].click();", view_button)
        print(" Clicked View")

        # ---- VERIFY VIEW PAGE LOADED ----
        print("➡ Verifying View Sales Manager page...")

        name_header = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//p[contains(@class,'font-extrabold') and contains(@class,'text-purple-800')]"
                )
            )
        )

        manager_name = name_header.text.strip()
        assert manager_name != ""

        print(f" View Sales Manager page loaded successfully! Name: {manager_name}")

        # Also verify the "All Customers" section exists
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[text()='All Customers']")
            )
        )

        print(" 'All Customers' section is visible — View page is correct.")




