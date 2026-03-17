import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pay_bill(login):
    driver = login
    wait = WebDriverWait(driver, 20)

    # ---------------- Click Accounts Payable ---------------- #
    accounts_payable = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Accounts Payable')]"))
    )
    accounts_payable.click()


    # ---------------- Navigate to Approvals ---------------- #
    approvals_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Approvals']"))
    )
    approvals_menu.click()
       # ---------------- Click Bill Payment tab ---------------- #
    bill_payment_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Bill Payment']"))
    )
    bill_payment_tab.click()


    # ---------------- Click View ---------------- #
    view_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(@class,'text-purple-800') and text()='View']"))
    )
    view_button.click()

    # ---------------- Wait for overlay to disappear ---------------- #
    try:
        wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'bg-black bg-opacity-70')]")
            )
        )
    except:
        pass  # overlay may not appear, continue

    
    # ---------------- Click Approve Bill (Upper-right) ---------------- #
    approve_bill_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Approve Bill']"))
    )
    # Use JS click in case overlay still blocks
    driver.execute_script("arguments[0].click();", approve_bill_button)

    # ---------------- Enter Comments ---------------- #
    comments_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter comments here']"))
    )
    comments_box.clear()
    comments_box.send_keys("Approved for testing automation.")

    # ---------------- Click Approve ---------------- #
    approve_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Approve']"))
    )
    driver.execute_script("arguments[0].click();", approve_button)

    # ---------------- Wait for success message ---------------- #
    success_message = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[text()='Invoice Submitted for Approval']")
        )
    )
    assert success_message.is_displayed()
    print(" Bill approved successfully!")


   


  

  
