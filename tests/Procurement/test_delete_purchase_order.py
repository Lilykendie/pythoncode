import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

def test_delete_purchase_order(login):
    browser = login
    wait = WebDriverWait(browser, 20)

    # Step 1: Navigate to Procurement -> Purchase Orders
    procurement_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Procurements')]"))
    )
    procurement_tab.click()

    purchase_order_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Purchase Orders')]"))
    )
    purchase_order_tab.click()

    # Step 2: Open dropdown menu in the last column of the row you want to delete
    chevron = wait.until(
        EC.presence_of_element_located((By.XPATH, "//td[last()]//div[@aria-haspopup='menu']"))
    )
    actions = ActionChains(browser)
    actions.move_to_element(chevron).click().perform()

    # Fallback click if intercepted
    try:
        chevron.click()
    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", chevron)

    # Step 3: Click Delete Purchase Order option
    delete_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and normalize-space()='Delete Purchase Order']"))
    )
    browser.execute_script("arguments[0].click();", delete_btn)

    # Step 4: Click Delete Purchase Order button in confirmation modal
    confirm_delete_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Delete Purchase Order']"))
    )
    try:
        confirm_delete_btn.click()
    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", confirm_delete_btn)

    # Optional wait for UI update
    time.sleep(1)

    # Step 5: Close success modal if exists
    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']"))
    )
    close_btn.click()

    print(" Purchase order deleted successfully.")

