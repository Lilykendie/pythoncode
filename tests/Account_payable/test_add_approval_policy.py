from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# -------------------------------------------------------
# CONFIG
# -------------------------------------------------------
URL = "https://staging.useklak.com/login"
EMAIL = "akinyililian993@gmail.com"
PASSWORD = "Company22_"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# -------------------------------------------------------
# LOGIN
# -------------------------------------------------------
driver.get(URL)

wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(EMAIL)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# -------------------------------------------------------
# NAVIGATE → Company → Approval Policies → Accounts Payable
# -------------------------------------------------------
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Company')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Approval Policies')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/accounts-payable') and .//p[text()='Accounts Payable']]"))).click()

# -------------------------------------------------------
# CLICK: Add Approval Policy Button
# -------------------------------------------------------
time.sleep(2)  # wait for modal/form to appear
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add') or contains(text(),'New')]"))).click()

# -------------------------------------------------------
# FILL THE FORM: Name & Amounts
# -------------------------------------------------------
policy_name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
policy_name_input.clear()
policy_name_input.send_keys("Final say approval")

lower_amount = driver.find_element(By.NAME, "lowerRangeAmount")
lower_amount.clear()
lower_amount.send_keys("1000")

upper_amount = driver.find_element(By.NAME, "upperRangeAmount")
upper_amount.clear()
upper_amount.send_keys("50000")

# -------------------------------------------------------
# SELECT DEPARTMENT: Accounts
# -------------------------------------------------------
department_input = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//div[contains(., 'Choose Department')]//input[contains(@id, 'react-select')]")
))
department_input.click()
department_input.send_keys("Accounts")
time.sleep(1)
department_input.send_keys(Keys.ENTER)

# -------------------------------------------------------
# TOGGLE BILL CREATION
# -------------------------------------------------------
bill_creation_toggle = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[text()='Bill Creation']")
))
bill_creation_toggle.click()

# -------------------------------------------------------
# SELECT USER: Lily Akinyi
# -------------------------------------------------------
user_input = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//div[contains(@class,'css-19bb58m')]//input[contains(@id,'react-select')]")
))
user_input.click()
user_input.send_keys("Lily Akinyi")
time.sleep(1)
user_input.send_keys(Keys.ENTER)

# -------------------------------------------------------
# CLICK SAVE
# -------------------------------------------------------
save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
save_btn.click()

time.sleep(3)
driver.quit()


















