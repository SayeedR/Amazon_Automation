import unittest
import time
from selenium import webdriver

from Amazon.Pages.DropDown import DropDown
from Amazon.Pages.SearchAction import SearchAction


class AmazonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.amazon.com/")

    def test_amazon(self):
        driver = self.driver


        drop_down_scroll = DropDown(driver)
        time.sleep(5)
        drop_down_scroll.select_dropdown_option("Software")

        print("From dropdown select 'Software' Successfully")

        search_action = SearchAction(driver)
        search_action.send_text_search_box("games")
        search_action.search_action()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
