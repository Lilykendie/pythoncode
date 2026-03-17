import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_view_reconciliation_history(login):
    driver = login
    wait = WebDriverWait(driver, 20)

    # -------------------- Click RECONCILIATION menu -------------------- #
    reconciliation_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Reconciliation')]"))
    )
    driver.execute_script("arguments[0].click();", reconciliation_menu)
    print("➡ Clicked Reconciliation menu.")

    # -------------------- Click BANK RECONCILIATION -------------------- #
    bank_recon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Bank Reconciliation')]"))
    )
    driver.execute_script("arguments[0].click();", bank_recon)
    print("➡ Opened Bank Reconciliation.")

    # -------------------- Click GO TO RECONCILIATION HISTORY -------------------- #
    history_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(),'Go to reconciliation history')]")
        )
    )
    driver.execute_script("arguments[0].click();", history_btn)
    print("➡ Navigated to Reconciliation History.")

    # -------------------- Validate HISTORY PAGE -------------------- #
    header = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Reconciliation History')]")
        )
    )

    assert header.is_displayed(), " Reconciliation History page did NOT open!"
    print(" Reconciliation History header is visible.")

    # -------------------- Validate TABLE EXISTS -------------------- #
    table_rows = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//table/tbody/tr")
        )
    )

    assert len(table_rows) > 0, " No reconciliation history records found!"
    print(f" Table loaded successfully with {len(table_rows)} rows.")
