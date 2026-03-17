import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("login")
def test_edit_profile(login):
    driver = login  # logged-in driver from login fixture
    wait = WebDriverWait(driver, 20)

    # --- Navigate to User & Business Profile ---
    user_profile_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'User & Business Profile')]"))
    )
    user_profile_btn.click()
    print(" Navigated to User & Business Profile")

    # --- Click Edit Profile ---
    edit_profile_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Edit Profile')]"))
    )

    # Wait for any overlay/modal to disappear
    try:
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.fixed.inset-0.bg-black.bg-opacity-70")))
    except:
        pass  # if overlay not present, continue

    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", edit_profile_btn)

    # Click using JS to avoid interception
    driver.execute_script("arguments[0].click();", edit_profile_btn)
    print(" Clicked Edit Profile")

    # --- Fill in profile fields ---
    first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    first_name_input.clear()
    first_name_input.send_keys("Bridgette")

    last_name_input = driver.find_element(By.NAME, "lastName")
    last_name_input.clear()
    last_name_input.send_keys("Sharpton")
    print(" Updated profile fields")

    # --- Submit the form ---
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Edit Profile')]")

    # Scroll and JS click for submit button
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    driver.execute_script("arguments[0].click();", submit_btn)
    print(" Submitted profile update")

    # --- Verify success message ---
    success_msg = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Congratulations')]"))
    )
    assert "Congratulations" in success_msg.text
    print(" Profile updated successfully")

    # --- Verify success message ---
    success_modal = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Congratulations 🎉')]")
    )
    )
    assert "User info updated successfully" in driver.page_source
    print(" Profile updated successfully")

    # --- Close the success modal ---
    close_btn = success_modal.find_element(
    By.XPATH, "//button[contains(text(),'Close')]"
   )
    driver.execute_script("arguments[0].click();", close_btn)
    print(" Closed success modal")