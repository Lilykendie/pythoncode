import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("login")
def test_approve_purchase_requisition(browser):

    wait = WebDriverWait(browser, 15)

    # 1. Navigate to Procurements
    procurements_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Procurements')]"))
    )
    procurements_menu.click()

    # 2. Click Approvals
    approvals_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Approvals')]"))
    )
    approvals_menu.click()

    # 3. Select Purchase Requisition tab
    pr_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Purchase Requisition')]"))
    )
    pr_tab.click()

    # 4. Click the first View link in the PR table
    first_view = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//p[contains(@class,'cursor-pointer') and contains(text(),'View')])[1]"
        ))
    )
    first_view.click()

    # 5. Click Approve Purchase Requisition button
    approve_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Approve Purchase Requisition')]"))
    )
    approve_btn.click()
    # Step 4: Enter comments in the textarea
    comments_box = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//textarea[@placeholder='Enter comments here']")
    ))
    comments_box.clear()
    comments_box.send_keys("nil")  # You can change this to any comment

# Step 5: Click the secondary "Approve" button
    final_approve_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[text()='Approve']")
    ))
    final_approve_button.click()

# Step 6: Handle post-approval options
# Example: Click "Send Quotation to Suppliers"
    send_quotation_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[text()='Send Quotation to Suppliers']")
   ))
    send_quotation_button.click()

# Optional: Wait a bit and close browser
    time.sleep(3)
    browser.quit()

    # 6. Wait for success message or state change
    success_message = wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//*[contains(text(),'successfully') or contains(text(),'approved') or contains(text(),'Success')]"
        ))
    )

    assert success_message.is_displayed(), "Approval success message not displayed"

    print("Purchase Requisition approved successfully!")
