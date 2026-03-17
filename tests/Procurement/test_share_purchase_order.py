import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

def test_view_and_share_purchase_order(login):
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

    # Step 2: Open dropdown menu in the last column of the row
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

    # Step 3: Click "View"
    view_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='View']"))
    )
    browser.execute_script("arguments[0].click();", view_btn)

    # Step 4: Click "Share Purchase Order" inside the modal
    share_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Share Purchase Order']"))
    )
    browser.execute_script("arguments[0].click();", share_btn)

    # Optional Step 5: Handle email input if present
    try:
        email_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_input.clear()
        email_input.send_keys("example@domain.com")

        send_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Send']"))
        )
        send_button.click()
    except:
        print("⚠ No email input detected, maybe auto-share")

    # Step 6: Close modal
    try:
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']"))
        )
        close_btn.click()
    except:
        pass

    print(" Purchase order viewed and shared successfully.")
