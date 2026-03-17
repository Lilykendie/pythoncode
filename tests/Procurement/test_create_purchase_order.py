from asyncio import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_create_purchase_order(login):
    browser = login
    wait = WebDriverWait(browser, 20)

    # Step 1: Navigate to Procurement -> Purchase Orders
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Procurements')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Purchase Orders')]"))).click()

    # Step 2: Click "Create a Purchase Order"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create a Purchase Order')]"))).click()


    # Step 4: Select supplier "Lerian Enterprise"
    dept_input = wait.until(
    EC.element_to_be_clickable((By.ID, "react-select-2-input"))
    )
    dept_input.send_keys("Lerian Enterprise")
 
    # Wait a moment for the dropdown to render
    time.sleep(0.5)

    # Press Enter to select the first matching option
    dept_input.send_keys("\n")


    # Wait until the Quote dropdown input is clickable
    quote_input = wait.until(
    EC.element_to_be_clickable((By.ID, "react-select-3-input"))
  )

    # Type the quote name
    quote_input.send_keys("PRQ-202511-FFG-9HK")  # replace with actual quote

    # Wait a short moment for the dropdown to render
    time.sleep(0.5)

    # Press Enter to select the first matching option
    quote_input.send_keys("\n")
    # wait for any loader to disappear
    wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, ".opacity-50, .pointer-events-none")))
    continue_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]"))
)
    browser.execute_script("arguments[0].click();", continue_btn)

    # WAIT FOR PAGE TO LOAD
    time.sleep(2)

    # SCROLL TO BOTTOM (Submit button is at the bottom)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    # CLICK SUBMIT FOR APPROVAL
    submit_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit For Approval')]"))
    )
    submit_btn.click()



    

