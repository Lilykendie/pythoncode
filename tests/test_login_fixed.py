import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ Fixture: Launch and close browser
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# ✅ Test 1: Valid login
def test_valid_login(browser):
    browser.get("https://staging.useklak.com/login")

    # Wait until email field is visible
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    # Find and fill in fields
    email_input = browser.find_element(By.NAME, "email")
    password_input = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    email_input.send_keys("akinyililian993@gmail.com")
    password_input.send_keys("Company22_")
    login_button.click()

    # Wait for redirect or dashboard text
    WebDriverWait(browser, 15).until(
        EC.any_of(
            EC.url_contains("/dashboard"),
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dashboard') or contains(text(), 'Welcome')]"))
        )
    )

    assert "/dashboard" in browser.current_url or "dashboard" in browser.page_source.lower()


# ❌ Test 2: Invalid login (parametrized)
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.parametrize("email, pwd", [
    ("wronguser@gmail.com", "wrongpass"),
    ("akinyililian993@gmail.com", "wrongpass"),
    ("wronguser@gmail.com", "Company22_"),
])
def test_invalid_login(browser, email, pwd):
    browser.get("https://staging.useklak.com/login")

    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    email_input = browser.find_element(By.NAME, "email")
    password_input = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    email_input.clear()
    password_input.clear()
    email_input.send_keys(email)
    password_input.send_keys(pwd)
    login_button.click()

    try:
        # Wait for modal or message
        modal = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(), 'Invalid email or password')]")
            )
        )
        assert "Invalid email or password" in modal.text
    except Exception as e:
        # Take screenshot and dump HTML for debugging
        timestamp = str(int(time.time()))
        browser.save_screenshot(f"error_debug_{timestamp}.png")
        with open(f"page_source_{timestamp}.html", "w", encoding="utf-8") as f:
            f.write(browser.page_source)
        raise e
