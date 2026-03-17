import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_create_purchase_requisition(login):
    browser = login
    wait = WebDriverWait(browser, 20)

    # Step 1: Navigate to Procurement -> Purchase Requisitions
    procurement_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Procurements')]"))
    )
    procurement_tab.click()

    purchase_requisition_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Purchase Requisitions')]"))
    )
    purchase_requisition_tab.click()

    # Step 2: Click "Create Purchase Requisition"
    create_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create a Purchase Requisition')]"))
    )
    create_btn.click()

    # Step 3: Pick a Date (e.g., 24th)
    date_picker = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Pick a date')]"))
    )
    date_picker.click()

    day_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='day' and text()='24']"))
    )
    day_btn.click()


    # Step 4: Select department "IT department"
    dept_input = wait.until(
    EC.element_to_be_clickable((By.ID, "react-select-2-input"))
    )
    dept_input.send_keys("IT department")
 
    # Wait a moment for the dropdown to render
    time.sleep(0.5)

    # Press Enter to select the first matching option
    dept_input.send_keys("\n")

    
    # Step 5: Fill in item details
    item_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Item description']"))
    )
    item_input.send_keys("mouse")

    quantity_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='number']"))
    )
    quantity_input.clear()
    quantity_input.send_keys("1")

    purpose_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Purpose']"))
    )
    purpose_input.send_keys("office use")

    # Step 6: Enter document name
    doc_name_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g. Catalog, Photo of item, etc.']"))
    )
    doc_name_input.send_keys("sample")


    # Step 8: Click Preview
    preview_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Preview']"))
    )
    preview_btn.click()

    # Step 9: Click Submit for Approval
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit for Approval']"))
    )
    submit_btn.click()

    # Optional: verify success (if there’s a success message)
    success_msg = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'submitted successfully')]"))
    )
    assert "submitted successfully" in success_msg.text.lower()


