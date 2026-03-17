import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("login")
def test_add_role(login):
    driver = login
    wait = WebDriverWait(driver, 30)

    # ---------------------------
    # Happy Path: Create Role Successfully
    # ---------------------------
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Company' or contains(text(),'Company')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Roles & Permissions' or contains(text(),'Roles & Permissions')]"))).click()
    add_role_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add role')]")))
    add_role_btn.click()
    time.sleep(1)  # wait for React rendering

    role_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "roleName")))
    role_name_input.clear()
    role_name_input.send_keys("QA Analyst")

    role_desc_input = wait.until(EC.visibility_of_element_located((By.NAME, "roleDescription")))
    role_desc_input.clear()
    role_desc_input.send_keys("Manage testing")

    approve_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "approve-purchase-requisition")))
    approve_checkbox.click()

    create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(),'Create')]")))
    create_btn.click()

    success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'has been created successfully')]")))
    assert "has been created successfully" in success_msg.text




