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
# https://www.browserstack.com/guide/noalertpresentexception-in-selenium

# This test file assumes that a customer accont has already been created.
# Account created by me - Customer ID = 43593

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException

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

    # captures alert message and accepts it. Returns alert text (if present)
    def capture_alert(self):
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            return None

    # Test 1: Customer ID empty
    def test1_emptyID(self):
        print("Test1: Verify ID cannot be empty")

        self.go_edit_customer()
        self.submit_cust_id("")
        
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        message = self.capture_alert()
        self.assertEqual(message, "Please fill all fields")
        print("Test 1 passed")

    # Test 2: ID must be numeric
    def test2_numericID(self):
        print("Test 2: Verify ID cannot contain letters")
        
        self.go_edit_customer()
        self.browser.find_element(By.NAME, "cusid").send_keys("abc")
        sleep(1)
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
        self.assertTrue(cant_contain.is_displayed())
        print("Warning displayed")

        # Check if alert is present
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        alert = self.capture_alert()
        self.assertIsNotNone(alert, "Exepcted Alert")
        print("Test 2 passed")

    # Test 3: Inserting special characters in Customer ID field
    def test3_specialChar(self):
        print("Test 3: Verify ID cannot contain special characters")

        self.go_edit_customer()
        self.browser.find_element(By.NAME, "cusid").send_keys("@*$&%$@*")
        sleep(1)
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message14")

        self.assertTrue(cant_contain.is_displayed())
        print("Warning displayed")
        
        # Check if alert is present
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        alert = self.capture_alert()
        self.assertIsNotNone(alert, "Expected alert")
        print("Test 2 passed")

    def test4_validID(self):
        print("Test 4: Verify that a valid ID is accepted")

        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Check to see if name field is displayed
        # if not, then ID is invalid

        name_field = self.browser.find_element(By.NAME, "name")
        self.assertTrue(name_field.is_displayed())
        print("Name field displayed")

        print("Test 4 passed")

    def test4_empty_address(self):
        print("Test 5: Verify address field cannot be empty")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # clear address field
        address_field = self.browser.find_element(By.NAME, "addr")
        address_field.clear()
        sleep(.5)

        # press tab to trigger warning message
        address_field.send_keys(Keys.TAB)
        sleep(1)

        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message3")

        self.assertTrue(cant_contain.is_displayed())
        print("Warning displayed")

        # Check if address field is empty (saved empty address to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.browser.get("https://demo.guru99.com/V4/")
        self.browser.find_element(By.NAME, "uid").send_keys("mngr619261")
        self.browser.find_element(By.NAME, "password").send_keys("anugagy")
        self.browser.find_element(By.NAME, "btnLogin").click()
        sleep(1)

        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        address_field = self.browser.find_element(By.NAME, "addr")
        address_field_value = address_field.get_attribute("value")
        self.assertEqual(address_field_value, "", "BUG Address field is empty. Invalid address was saved to DB")

        print("Test 5 BUG FOUND: Warning message displayed, but empty address was still saved")


        
if __name__ == '__main__':
    unittest.main()
    