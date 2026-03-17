import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Login Fixture ---
@pytest.fixture
def login():
    driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    driver.maximize_window()
    
    # Navigate to login page
    driver.get("https://staging.useklak.com/login")  # <-- Replace with your actual login URL
    
    wait = WebDriverWait(driver, 20)
    
    # Enter username/email
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    username_input.clear()
    username_input.send_keys("akinyililian993@gmail.com")  # <-- Replace with your login email
    
    # Enter password
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("Company22_")  # <-- Your current password
    
    # Click login
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    
    # Wait until login is successful (dashboard/profile visible)
    wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'User & Business Profile')]")))
    
    print(" Logged in successfully.")
    yield driver
    
    driver.quit()


# --- Test: Delete Profile Picture ---
def test_delete_profile_photo(login):
    driver = login
    wait = WebDriverWait(driver, 20)
    
    # Navigate to User & Business Profile
    user_profile_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'User & Business Profile')]"))
    )
    user_profile_btn.click()
    
    # Click Delete Profile Photo button
    delete_photo_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Delete Profile Photo')]"))
    )
    delete_photo_btn.click()
    
    # Wait for success modal
    success_modal = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'Profile picture deleted successfully')]")
        )
    )
    
    assert success_modal.is_displayed()
    print(" Profile picture deleted successfully.")
    
    # Close the success modal
    close_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Close')]")
    close_btn.click()

