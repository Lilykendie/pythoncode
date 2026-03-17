import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("login")
def test_add_reminder(login):
    browser = login
    wait = WebDriverWait(browser, 20)

    # Navigate to "Collections & Receivables" → "Reminders"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Collections & Receivables')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Reminders']"))).click()

   # 3 Click "Add Reminder"
    add_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Reminder')]"))
    )
    # Wait for modal to appear
    modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))

    # Fill in Template Title
    title_input = wait.until(EC.element_to_be_clickable((By.NAME, "title")))
    title_input.clear()
    title_input.send_keys("Due Date Reminder")

    # Select "Before Due" value (React-select)
    before_due_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id^='react-select'][id$='-input']"))
    )
    before_due_input.send_keys("3 days before\n")

    # Toggle Email if needed
    email_toggle = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Email')]/following-sibling::button[@role='switch']")))
    if email_toggle.get_attribute("aria-checked") == "false":
        email_toggle.click()

    # Enter Email Subject
    subject_input = wait.until(EC.visibility_of_element_located((By.NAME, "emailSubject")))
    subject_input.clear()
    subject_input.send_keys("Invoice Due Reminder")

    # Enter Message Body
    message_input = wait.until(EC.element_to_be_clickable((By.NAME, "messageBody")))
    message_input.clear()
    message_input.send_keys("This is a friendly reminder that your invoice is due soon.")

    # Click Save Template
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save Template']")))
    save_btn.click()

    # Optionally, assert success (if any confirmation text appears)
    success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Reminder saved successfully')]")))
    assert success_msg.is_displayed()
    print(" Reminder added successfully.")







