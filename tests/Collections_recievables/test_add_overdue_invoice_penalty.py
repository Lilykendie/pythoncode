import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddOverduePenalty:

    def navigate_to_penalties(self, browser):
        wait = WebDriverWait(browser, 30)

        # Open Collections / Receivables menu
        menu = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Collections') or contains(.,'Receivables')]"))
        )
        browser.execute_script("arguments[0].click();", menu)

        # Click Reminders
        reminders = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Reminders']")))
        browser.execute_script("arguments[0].click();", reminders)

        # Click the Overdue Invoice Penalties tab (explicit)
        penalties_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Overdue Invoice Penalties')]"))
        )
        browser.execute_script("arguments[0].click();", penalties_tab)

        print(" Navigated to Reminders → Overdue Invoice Penalties")

    def select_react_dropdown_after(self, browser, anchor_name, option_text, timeout=20):
        """
        Finds the first react-select input that appears AFTER the field with name `anchor_name`,
        clicks it, types option_text to filter, then selects the visible option that contains option_text.
        This is robust to several react-select IDs.
        """
        wait = WebDriverWait(browser, timeout)

        # 1) find the anchor input (e.g. name="title") and then the first react-select input after it
        anchor = wait.until(EC.presence_of_element_located((By.NAME, anchor_name)))

        # react-select container inputs are inside divs with class css-19bb58m (observed) — locate the first that follows the anchor
        dropdown_input = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//following::div[contains(@class,'css-19bb58m')][1]//input")
            )
        ) if False else wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@name='{}']/following::div[contains(@class,'css-19bb58m')][1]//input".format(anchor_name))
            )
        )

        # Click into the input to activate the react dropdown
        browser.execute_script("arguments[0].click();", dropdown_input)
        time.sleep(0.2)

        # Type the option text to filter (if the widget supports typing)
        dropdown_input.send_keys(option_text)
        time.sleep(0.8)

        # Select the visible option (role=option is typical for react-select lists)
        # Try to find option by text
        option = None
        try:
            option = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@role,'option') and contains(normalize-space(.), '{option_text}')]")
            ))
        except Exception:
            # fallback: try clickable div that contains the option_text anywhere
            option = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(normalize-space(.), '{option_text}') and not(contains(@class,'css-19bb58m'))]")
            ))

        browser.execute_script("arguments[0].click();", option)
        print(f" Selected react option: {option_text}")

    @pytest.mark.usefixtures("login")
    def test_add_overdue_penalty(self, login):
        browser = login
        wait = WebDriverWait(browser, 30)

        # Navigate to Overdue Invoice Penalties
        self.navigate_to_penalties(browser)

        # Click Add Reminder (button text is "Add Reminder" in UI)
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add Reminder')]")))
        browser.execute_script("arguments[0].click();", add_btn)
        print(" Opened Add Reminder (penalty) modal")

        # Fill Title (penalty name)
        title = wait.until(EC.element_to_be_clickable((By.NAME, "title")))
        title.clear()
        title.send_keys("Due date penalty")
        print(" Filled Title")

        # Select penalty-type dropdown that appears after the title input.
        # Example option_text: "Daily" or "Percentage" — change to the actual option in your app.
        # If the dropdown options are different, pass the correct visible text.
        self.select_react_dropdown_after(browser, anchor_name="title", option_text="Daily")

        # Fill the amount/percentage field (name observed: conditions.0.amount)
        amount = wait.until(EC.presence_of_element_located((By.NAME, "conditions.0.amount")))
        amount.clear()
        amount.send_keys("5")   # e.g., 5%
        print(" Filled penalty amount")

        # Save (button text "Save Template" observed in markup)
        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Save Template') or contains(.,'Save')]")))
        browser.execute_script("arguments[0].click();", save_btn)
        print(" Clicked Save")

        # Verify success message shown (match text that appears in UI)
        success = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(.,'Penalty created successfully') or contains(.,'created successfully')]")))
        assert success is not None and success.is_displayed()
        print(" Penalty created successfully")






