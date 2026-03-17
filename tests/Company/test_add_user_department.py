from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from tests.conftest import login

def add_user_to_department(browser, user_email, role_name):
    wait = WebDriverWait(browser, 20)

    # Step 1 → Navigate to Departments page
    departments_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Departments')]"))
    )
    departments_tab.click()

    # Step 2 → Click the first department
    first_department = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'bg-card')])[1]"))
    )
    first_department.click()

    # Step 3 → Select user
    user_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select users']"))
    )
    user_input.send_keys(user_email)
    time.sleep(1)
    user_input.send_keys(Keys.ENTER)

    # Step 4 → Select role
    role_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select roles']"))
    )
    role_input.send_keys(role_name)
    time.sleep(1)
    role_input.send_keys(Keys.ENTER)

    # Step 5 → Save
    save_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))
    )
    save_button.click()
    
    from pages.add_user_department import add_user_to_department

    def test_add_user_to_department(login):
    browser = login
    add_user_to_department(
        browser,
        user_email="akinyililian993@gmail.com",
        role_name="QA Engineer"
    )


