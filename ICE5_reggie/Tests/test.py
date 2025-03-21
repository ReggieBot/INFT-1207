# Reggie Brown
# INFT 1207
# Prof Patel
# Desc: Created a new user on a test site with predefined credentials and validates successful auth using python/selenium

from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MercuryToursTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        # opens MercuryTours site in the browser by URL
        cls.browser.get("https://demo.guru99.com/test/newtours/")
        sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        # Tear down method for closing script after exec.

    def test1_Register_User(self):
        # First test case: Register user with username "Reggie" and password "durhamcollege2025"
        # First login using "tutorial" as username/password