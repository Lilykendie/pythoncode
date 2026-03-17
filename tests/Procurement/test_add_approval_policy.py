from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# -----------------------------------------
# CONFIG
# -----------------------------------------
URL = "https://staging.useklak.com/login"
EMAIL = "akinyililian993@gmail.com"
PASSWORD = "Company22_"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# -----------------------------------------
# LOGIN
# -----------------------------------------
driver.get(URL)

wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(EMAIL)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# -----------------------------------------
# NAVIGATE: Company → Approval Policies → Procurement
# -----------------------------------------
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Company')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Approval Policies')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/procurement')]"))).click()

# -----------------------------------------
# CLICK: Add Approval Policy
# -----------------------------------------
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'Add') or contains(text(),'New')]"))
).click()

# -----------------------------------------
# FILL FORM
# -----------------------------------------

# Policy Name
policy_name = wait.until(EC.presence_of_element_located((By.NAME, "name")))
policy_name.clear()
policy_name.send_keys("Final say approval")

# Department (react-select-5-input)
dept_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-5-input")))
dept_input.click()
dept_input.send_keys("IT Department")
time.sleep(1)
dept_input.send_keys(Keys.ENTER)

# Toggle "Show Amount"
toggle_btn = wait.until(EC.element_to_be_clickable((By.ID, "show-amount")))
toggle_btn.click()

# Lower amount
lower_amount = wait.until(EC.presence_of_element_located((By.NAME, "lowerRangeAmount")))
lower_amount.clear()
lower_amount.send_keys("500")

# Upper amount
upper_amount = wait.until(EC.presence_of_element_located((By.NAME, "upperRangeAmount")))
upper_amount.clear()
upper_amount.send_keys("1000000")

# User select (react-select-6-input)
user_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-6-input")))
user_input.click()
user_input.send_keys("Lily Akinyi")
time.sleep(1)
user_input.send_keys(Keys.ENTER)

# -----------------------------------------
# SAVE
# -----------------------------------------
save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
save_btn.click()

# Wait for success popup
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//p[contains(text(),'Procurement approval policy created successfully')]")
))

print(" Procurement Approval Policy created!")

time.sleep(2)
driver.quit()







