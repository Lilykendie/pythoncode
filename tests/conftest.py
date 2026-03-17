import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login(browser):
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if not email or not password:
        raise Exception("❌ EMAIL or PASSWORD not found in .env file.")

    browser.get("https://staging.useklak.com/login")

    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    try:
        WebDriverWait(browser, 30).until(
            EC.any_of(
                EC.url_contains("/dashboard"),
                EC.url_contains("/cashflow"),
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Cashflow')]"))
            )
        )
        print("✅ Logged in successfully.")
    except Exception:
        print("⚠️ Login may have succeeded but dashboard not detected.")

    return browser


