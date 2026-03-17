import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCreateInvoice:

    def navigate_to_invoices(self, browser):
        wait = WebDriverWait(browser, 30)

        collections = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//p[contains(text(),'Collections')]"
        )))
        browser.execute_script("arguments[0].click();", collections)

        invoices = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//p[normalize-space()='Invoices']"
        )))
        browser.execute_script("arguments[0].click();", invoices)

        print(" Navigated to Invoices")

    def select_react_option_by_typing(self, browser, input_id, text):
        inp = browser.find_element(By.ID, input_id)
        inp.send_keys(text)
        time.sleep(0.8)
        inp.send_keys(Keys.ENTER)

    def test_create_invoice(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)
        actions = ActionChains(browser)

        # 1. Navigate
        self.navigate_to_invoices(browser)

        # 2. Click Create Invoice
        create_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Create Invoice')]"))
        )
        browser.execute_script("arguments[0].click();", create_btn)
        print(" Opened Create Invoice modal ")
        time.sleep(0.6)

        # 3. Fill Note
        note = wait.until(EC.element_to_be_clickable((By.NAME, "note")))
        note.clear()
        note.send_keys("nil")
        print(" Filled note")

        # 4. Purchase Order number
        po = wait.until(EC.element_to_be_clickable((By.NAME, "purchaseOrderNumber")))
        po.clear()
        po.send_keys("PO-002")
        print(" Filled purchase order number")

        # 5. Select Customer (Highway Supermarkets)
        react_ids = ["react-select-4-input", "react-select-5-input", "react-select-3-input", "react-select-7-input"]
        found = False

        for rid in react_ids:
            try:
                browser.find_element(By.ID, rid)
                self.select_react_option_by_typing(browser, rid, "Highway Supermarkets")
                print(" Selected Customer: Highway Supermarkets")
                found = True
                break
            except Exception:
                continue

        if not found:
            wrapper = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[contains(@class,'css-') and .//input[@role='combobox']]"
            )))
            browser.execute_script("arguments[0].click();", wrapper)
            inp = wrapper.find_element(By.XPATH, ".//input[@role='combobox']")
            inp.send_keys("Highway Supermarkets")
            time.sleep(0.9)
            inp.send_keys(Keys.ENTER)
            print(" Selected customer via fallback")

        time.sleep(0.5)

        # 6. Item name
        item = wait.until(EC.element_to_be_clickable((By.NAME, "itemName")))
        item.send_keys("Test Item 1")
        print(" Item name filled")

        # 7. Quantity
        qty = wait.until(EC.element_to_be_clickable((By.NAME, "quantity")))
        qty.send_keys("2")
        print(" Quantity filled")

        # 8. Unit price
        price = wait.until(EC.element_to_be_clickable((By.NAME, "unitPrice")))
        price.send_keys("1000")
        print(" Unit price added")

        # 9. Tax
        tax = wait.until(EC.element_to_be_clickable((By.NAME, "tax")))
        tax.send_keys("50")
        print(" Tax added")

        # 10. Save button
        save_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[normalize-space()='Save']"
        )))
        browser.execute_script("arguments[0].click();", save_btn)
        print(" Item saved")
        time.sleep(1)

        # 11. Continue button
        cont = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[contains(.,'Continue')]"
        )))
        browser.execute_script("arguments[0].click();", cont)
        print(" Continue clicked — navigating to summary page")
        time.sleep(1)

        print("➡ Waiting for recipient summary page to load...")

       
