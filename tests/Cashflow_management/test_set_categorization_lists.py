import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("login")
def test_set_categorization_lists(login):
    browser = login

    # Step 1: Wait for dashboard
    WebDriverWait(browser, 25).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Cashflow Management')]"))
    )
    print(" Dashboard loaded successfully.")

    # Step 2: Go to Cashflow Management
    cashflow_card = browser.find_element(By.XPATH, "//p[contains(text(), 'Cashflow Management')]/ancestor::a")
    browser.execute_script("arguments[0].scrollIntoView(true);", cashflow_card)
    cashflow_card.click()
    print(" Clicked Cashflow Management module.")

    # Step 3: Go to Cashflow Analysis tab
    cashflow_analysis_tab = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Cashflow Analysis')]"))
    )
    cashflow_analysis_tab.click()
    print(" Clicked Cashflow Analysis tab.")

    # Step 4: Click “Set Categorization Rule”
    set_rule_btn = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Set Categorization Rule')]"))
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", set_rule_btn)
    set_rule_btn.click()
    print(" Opened Set Categorization Rule modal.")

    # Step 5: Click on “Lists” tab
    lists_tab = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Lists')]"))
    )
    lists_tab.click()
    print(" Switched to Lists tab.")

    # Step 6: Click “Add List”
    add_list_btn = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add List')]"))
    )
    add_list_btn.click()
    print(" Clicked Add List button.")

    # Step 7: Fill in list input fields
    inputs = WebDriverWait(browser, 25).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[placeholder*='e.g.']"))
    )
    if len(inputs) >= 2:
        inputs[0].clear()
        inputs[0].send_keys("When Narration has VAT")
        inputs[1].clear()
        inputs[1].send_keys("Categorize as Vendor Payment")
        print(" Filled in list details.")
    else:
        raise Exception(" Could not find list input fields!")

    # Step 8: Click “Save Changes”
    save_btn = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save Changes')]"))
    )
    save_btn.click()
    print(" Clicked Save Changes.")

    # Step 9: Wait for success confirmation modal
    success_modal = WebDriverWait(browser, 40).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Categorization rules saved successfully')]")
        )
    )
    assert "Categorization rules saved successfully" in success_modal.text
    print(" Success: List categorization rule saved successfully!")

    # Step 10: Close success modal
    close_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Close')]"))
    )
    close_button.click()
    print(" Closed success modal.")
