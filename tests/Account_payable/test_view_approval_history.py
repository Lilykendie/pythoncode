import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pay_bill(login):
    driver = login
    wait = WebDriverWait(driver, 20)

    # ---------------- Click Accounts Payable ---------------- #
    accounts_payable = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Accounts Payable')]"))
    )
    accounts_payable.click()


    # ---------------- Navigate to Approvals ---------------- #
    approvals_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Approvals']"))
    )
    approvals_menu.click()

    # ---------------- Click 'View History' Button ---------------- #
    view_history_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'View History')]"))
    )
    driver.execute_script("arguments[0].click();", view_history_btn)
    print("➡ Clicked View History.")

    # ---------------- Validate Approvals History Modal/Page Opened ---------------- #
    approvals_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Approvals History']"))
    )

    assert approvals_header.is_displayed(), "❌ Approvals History page did NOT open!"
    print(" Approvals History opened successfully.")
