import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

def test_edit_purchase_requisition(login):
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

    # Step 2: Open dropdown menu in the last column
    chevron = wait.until(
        EC.presence_of_element_located((By.XPATH, "//td[last()]//div[@aria-haspopup='menu']"))
    )
    actions = ActionChains(browser)
    actions.move_to_element(chevron).click().perform()

    try:
        chevron.click()
    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", chevron)

    # Step 3: Click Edit option
    edit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and normalize-space()='Edit']"))
    )
    browser.execute_script("arguments[0].click();", edit_btn)

    # Step 4: Click Update Preview first
    update_preview_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Update Preview']"))
    )
    try:
        update_preview_button.click()
    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", update_preview_button)

    # Small wait to ensure UI updates after Update Preview
    time.sleep(1)

    # Step 5: Click Update Requisition
    update_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Update Requisition']"))
    )
    try:
        update_button.click()
    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", update_button)

    # Step 6: Wait for Done button in success modal
    done_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Done']"))
    )
    done_button.click()

    print(" Purchase requisition updated successfully.")

