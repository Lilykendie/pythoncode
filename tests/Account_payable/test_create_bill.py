import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_create_bill(login):
    browser = login
    wait = WebDriverWait(browser, 20)

    # ===== 1. Navigate to Bills =====
    # Click Accounts Payable
    ap = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//p[contains(., 'Accounts Payable')]")
    ))
    ap.click()

    # Click Bills
    bills = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//p[text()='Bills']")
    ))
    bills.click()

    # Click Create a Bill
    create_bill_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Create a Bill')]")
    ))
    create_bill_btn.click()

    # ===== 2. Fill Invoice Number =====
    invoice_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Invoice No']"))
    )
    invoice_input.clear()
    invoice_input.send_keys("INV001")

    # ===== 4. Upload Invoice PDF =====
    upload_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Upload']"))
    )
    upload_btn.click()

    # Input type=file becomes visible after clicking Upload
    file_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    file_input.send_keys(r"C:\Users\LENOVO\Desktop\sample_test_invoice.pdf")

    time.sleep(2)  # Let the preview load

    # ===== 4. Select Supplier "AMS" =====
    # Click supplier dropdown (react-select input)
    supplier_dropdown = wait.until(
        EC.element_to_be_clickable((By.ID, "react-select-2-input"))
    )
    supplier_dropdown.send_keys("AMS")

    # Select from the dropdown list
    ams_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'AMS')]"))
    )
    ams_option.click()

    # ===== 5. Fill Invoice Note (the second notes field) =====
    invoice_note = wait.until(
        EC.presence_of_element_located((
            By.XPATH,
            "//textarea[contains(@placeholder, 'note') or @rows='3']"
        ))
    )
    invoice_note.clear()
    invoice_note.send_keys("Uploaded PDF with 2 items — automated test invoice.")

    # ===== 5. Click Proceed =====
    proceed_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Proceed')]"))
    )
    proceed_btn.click()

# ===== 7. Click "Submit for Approval" =====
    submit_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//button[contains(., 'Submit for Approval')]"
    ))
)
    submit_btn.click()

# ===== 8. Confirm success message =====
    success_msg = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//h2[contains(text(), 'Invoice Submitted for Approval')]"
    ))
)

    print(" Invoice successfully submitted for approval!")















    







