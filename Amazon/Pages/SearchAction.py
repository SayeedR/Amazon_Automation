import time

from selenium.webdriver.common.by import By



class SearchAction:

    def __init__(self, driver):

        self.driver = driver

    # search box locator clean and send value
    def send_text_search_box(self, txt):
        self.driver.find_element(By.ID, 'twotabsearchtextbox').clear()
        self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(txt)

        # to confirm print e message
        print("Enter 'games' text Pass successfully")
        time.sleep(10)

    # click action on btn
    def search_action(self):
        self.driver.find_element(By.ID, 'nav-search-submit-button').click()
        print("Search Action Perform successfully")
        time.sleep(10)
