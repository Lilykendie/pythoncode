import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("login")
def test_view_procurement_history(browser):

    wait = WebDriverWait(browser, 15)

    # 1. Click Procurements
    procurements_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Procurements')]"))
    )
    procurements_menu.click()

    # 2. Click Approvals
    approvals_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Approvals')]"))
    )
    approvals_menu.click()

    # 3. Click View History button
    view_history_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'View History')]"))
    )
    view_history_btn.click()

    # 4. Assert Approvals History title is visible
    history_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Approvals History')]"))
    )
    assert history_title.is_displayed(), "Approvals History page did not load"

    # 5. Wait for table rows to load
    first_view_button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//p[contains(@class, 'cursor-pointer') and contains(text(),'View')])[1]"
        ))
    )

    # 6. Click the first View button in table
    first_view_button.click()

    # 7. Validate that a details modal/page opened
    # (assuming a title like 'Purchase Requisition Details' appears)
    details_header = wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//h2[contains(text(), 'Requisition') or contains(text(), 'Details') or contains(text(), 'History')]"
        ))
    )

    assert details_header.is_displayed(), "PR Details view did not open"

    print("Procurement View History test passed successfully!")
