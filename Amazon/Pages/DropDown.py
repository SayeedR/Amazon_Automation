import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DropDown:

    def __init__(self, driver):
        self.driver = driver

    def select_dropdown_option(self, visible_text):
        # Wait for the dropdown to be present
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.presence_of_element_located((By.ID, 'searchDropdownBox')))
        dropdown.click()

        # Scroll to the dropdown and click on it (if needed)
        ActionChains(self.driver).move_to_element(dropdown).perform()

        # Create a Select object for the dropdown
        select = Select(dropdown)

        # Select "Software" from the dropdown
        select.select_by_visible_text(visible_text)

        time.sleep(5)
