import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("login")
def test_add_department(login):
    driver = login
    wait = WebDriverWait(driver, 30)

    # 1 Navigate to Company → Departments
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Company']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Departments']"))).click()
    time.sleep(1)  # wait for form to render

    # 2 Enter Department Name
    dept_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "teams.0.name")))
    dept_name_input.clear()
    dept_name_input.send_keys("Logistics")

    # 3 Enter Department Description (optional)
    dept_desc_input = driver.find_element(By.NAME, "teams.0.description")
    dept_desc_input.clear()
    dept_desc_input.send_keys("Manage logistics")

    # 4 Select "QA Manager" role
    try:
        # Try clicking dropdown and selecting
        role_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select roles']")))
        role_dropdown.click()
        time.sleep(1)
        qa_role = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'absolute') and contains(@class,'z-50')]//span[contains(text(),'QA manager')] | //p[contains(text(),'QA manager')]")
        ))
        qa_role.click()
    except:
        # Fallback: use JS to set role directly
        driver.execute_script("""
            let roleInput = document.querySelector("input[placeholder='Select roles']");
            roleInput.value = 'QA manager';
            roleInput.dispatchEvent(new Event('input', { bubbles: true }));
        """)

    # 5 Enter Budget (4000)
    budget_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter budget amount']")
    budget_input.clear()
    budget_input.send_keys("4000")

    # 6 Skip date (do nothing)

    # 7 Click Add Department button
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add department')]")))
    add_btn.click()

    # Optional: wait for confirmation or success toast
    time.sleep(2)








