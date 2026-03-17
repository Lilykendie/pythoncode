import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("login")
def test_set_categorization_rule(login):
    browser = login

    # Step 1: Dashboard
    WebDriverWait(browser, 25).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Cashflow Management')]"))
    )
    print(" Dashboard loaded successfully.")

    # Step 2: Cashflow Management
    cashflow_card = browser.find_element(By.XPATH, "//p[contains(text(), 'Cashflow Management')]/ancestor::a")
    browser.execute_script("arguments[0].scrollIntoView(true);", cashflow_card)
    cashflow_card.click()
    print(" Clicked Cashflow Management module.")

    # Step 3: Cashflow Analysis
    cashflow_analysis_tab = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Cashflow Analysis')]"))
    )
    cashflow_analysis_tab.click()
    print(" Opened Cashflow Analysis tab.")

    # Step 4: Set Categorization Rule
    set_rule_btn = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Set Categorization Rule')]"))
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", set_rule_btn)
    set_rule_btn.click()
    print(" Clicked 'Set Categorization Rule'.")

    # Step 5: Wait for modal/iframe with textarea
    time.sleep(2)
    print("⌛ Waiting for categorization editor to load...")

    try:
        # If textarea is in an iframe, switch to it
        iframe = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'w-md-editor')]"))
        )
        browser.switch_to.frame(iframe)
        print(" Switched to iframe containing editor.")
    except Exception:
        print("ℹ No iframe found, continuing normally...")

    # Step 6: Wait for textarea and enter text
    textarea = WebDriverWait(browser, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.w-md-editor-text-input"))
    )
    textarea.clear()
    textarea.send_keys("Investing\nFinancing\nOperating")
    print(" Entered categorization instructions.")

    # Step 7: Save Changes
    browser.switch_to.default_content()  # Ensure we're back to main document
    save_btn = WebDriverWait(browser, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save Changes')]"))
    )
    save_btn.click()
    print(" Clicked 'Save Changes'.")

    # Step 8: Close success modal
    close_btn = WebDriverWait(browser, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Close')]"))
    )
    close_btn.click()
    print(" Closed success modal.")

    print("Instructions section complete.")











