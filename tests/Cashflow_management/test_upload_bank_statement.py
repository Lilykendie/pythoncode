
import os
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("login")
def test_upload_bank_statement(login):
    browser = login

    # Step 1: Wait for dashboard to load
    WebDriverWait(browser, 25).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Cashflow Management')]"))
    )
    print(" Dashboard loaded successfully.")

    # Step 2: Click on "Cashflow Management"
    cashflow_card = browser.find_element(
        By.XPATH, "//p[contains(text(), 'Cashflow Management')]/ancestor::a"
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", cashflow_card)
    time.sleep(1)
    cashflow_card.click()
    print(" Clicked Cashflow Management module.")

    # Step 3: Click "Add Bank Account"
    add_account = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Add Bank Account')]"))
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", add_account)
    time.sleep(1)
    add_account.click()
    print(" Clicked Add Bank Account.")

    # Step 4: Click "Upload Bank Statement"
    upload_card = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.XPATH, "//h3[contains(text(), 'Upload Bank Statement')]"))
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", upload_card)
    time.sleep(1)
    upload_card.click()
    print(" Opened Upload Bank Statement section.")

    # Step 5: Wait for upload form
    WebDriverWait(browser, 25).until(
        EC.presence_of_element_located((By.NAME, "bankTitle"))
    )

    # Step 6: Fill in form details
    browser.find_element(By.NAME, "bankTitle").send_keys("OLUWASEUN SAMUEL AYEGBUSI")
    browser.find_element(By.NAME, "accountNumber").send_keys("3880117122")
    print(" Filled in account title and number.")

    # Step 7: Select Bank Name
    bank_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[label[contains(text(), 'Bank')]]//input[contains(@id, 'react-select')]"))
    )
    bank_input.send_keys("Ecobank\n")
    print(" Selected Bank: Ecobank.")

    # Step 8: Select Account Type
    account_type_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[label[contains(text(), 'Account Type')]]//input[contains(@id, 'react-select')]"))
    )
    account_type_input.send_keys("Current\n")
    print(" Selected Account Type: Current.")

    # Step 9: Select Currency
    currency_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[label[contains(text(), 'Currency')]]//input[contains(@id, 'react-select')]"))
    )
    currency_input.send_keys("Nigerian Naira\n")
    print(" Selected Currency: Nigerian Naira.")

    # Step 10: Create a sample dummy PDF to upload
    pdf_folder = os.path.abspath("bank_statements")
    os.makedirs(pdf_folder, exist_ok=True)
    sample_pdf = os.path.join(pdf_folder, "sample_statement.pdf")

    # Create file if it doesn't exist
    if not os.path.exists(sample_pdf):
        with open(sample_pdf, "wb") as f:
            f.write(b"%PDF-1.4\n%Dummy PDF for testing upload\n%%EOF")

    print(f" Sample PDF created at {sample_pdf}")

    # Step 11: Upload the file
    file_input = WebDriverWait(browser, 25).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file'][name='statement']"))
    )
    browser.execute_script("arguments[0].style.display = 'block';", file_input)
    file_input.send_keys(sample_pdf)
    print(" Uploaded sample bank statement file.")

    # Step 12: Click "Import Statement" button
    import_button = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Import Statement')]"))
    )
    import_button.click()
    print(" Clicked Import Statement button.")

    # Step 13: Confirm upload success
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'successfully') or contains(text(), 'processed')]"))
    )
    print(" Bank statement uploaded successfully!")












