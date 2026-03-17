from concurrent.futures import wait
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pay_unpaid_bill(login):
    driver = login
    wait = WebDriverWait(driver, 20)

    # ---------------- Click Accounts Payable ---------------- #
    accounts_payable = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Accounts Payable')]"))
    )
    accounts_payable.click()

    # ---------------- Click Pay Bills ---------------- #
    pay_bills = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Pay Bills']"))
    )
    pay_bills.click()

    # ---------------- Select Unpaid Bills Tab ---------------- #
    unpaid_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Unpaid Bills']"))
    )
    unpaid_tab.click()
    # ---------------- Click Action Icon (Chevron) ---------------- #
    action_chevron = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//td[last()]//div[@aria-haspopup='menu']"))
    )
    driver.execute_script("arguments[0].click();", action_chevron)
    print("➡ Action dropdown opened. Clicking View Bill...")
# ---------------- Click View Bill from dropdown ---------------- #
    view_bill = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and text()='View Bill']"))
    )
    driver.execute_script("arguments[0].click();", view_bill)
    print("➡ View Bill opened.")

   # CLICK CHANGE STATUS
    change_status_btn = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//button[contains(text(), 'Change Status')]"
)))
    driver.execute_script("arguments[0].click();", change_status_btn)

# WAIT FOR MODAL
    wait.until(EC.visibility_of_element_located((
    By.XPATH, "//div[contains(text(), 'Change Payment Status')]"
   )))

# ENTER REFERENCE ID
    reference_input = wait.until(EC.element_to_be_clickable((
    By.NAME, "transactionReference"
   )))
    reference_input.send_keys("TXN-123456")

# CLICK SAVE CHANGES
    save_btn = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//button[@type='submit' and contains(text(), 'Save Changes')]"
)))
    driver.execute_script("arguments[0].click();", save_btn)
    print(" Payment updated successfully!")
