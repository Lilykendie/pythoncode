
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# ---------------- JS CLICK FUNCTION ---------------- #
def js_click_date(driver, date_value):
    """
    Clicks a date inside the calendar using JS.
    Example date_value: '2025-11-04'
    """
    driver.execute_script(
        """
        const btn = document.querySelector("button[data-date='%s']");
        if(btn){ btn.click(); }
        """ % date_value
    )

# ---------------- LOGIN FIXTURE ---------------- #
@pytest.fixture
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    driver.get("https://staging.useklak.com/")

    # Login
    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email.send_keys("akinyililian993@gmail.com")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("Company22_")

    login_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    login_btn.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Reconciliation')]")))
    yield driver
    driver.quit()

# ---------------- TEST RECONCILIATION ---------------- #
def test_reconciliation(login):
    driver = login
    wait = WebDriverWait(driver, 20)

    # Click Reconciliation menu
    driver.find_element(By.XPATH, "//p[contains(text(),'Reconciliation')]").click()

    # Click Bank Reconciliation
    bank_recon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Bank Reconciliation']"))
    )
    bank_recon.click()

    # Wait for page elements
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Start Reconciliation']")))

    # ---------------- SELECT START DATE ---------------- #
    start_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Select Start Date']")))
    start_label.click()
    time.sleep(2)
    js_click_date(driver, "2025-11-04")   # Force set date via JS

    # ---------------- SELECT END DATE ---------------- #
    end_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Select End Date']")))
    end_label.click()
    time.sleep(2)
    js_click_date(driver, "2025-11-05")   # Force set date via JS


# Ledger Selection
    ledger_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Ledger']/ancestor::div[contains(@class,'rounded-xl')]//div[contains(@class,'p-4')][2]")))
    ledger_btn.click()

    ledger_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'css-19bb58m')]//input")))
    ledger_input.send_keys("Billable Expense Income")
    ledger_input.send_keys(Keys.ENTER)


    add_account_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//h3[text()='Bank Account']/ancestor::div[contains(@class,'rounded-xl')]//p[text()='Add Corresponding Account']")
    )
)
    add_account_btn.click()
    account_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'css-19bb58m')]//input"))
)
    account_input.send_keys("3880117122 - Ecobank Nigeria")
    account_input.send_keys(Keys.ENTER)

# Start Reconciliation
    start_recon_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Start Reconciliation']"))
)
    start_recon_btn.click()

    # ---------------- HANDLE CONTINUE BUTTONS ---------------- #
    continue_btn = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Continue']"))
    )
    continue_btn.click()
    time.sleep(1)  # short wait for DOM update

    continue_anyway_btn = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and text()='Continue Anyway']"))
    )
    continue_anyway_btn.click()
    
 # ---------------- EXTRACT BALANCES ---------------- #
    time.sleep(2)  # wait for page to render balances

    # Opening and Closing Balances
    bank_opening = driver.find_element(By.XPATH, "//p[contains(text(),'Opening Balance')]/following-sibling::p").text
    ledger_opening = driver.find_element(By.XPATH, "//p[contains(text(),'Opening Balance')]/following-sibling::p[2]").text
    bank_closing = driver.find_element(By.XPATH, "//p[contains(text(),'Closing Balance')]/following-sibling::p").text
    ledger_closing = driver.find_element(By.XPATH, "//p[contains(text(),'Closing Balance')]/following-sibling::p[2]").text

    print("Bank Opening Balance:", bank_opening)
    print("Ledger Opening Balance:", ledger_opening)
    print("Bank Closing Balance:", bank_closing)
    print("Ledger Closing Balance:", ledger_closing)


















