# Reggie Brown
# reggie.brown@dcmail.ca
# INFT 1207 - Final Project 
# Prof. Patel
# Desciption: This file contains 20 test cases for the "edit customer" 
# functionality of the guru99 bank application. Test cases were written with unittest & selenium
# Github: https://github.com/ReggieBot/INFT-1207/tree/main/FinalProject_ReggieBrown

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestEditCustomer(unittest.TestCase):

    # 20 test cases for the "edit customer" functionality

    @classmethod
    def setUpClass(cls) -> None:
        # set up webdriver
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()

        # nav to site
        cls.browser.get("http://demo.guru99.com/v4/")
        sleep(1.5)

        # log in (manager credentials)
        cls.browser.find_element(By.NAME, "uid").send_keys("mngr619261")
        cls.browser.find_element(By.NAME, "password").send_keys("anugagy")
        cls.browser.find_element(By.NAME, "btnLogin").click()
        sleep(1.5)

        print("Manager login successful")

        def tearDownClass(cls) -> None:
            # close browser
            sleep(2)
            cls.browser.quit()


if __name__ == '__main__':
    unittest.main()