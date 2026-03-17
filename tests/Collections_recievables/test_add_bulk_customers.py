import time
import csv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBulkAddCustomers:

    def navigate_to_customers(self, browser):
        wait = WebDriverWait(browser, 40)

        # Open Collections
        collections = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Collections')]"))
        )
        browser.execute_script("arguments[0].click();", collections)

        # Open Customers
        customers = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Customers')]"))
        )
        browser.execute_script("arguments[0].click();", customers)

        print(" Opened Customers Page")

    def create_sample_csv(self):
        """Creates a temporary CSV file for uploading."""
        file_path = os.path.join(os.getcwd(), "sample_customers.csv")

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # CSV header
            writer.writerow(["Customer Name", "Email", "Phone", "Company"])
            # Sample rows
            writer.writerow(["Test Customer 1", "test1@mail.com", "0712345678", "Company A"])
            writer.writerow(["Test Customer 2", "test2@mail.com", "0798765432", "Company B"])

        return file_path

    def test_bulk_add_customers(self, login):
        browser = login
        wait = WebDriverWait(browser, 40)

        # Navigate to Customers page
        self.navigate_to_customers(browser)

        # Click Add a Customer
        add_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add a Customer')]"))
        )
        browser.execute_script("arguments[0].click();", add_btn)
        print(" Clicked Add a Customer")

        time.sleep(1)

        # Create sample CSV
        file_path = self.create_sample_csv()
        print(f" Sample CSV created → {file_path}")

        # Upload file using hidden input
        file_input = wait.until(
            EC.presence_of_element_located((By.ID, "fileInput"))
        )
        file_input.send_keys(file_path)
        print(" File uploaded")

        time.sleep(1)

        # Click Add Customers button
        add_customers_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add Customers')]"))
        )
        browser.execute_script("arguments[0].click();", add_customers_btn)
        print(" Clicked Add Customers button")

        # Verify success modal
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(text(),'File has been added.')]"))
        )

        print(" Bulk Customers Added Successfully!")

        # Cleanup temporary file
        os.remove(file_path)


