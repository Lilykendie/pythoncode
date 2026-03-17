import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def test_download_purchase_requisition_report(login):
    browser = login
    wait = WebDriverWait(browser, 20)

def test_download_purchase_requisition_report(login):
    browser = login
    wait = WebDriverWait(browser, 20)

   # Step 1: Navigate to Procurement tab
    procurement_tab = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Procurements')]"))
)
    procurement_tab.click()
    time.sleep(1)  # wait for menu to expand

    # Step 2: Click on Purchase Requisition tab
    purchase_requisition_tab = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Purchase Requisitions')]"))
)
    purchase_requisition_tab.click()


    # Step 3: Click on Download Report button
    download_report_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Download Report')]"))
    )
    download_report_btn.click()

    # Optional: Wait for file to download (adjust path and filename as needed)
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    timeout = 30
    file_downloaded = False
    for _ in range(timeout):
        files = os.listdir(download_dir)
        if any(f.endswith(".csv") or f.endswith(".xlsx") for f in files):
            file_downloaded = True
            break
        time.sleep(1)

    assert file_downloaded, " Purchase Requisition report was not downloaded."
    print(" Purchase Requisition report downloaded successfully.")
