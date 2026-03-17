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

    # ---------------- Click Pay Bills ---------------- #
    pay_bills = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Pay Bills']"))
    )
    pay_bills.click()

    # ---------------- Click Payment Memos Tab ---------------- #
    payment_memos = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Payment Memos')]")
        )
    )
    payment_memos.click()
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

    # ---------------- Click Manual Payment ---------------- #
    manual_payment = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h4[text()='Manual Payment']/following-sibling::p[contains(text(),'Pay outside')]/parent::div")
        )
    )
    manual_payment.click()

    # ---------------- Click Send for Approval ---------------- #
    send_approval = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Send for Approval']")
        )
    )
    send_approval.click()

    # Optionally, you can wait for a confirmation message
    confirmation = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Invoice Submitted for Approval')]")
        )
    )
    assert "Invoice Submitted for Approval" in confirmation.text
    print(" Bill submitted for approval successfully.")







