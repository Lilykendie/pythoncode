import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("login")
def test_edit_any_department(login):
    driver = login
    wait = WebDriverWait(driver, 30)

    # 1 Navigate to Company → Departments
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Company']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Departments']"))).click()
    time.sleep(1)  # wait for department list to render

    # 2 Click the edit button for the first department in the list
    first_edit_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "(//button[.//svg[contains(@class,'lucide-file-pen-line')]])[1]"  # first department edit button
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", first_edit_btn)
    first_edit_btn.click()
    time.sleep(1)

    # 3 Update Department Name
    dept_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "teams.0.name")))
    dept_name_input.clear()
    dept_name_input.send_keys("IT Department Updated")

    # 4 Update Department Description
    dept_desc_input = driver.find_element(By.NAME, "teams.0.description")
    dept_desc_input.clear()
    dept_desc_input.send_keys("Manage IT operations efficiently")

    # 5 Force-enter role using JS
    role_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select roles']")))
    driver.execute_script("arguments[0].value = 'QA manager'; arguments[0].dispatchEvent(new Event('input'));", role_input)
    time.sleep(1)

    # 6 Enter Budget (4000)
    budget_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter budget amount']")
    budget_input.clear()
    budget_input.send_keys("4000")

    # 7 Skip budget end date (do nothing)

    # 8 Click Update Department
    update_btn = driver.find_element(By.XPATH, "//p[contains(text(),'Update department')]/ancestor::button")
    driver.execute_script("arguments[0].scrollIntoView(true);", update_btn)
    update_btn.click()
    time.sleep(2)

    # 9 Confirm success modal
    close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Close')]")))
    close_btn.click()
    print(" Department updated successfully.")
