import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("login")
def test_add_supplier_complete(login):
    driver = login
    wait = WebDriverWait(driver, 30)

    # 1️⃣ Navigate to Suppliers page
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='Suppliers' or contains(text(),'Suppliers')]")
    )).click()

    # 2️⃣ Click "Add a Supplier"
    add_supplier_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Add a Supplier')]")
    ))
    add_supplier_btn.click()
    time.sleep(1)  # wait for React to render

    # ---------------------------
    # 3 Fill mandatory Supplier details
    # ---------------------------
    supplier_name = wait.until(EC.visibility_of_element_located(
        (By.NAME, "supplierCompanyName")
    ))
    supplier_name.clear()
    supplier_name.send_keys("EM Collection")

    supplier_email = driver.find_element(By.NAME, "email")
    supplier_email.clear()
    supplier_email.send_keys("lilianakinyi@kabarak.ac.ke")
    supplier_phone = driver.find_element(By.NAME, "phoneNumber")
    supplier_phone.clear()
    supplier_phone.send_keys("+0876543210")
    #---------------------------
    
    # 4 Continue through optional pages
    # ---------------------------
    while True:
        try:
            continue_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Continue')]")
            ))
            continue_btn.click()
            time.sleep(1)  # wait for next page to render
        except:
            # If no more continue buttons, break loop
            break

    # ---------------------------
    # 5 Fill Representative details
    # ---------------------------
    rep_first_name = wait.until(EC.visibility_of_element_located(
        (By.NAME, "repFirstName")
    ))
    rep_first_name.clear()
    rep_first_name.send_keys("Lilian")

    rep_last_name = driver.find_element(By.NAME, "repLastName")
    rep_last_name.clear()
    rep_last_name.send_keys("Akinyi")

    rep_email = driver.find_element(By.NAME, "repEmail")
    rep_email.clear()
    rep_email.send_keys("Paulnokwo12@gmail.com")

    # ---------------------------
    # 6 Submit the supplier
    # ---------------------------
    add_supplier_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(),'Add Supplier')]")
    ))
    add_supplier_btn.click()

    # ---------------------------
    # 7 Wait for success message
    # ---------------------------
    success_msg = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(text(),'Supplier created successfully')]")
    ))
    assert "Supplier created successfully" in success_msg.text


