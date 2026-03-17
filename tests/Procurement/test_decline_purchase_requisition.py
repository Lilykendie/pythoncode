import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

def test_decline_purchase_requisition(login):
    browser = login
    wait = WebDriverWait(browser, 20)

     # 1. Navigate to Procurements
    procurements_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Procurements')]"))
    )
    procurements_menu.click()

    # 2. Click Approvals
    approvals_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Approvals')]"))
    )
    approvals_menu.click()
    # Step 2: Open the purchase_requisition dropdown (if needed) and click "View"
    view_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'View')]"))
    )
    browser.execute_script("arguments[0].click();", view_btn)

    # Step 3: Click Decline
    decline_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Decline']"))
    )
    browser.execute_script("arguments[0].click();", decline_btn)

    # Step 4: Enter decline message
    message_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Write message to send to the receiver of the invoice']"))
    )
    message_box.clear()
    message_box.send_keys("Declined via automation test")

    # Step 5: Click Submit
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
    )
    browser.execute_script("arguments[0].click();", submit_btn)

    # Step 6: Optionally, wait for success modal and verify
    success_modal = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'shadow-lg')]"))
    )
    assert success_modal.is_displayed(), "❌ Decline confirmation not displayed"
    print(" Purchase Requisition declined successfully.")

    # Step 7: Close modal (if there's a Close button)
    try:
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']"))
        )
        close_btn.click()
    except:
        pass
