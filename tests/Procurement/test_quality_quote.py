from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_qualify_quote(login):
    browser = login
    wait = WebDriverWait(browser, 25)

    # STEP 1 → Navigate to Purchase Requisitions
    procurement_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Procurements')]"))
    )
    procurement_tab.click()

    purchase_req_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Purchase Requisitions')]"))
    )
    purchase_req_tab.click()

    # STEP 2 → Open dropdown menu on first Purchase Requisition
    chevron = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//td[last()]//div[@aria-haspopup='menu']"))
    )
    chevron.click()

    # STEP 3 → Click "View" inside the dropdown
    view_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and normalize-space()='View']"))
    )
    view_option.click()

    # STEP 4 → Wait for Suppliers Quotes section
    supplier_section = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Suppliers Quotes')]/following-sibling::div"))
    )

    # STEP 5 → Click "View" for the first supplier
    first_supplier_view = supplier_section.find_element(By.XPATH, ".//button[normalize-space()='View']")
    first_supplier_view.click()

    # Wait for the dialog to appear
    quote_dialog = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='dialog' and contains(@class,'fixed')]"))
  )

    # Click 'Qualify Quote' inside the dialog
    qualify_button = quote_dialog.find_element(By.XPATH, ".//button[normalize-space()='Qualify Quote']")
    browser.execute_script("arguments[0].click();", qualify_button)

    print(" 'Qualify Quote' clicked successfully")
    
   



