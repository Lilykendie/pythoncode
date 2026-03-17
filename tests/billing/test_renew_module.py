import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Login fixture ---
@pytest.fixture
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    # --- Navigate to login page ---
    driver.get("https://staging.useklak.com/")  # Replace with your login URL

    # --- Enter login credentials ---
    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email.send_keys("akinyililian993@gmail.com")  # Replace with your email
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys("Company22_")  # Replace with your password

    # --- Click Login button ---
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
    )
    login_button.click()

    # --- Wait for dashboard to load (Settings menu) ---
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Settings')]"))
    )

    yield driver
    driver.quit()


# --- Test: Renew Module ---
def test_renew_subscription(login):
    driver = login
    wait = WebDriverWait(driver, 20)

    # --- Navigate to Settings → Billing ---
    settings_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Settings')]")))
    settings_menu.click()

    billing_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Billing')]")))
    billing_option.click()

    # --- Navigate to My Plan ---
    my_plan_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/billing/my-plan')]")))
    my_plan_btn.click()

 # Click Renew Module
    renew_module = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//span[contains(text(),'Renew Module')]")
   ))
    renew_module.click()

# Click Renew Subscription
    renew_subscription_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'Renew Subscription')]")
   ))
    renew_subscription_btn.click()

# Select Bank Authentication card
    bank_auth_card = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@data-testid='testCard-1']")
   ))
    bank_auth_card.click()

# Click Authenticate to complete payment
    authenticate_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@data-testid='continueRedirect']")
    ))
    authenticate_btn.click()
