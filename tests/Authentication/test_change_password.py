import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("login")
def test_change_password(login):
    driver = login  # Logged-in driver from your login fixture
    wait = WebDriverWait(driver, 20)

    # --- Navigate to User & Business Profile ---
    user_profile_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'User & Business Profile')]"))
    )
    user_profile_btn.click()

    # --- Click Change Password ---
    change_password_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Change Password')]"))
    )
    change_password_btn.click()

    # --- Fill in passwords ---
    wait.until(EC.presence_of_element_located((By.NAME, "oldPassword"))).send_keys("Company22_")
    driver.find_element(By.NAME, "newPassword").send_keys("Company23_")
    driver.find_element(By.NAME, "confirmPassword").send_keys("Company23_")

    # --- Submit the form ---
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    submit_btn.click()

    # --- Verify success message ---
    success_msg = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Password updated successfully')]"))
    )
    assert success_msg.is_displayed()

    print(" Password updated successfully")

