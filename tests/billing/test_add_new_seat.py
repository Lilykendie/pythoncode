import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    # --- Navigate to login page ---
    driver.get("https://staging.useklak.com/")  # replace

    # --- Enter login credentials ---
    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email.send_keys("akinyililian993@gmail.com")  # replace
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys("Company22_")  # replace

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
def test_add_seats_and_pay(login):
    driver = login
    wait = WebDriverWait(driver, 20)

    # --- Navigate to Billing under Settings ---
    settings_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Settings')]")))
    settings_btn.click()

    billing_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Billing')]")))
    billing_btn.click()

    # --- Click My Plan ---
    my_plan_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/billing/my-plan')]")))
    my_plan_btn.click()

    # --- Click Add New Seat ---
    add_new_seat_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Add New Seat']]")))
    add_new_seat_btn.click()

    # --- Click Add 1 Seat ---
    add_one_seat_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add 1 Seat']")))
    add_one_seat_btn.click()

    # --- Click Add Seats ---
    add_seats_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Seats']")))
    add_seats_btn.click()

    # --- Select Bank Authentication card ---
    bank_auth_card = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Bank Authentication']/ancestor::div[@data-testid='testCard-1']")
        )
    )
    bank_auth_card.click()

    # --- Click Pay ---
    pay_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='testCardsPaymentButton']"))
    )
    pay_button.click()

    # --- Click Authenticate ---
    authenticate_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='continueRedirect']"))
    )
    authenticate_button.click()

    # --- Confirm action ---
    success_msg = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Bank Authentication')]"))
    )

    assert "Bank Authentication" in success_msg.text
    print(" Seats added and payment authenticated successfully.")



