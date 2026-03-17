import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

def test_view_purchase_requisition(login):
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

    # Force click if normal click is blocked
    try:
        chevron.click()
    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", chevron)

    # Step 3: Click "View" option
    view_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and normalize-space()='View']"))
    )
    browser.execute_script("arguments[0].click();", view_btn)

    # Step 4: Wait for modal/details panel to appear
    modal = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'modal') or contains(@class,'shadow-lg')]"))
    )
    assert modal.is_displayed(), " Purchase Requisition modal not displayed"
    print(" Purchase Requisition viewed successfully.")

    # Step 5: Close modal
    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']"))
    )
    close_btn.click()
