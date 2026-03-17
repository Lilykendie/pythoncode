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

    # Step 4: Click "change Status " inside the modal
    change_status_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Change Status']"))
    )
    browser.execute_script("arguments[0].click();", change_status_btn)

   
    # STEP 5 → Wait for Change Status dialog
    status_dialog = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='dialog' and .//h2[contains(text(),'Update Delivery Status')]]"))
   )

    # STEP 6 → Open React Select dropdown
    dropdown = status_dialog.find_element(By.XPATH, ".//div[contains(@class,'react-select__control')]")
    dropdown.click()

    # STEP 7 → Select desired status
    desired_status = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class,'react-select__option') and normalize-space()='Not Delivered']")
    )
    )
    desired_status.click()

    # STEP 8 → Enter reason
    reason_input = status_dialog.find_element(By.XPATH, ".//textarea[@name='reason']")
    reason_input.send_keys("Delivered on time")

    # STEP 9 → Click Update Status
    update_button = status_dialog.find_element(By.XPATH, ".//button[normalize-space()='Update Status']")
    update_button.click()
    