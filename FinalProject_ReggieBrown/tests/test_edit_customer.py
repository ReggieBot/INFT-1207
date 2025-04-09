# Reggie Brown
# reggie.brown@dcmail.ca
# INFT 1207 - Final Project 
# Prof. Patel
# Desciption: This file contains 20 test cases for the "edit customer" 
# functionality of the guru99 bank application. Test cases were written with unittest & selenium
# Github: https://github.com/ReggieBot/INFT-1207/tree/main/FinalProject_ReggieBrown

# REFERENCES: 
# https://www.selenium.dev/documentation/webdriver/elements/interactions/      .clear()
# https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-element-exception noSuchElementException
# https://www.browserstack.com/guide/alerts-and-popups-in-selenium
https://www.browserstack.com/guide/noalertpresentexception-in-selenium

# This test file assumes that a customer accont has already been created.
# Account created by me - Customer ID = 43593

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class TestEditCustomer(unittest.TestCase):

    # 20 test cases for the "edit customer" functionality

    @classmethod
    def setUpClass(cls) -> None:
        # set up webdriver
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()

        # nav to site
        cls.browser.get("http://demo.guru99.com/V4/")
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

    # various methods for use in test cases

    # cick on 'edit customer' link
    def go_edit_customer(self):
        self.browser.find_element(By.LINK_TEXT, "Edit Customer").click()
        sleep(1)

    # Enter customer id + submit
    def submit_cust_id(self, customer_id):
        self.browser.find_element(By.NAME, "cusid").send_keys(customer_id)
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

    def capture_alert
if __name__ == '__main__':
    unittest.main()
    