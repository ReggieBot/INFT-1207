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

    @classmethod
    def tearDownClass(cls) -> None:
        # close browser
        sleep(2)
        cls.browser.quit()

    # various methods for use in test cases

    # log in as manager
    def manager_login(self):
        self.browser.get("https://demo.guru99.com/V4/")
        self.browser.find_element(By.NAME, "uid").send_keys("mngr619261")
        self.browser.find_element(By.NAME, "password").send_keys("anugagy")
        self.browser.find_element(By.NAME, "btnLogin").click()
        sleep(1)

    # click on 'edit customer' link
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
    def test01_emptyID(self):
        print("Test1: Verify ID cannot be empty")

        self.go_edit_customer()
        self.submit_cust_id("")

        # tab to trigger warning message
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)
        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Customer ID is required")
            print("Test 1 warning displayed")
        except NoSuchElementException:
            print("Test 1 warning not displayed")
        
        # Check if alert is present
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        message = self.capture_alert()
        self.assertEqual(message, "Please fill all fields")
        print("Test 1 passed")

    # Test 2: ID must be numeric
    def test02_numericID(self):
        print("Test 2: Verify ID cannot contain letters")
        
        self.go_edit_customer()
        self.browser.find_element(By.NAME, "cusid").send_keys("1234Acc")
        sleep(.5)
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message14")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Characters are not allowed")
            print("Test 2.1 warning displayed")
        except NoSuchElementException:
            print("Test 2.1 warning not displayed")
 
        self.go_edit_customer()
        self.browser.find_element(By.NAME, "cusid").send_keys("Acc1234")
        sleep(.5)
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message14")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Characters are not allowed")
            print("Test 2.2 warning displayed")
        except NoSuchElementException:
            print("Test 2.2 warning not displayed")

        # Check if alert is present
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(.5)
        alert = self.capture_alert()
        self.assertIsNotNone(alert, "Exepcted Alert")
        print("Test 2 passed")

    # Test 3: Inserting special characters in Customer ID field
    def test03_specialChar(self):
        print("Test 3: Verify ID cannot contain special characters")

        self.go_edit_customer()
        self.browser.find_element(By.NAME, "cusid").send_keys("123!@#")
        sleep(1)
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message14")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 3.1 warning displayed")
        except NoSuchElementException:
            print("Test 3.1 warning not displayed")

        self.go_edit_customer()
        self.browser.find_element(By.NAME, "cusid").send_keys("!@#")
        sleep(1)
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message14")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 3.2 warning displayed")
        except NoSuchElementException:
            print("Test 3.2 warning not displayed")
        
        
        # Check if alert is present
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        alert = self.capture_alert()
        self.assertIsNotNone(alert, "Expected alert")
        print("Test 3 passed")

    # Test 4: Valid ID
    def test04_validID(self):
        print("Test 4: Verify that a valid ID is accepted")

        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Check to see if name field is displayed
        # if not, then ID is invalid, as we are not redirected

        name_field = self.browser.find_element(By.NAME, "name")
        self.assertTrue(name_field.is_displayed())
        print("Name field displayed")

        print("Test 4 passed")

    # Test 5: Empty address
    def test05_empty_address(self):
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

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Address Field must be blank")
            print("Test 5 warning displayed")
        except NoSuchElementException:
            print("Test 5 warning not displayed")

        # Check if address field is empty (saved empty address to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        address_field = self.browser.find_element(By.NAME, "addr")
        address_field_value = address_field.get_attribute("value")
        
        if (address_field_value == ""):
            print("BUG: Empty address field was saved to the database!")
        self.assertEqual(address_field_value, "", "BUG Address field is empty. Invalid address was saved to DB")


    # Test 6: Empty city
    def test06_empty_city(self):
        print("Test 6: Verify city field cannot be empty")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # clear city field
        city_field = self.browser.find_element(By.NAME, "city")
        city_field.clear()
        sleep(.5)

        # press tab to trigger warning message
        city_field.send_keys(Keys.TAB)
        sleep(1)

        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message4")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "City Field must not be blank")
            print("Test 6 warning displayed")
        except NoSuchElementException:
            print("Test 6 warning not displayed")
        # check if city field is empty (saved empty city to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        city_field = self.browser.find_element(By.NAME, "city")
        city_field_value = city_field.get_attribute("value")

        if (city_field_value == ""):
            print("BUG: Empty city field was saved to the database!")
        self.assertEqual(city_field_value, "", "BUG City field is empty. Invalid city was saved to DB")

    # Test 7: City numeric
    # NOTE: Test 7 test suite states that warning message must = "Numbers are allowed"
    def test07_city_numeric(self):
        print("Test 7: Verify city field cannot contain numbers")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # enter numbers in city field
        city_field = self.browser.find_element(By.NAME, "city")
        city_field.clear()
        city_field.send_keys("1234")
        sleep(.5)

        # press tab to trigger warning message
        city_field.send_keys(Keys.TAB)
        sleep(1)

        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message4")
        
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Numbers are allowed")
            print("Test 7.1 warning displayed")
        except NoSuchElementException:
            print("Test 7.1 warning not displayed")

        city_field.clear()
        city_field.send_keys("City123")
        sleep(.5)

        # press tab to trigger warning message
        city_field.send_keys(Keys.TAB)
        sleep(1)

        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message4")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Numbers are allowed")
            print("Test 7.2 warning displayed")
        except NoSuchElementException:
            print("Test 7.2 warning not displayed")

        # check if city field is numeric (saved numeric city to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        city_field = self.browser.find_element(By.NAME, "city")
        city_field_value = city_field.get_attribute("value")
        
        if (city_field_value == "City123"):
            print("BUG: City field with numeric characters was saved to the database!")
        self.assertEqual(city_field_value, "City123", "BUG City field is numeric. Invalid city was saved to DB")

    # Test 8: City special characters
    def test08_city_special(self):
        print("Test 8: Verify city field cannot contain special characters")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # enter special characters in city field
        city_field = self.browser.find_element(By.NAME, "city")
        city_field.clear()
        city_field.send_keys("City!@#")
        sleep(.5)

        # press tab to trigger warning message
        city_field.send_keys(Keys.TAB)
        sleep(1)
        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message4")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 8.1 warning displayed")
        except NoSuchElementException:
            print("Test 8.1 warning not displayed")
        city_field.clear()
        city_field.send_keys("!@#")
        sleep(.5)
        # press tab to trigger warning message
        city_field.send_keys(Keys.TAB)
        sleep(1)
        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message4")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 8.2 warning displayed")
        except NoSuchElementException:
            print("Test 8.2 warning not displayed")
        # check if city field is special characters (saved special characters to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)
        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        city_field = self.browser.find_element(By.NAME, "city")
        city_field_value = city_field.get_attribute("value")
        
        if (city_field_value == "!@#"):
            print("BUG: City field with special characters was saved to the database!")
        self.assertEqual(city_field_value, "!@#", "BUG City field is special characters. Invalid city was saved to DB")

    # Test 9: Empty state
    # NOTE: Test 9 test suite states that warning message must = "State must be blank"
    def test09_empty_state(self):
        print("Test 9: Verify state field cannot be empty")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # clear state field
        state_field = self.browser.find_element(By.NAME, "state")
        state_field.clear()
        sleep(.5)

        # press tab to trigger warning message
        state_field.send_keys(Keys.TAB)
        sleep(1)

        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message5")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "State must be blank")
            print("Test 9 warning displayed")
        except NoSuchElementException:
            print("Test 9 warning not displayed")

        # check if state field is empty (saved empty state to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        state_field = self.browser.find_element(By.NAME, "state")
        state_field_value = state_field.get_attribute("value")
        
        if (state_field_value == ""):
            print("BUG: Empty state field was saved to the database!")
        self.assertEqual(state_field_value, "", "BUG State field is empty. Invalid state was saved to DB")

    # Test 10: State numeric
    def test10_state_numeric(self):
        print("Test 10: Verify state field cannot contain numbers")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        # enter numbers in state field
        state_field = self.browser.find_element(By.NAME, "state")
        state_field.clear()
        state_field.send_keys("1234")
        sleep(.5)
        # press tab to trigger warning message
        state_field.send_keys(Keys.TAB)
        sleep(1)
        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message5")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Numbers are not allowed")
            print("Test 10 warning displayed")
        except NoSuchElementException:
            print("Test 10 warning not displayed")

        state_field.clear()
        state_field.send_keys("State123")
        sleep(.5)
        # press tab to trigger warning message
        state_field.send_keys(Keys.TAB)
        sleep(1)
        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message5")
        self.assertTrue(cant_contain.is_displayed())
        self.assertEqual(cant_contain.text, "Numbers are not allowed")
        print("Warning displayed")

        # check if state field is numeric (saved numeric state to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        state_field = self.browser.find_element(By.NAME, "state")
        state_field_value = state_field.get_attribute("value")
        
        if (state_field_value == "State123"):
            print("BUG: State field with numeric characters was saved to the database!")
        self.assertEqual(state_field_value, "State123", "BUG State field is numeric. Invalid state was saved to DB")

    # Test 11: State special characters
    def test11_state_special(self):
        print("Test 11: Verify state field cannot contain special characters")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # enter special characters in state field
        state_field = self.browser.find_element(By.NAME, "state")
        state_field.clear()
        state_field.send_keys("State!@#")
        sleep(.5)
        # press tab to trigger warning message
        state_field.send_keys(Keys.TAB)
        sleep(1)
        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message5")
        self.assertTrue(cant_contain.is_displayed())
        self.assertEqual(cant_contain.text, "Special characters are not allowed")
        print("Warning displayed")

        state_field.clear()
        state_field.send_keys("!@#")
        sleep(.5)
        # press tab to trigger warning message
        state_field.send_keys(Keys.TAB)
        sleep(1)
        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message5")
        self.assertTrue(cant_contain.is_displayed())
        self.assertEqual(cant_contain.text, "Special characters are not allowed")
        print("Warning displayed")

        # check if state field is special characters (saved special characters to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)
        

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        state_field = self.browser.find_element(By.NAME, "state")
        state_field_value = state_field.get_attribute("value")
        
        if (state_field_value == "!@#"):
            print("BUG: State field with special characters was saved to the database!")
        self.assertEqual(state_field_value, "!@#", "BUG State field is special characters. Invalid state was saved to DB")

    # Test 12: PIN letters
    def test12_pin_letters(self):
        print("Test 12: Verify PIN cannot contain letters")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Enter only letters
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field.clear()
        pin_field.send_keys("abcd")
        sleep(.5)

        # press tab to trigger warning message
        pin_field.send_keys(Keys.TAB)
        sleep(1)

        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message6")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Characters are not allowed")
            print("Test 12.1 warning displayed")
        except NoSuchElementException:
            print("Test 12.1 warning not displayed")

        # Enter mix of letters and digits
        pin_field.clear()
        pin_field.send_keys("123ab4")
        sleep(.5)

        # press tab to trigger warning message
        pin_field.send_keys(Keys.TAB)
        sleep(1)

        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message6")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Characters are not allowed")
            print("Test 12.2 warning displayed")
        except NoSuchElementException:
            print("Test 12.2 warning not displayed")

        # Attempt to save changes
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field_value = pin_field.get_attribute("value")
        
        if (pin_field_value == "123ab4"):
            print("BUG: PIN field with letters was saved to the database!")
        self.assertEqual(pin_field_value, "123ab4", "BUG PIN with letters saved to DB")

    # Test 13: Empty PIN
    def test13_empty_pin(self):
        print("Test 13: Verify PIN field cannot be empty")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # clear PIN field
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field.clear()
        sleep(.5)

        # press tab to trigger warning message
        pin_field.send_keys(Keys.TAB)
        sleep(1)

        # check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message6")

        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "PIN Code must not be blank")
            print("Test 13 warning displayed")
        except NoSuchElementException:
            print("Test 13 warning not displayed")

        # Check if PIN field is empty (saved empty PIN to DB)
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field_value = pin_field.get_attribute("value")
        
        if pin_field_value == "":
            print("BUG DETECTED: Empty PIN field was saved to the database!")
        self.assertEqual(pin_field_value, "", "BUG PIN field is empty. Invalid PIN was saved to DB")

    # Test 14: PIN length
    def test14_pin_length(self):
        print("Test 14: Verify PIN must have 6 digits")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Test with more than 6 digits
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field.clear()
        pin_field.send_keys("1234567")
        sleep(.5)

        # press tab to trigger warning message
        pin_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed for more than 6 digits
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message6")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "PIN Code must have 6 Digits")
            print("Test 14.1 warning displayed")
        except NoSuchElementException:
            print("Test 14.1 warning not displayed")

        # Test with less than 6 digits
        pin_field.clear()
        pin_field.send_keys("12345")
        sleep(.5)

        # press tab to trigger warning message
        pin_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed for less than 6 digits
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message6")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "PIN Code must have 6 Digits")
            print("Test 14.2 warning displayed")
        except NoSuchElementException:
            print("Test 14.2 warning not displayed")

        # Submit with invalid PIN length
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        # Verify the change was attempted with invalid data
        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field_value = pin_field.get_attribute("value")
        
        if len(pin_field_value) != 6:
            print("BUG: PIN with invalid length was saved to the database!")
        self.assertEqual(pin_field_value, "12345", "BUG Invalid PIN length was saved to DB")

    # Test 15: PIN special characters
    def test15_pin_special(self):
        print("Test 15: Verify PIN cannot have special characters")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Enter special characters in PIN field
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field.clear()
        pin_field.send_keys("!@#")
        sleep(.5)

        # Press tab to trigger warning message
        pin_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message6")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 15.1 warning displayed")
        except NoSuchElementException:
            print("Test 15.1 warning not displayed")

        pin_field.clear()
        pin_field.send_keys("123!@#")
        sleep(.5)

        # Press tab to trigger warning message
        pin_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message6")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 15.2 warning displayed")
        except NoSuchElementException:
            print("Test 15.2 warning not displayed")

        # Check if PIN field with special characters was saved to DB
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field_value = pin_field.get_attribute("value")
        
        if (pin_field == "123!@#"):
            print("BUG DETECTED: PIN field with special characters was saved to the database!")
        self.assertEqual(pin_field_value, "123!@#", "BUG PIN with special characters saved to DB")

    # Test 16: Empty mobile number
    def test16_empty_mobile(self):
        print("Test 16: Verify mobile number cannot be empty")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Clear mobile field
        mobile_field = self.browser.find_element(By.NAME, "telephoneno")
        mobile_field.clear()
        sleep(.5)

        # Press tab to trigger warning message
        mobile_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message7")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Telephone no must not be blank")
            print("Test 16 warning displayed")
        except NoSuchElementException:
            print("Test 16 warning not displayed")

        # Check if empty mobile field is saved to DB
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        mobile_field = self.browser.find_element(By.NAME, "telephoneno")
        mobile_field_value = mobile_field.get_attribute("value")
        
        if mobile_field_value == "":
            print("BUG DETECTED: Empty mobile field was saved to the database!")
        self.assertEqual(mobile_field_value, "", "BUG Empty mobile field saved to DB")

    # Test 17: Mobile special characters
    def test17_mobile_special(self):
        print("Test 17: Verify mobile number cannot have special characters")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Enter special characters in mobile field
        mobile_field = self.browser.find_element(By.NAME, "telephoneno")
        mobile_field.clear()
        mobile_field.send_keys("886636!@!2")
        sleep(.5)

        # Press tab to trigger warning message
        mobile_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message7")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 17.1 warning displayed")
        except NoSuchElementException:
            print("Test 17.1 warning not displayed")

        mobile_field.clear()
        mobile_field.send_keys("!@886626682")
        sleep(.5)

        # Press tab to trigger warning message
        mobile_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message7")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 17.2 warning displayed")
        except NoSuchElementException:
            print("Test 17.2 warning not displayed")

        mobile_field.clear()
        mobile_field.send_keys("8866362!@")
        sleep(.5)

        # Press tab to trigger warning message
        mobile_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message7")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Special characters are not allowed")
            print("Test 17.3 warning displayed")
        except NoSuchElementException:
            print("Test 17.3 warning not displayed")

        # Check if mobile field with special characters is saved to DB
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        mobile_field = self.browser.find_element(By.NAME, "telephoneno")
        mobile_field_value = mobile_field.get_attribute("value")
        
        if "!" in mobile_field_value or "@" in mobile_field_value:
            print("BUG DETECTED: Mobile field with special characters was saved to the database!")
        self.assertEqual(mobile_field_value, "8866362!@", "BUG Mobile with special characters saved to DB")
        
    # Test 18: Empty email
    def test18_empty_email(self):
        print("Test 18: Verify email cannot be empty")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Clear email field
        email_field = self.browser.find_element(By.NAME, "emailid")
        email_field.clear()
        sleep(.5)

        # Press tab to trigger warning message
        email_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message9")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Email-ID must not be blank")
            print("Test 18 warning displayed")
        except NoSuchElementException:
            print("Test 18 warning not displayed")

        # Check if empty email field is saved to DB
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        email_field = self.browser.find_element(By.NAME, "emailid")
        email_field_value = email_field.get_attribute("value")
        
        if email_field_value == "":
            print("BUG DETECTED: Empty email field was saved to the database!")
        self.assertEqual(email_field_value, "", "BUG Empty email field saved to DB")

    # Test 19: Email format
    def test19_email_format(self):
        print("Test 19: Verify email must be in correct format")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Test with invalid email format
        email_field = self.browser.find_element(By.NAME, "emailid")
        email_field.clear()
        email_field.send_keys("guru99@gmail")
        sleep(.5)

        # Press tab to trigger warning message
        email_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message9")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Email-ID is not valid")
            print("Test 19.1 warning displayed")
        except NoSuchElementException:
            print("Test 19.1 warning not displayed")

        email_field.clear()
        email_field.send_keys("guru99")
        sleep(.5)

        # Press tab to trigger warning message
        email_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message9")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Email-ID is not valid")
            print("Test 19.2 warning displayed")
        except NoSuchElementException:
            print("Test 19.2 warning not displayed")

        email_field.clear()
        email_field.send_keys("guru99@")
        sleep(.5)

        # Press tab to trigger warning message
        email_field.send_keys(Keys.TAB)
        sleep(1)

        # Check if warning message is displayed
        cant_contain = self.browser.find_element(By.CSS_SELECTOR, "label#message9")
        try:
            self.assertTrue(cant_contain.is_displayed())
            self.assertEqual(cant_contain.text, "Email-ID is not valid")
            print("Test 19.3 warning displayed")
        except NoSuchElementException:
            print("Test 19.3 warning not displayed")

        # Check if invalid email format is saved to DB
        email_field.clear()
        email_field.send_keys("guru99@gmail.com")
        sleep(.5)
        
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)

        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        email_field = self.browser.find_element(By.NAME, "emailid")
        email_field_value = email_field.get_attribute("value")
        
        if email_field_value == "guru99@gmail.com":
            print("BUG DETECTED: Invalid email format was saved to the database!")
        self.assertEqual(email_field_value, "guru99@gmail.com", "BUG Invalid email format saved to DB")

    # Test 20: Submit button / Update customer details with valid data
    def test20_submit_button(self):
        print("Test 20: Verify update is successful with valid data")
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)

        # Update fields with valid data
        address_field = self.browser.find_element(By.NAME, "addr")
        address_field.clear()
        address_field.send_keys("123 Main St, Updated Address")
        
        city_field = self.browser.find_element(By.NAME, "city")
        city_field.clear()
        city_field.send_keys("Toronto")
        
        state_field = self.browser.find_element(By.NAME, "state")
        state_field.clear()
        state_field.send_keys("Ontario")
        
        pin_field = self.browser.find_element(By.NAME, "pinno")
        pin_field.clear()
        pin_field.send_keys("654321")
        
        mobile_field = self.browser.find_element(By.NAME, "telephoneno")
        mobile_field.clear()
        mobile_field.send_keys("9876543210")
        
        email_field = self.browser.find_element(By.NAME, "emailid")
        email_field.clear()
        email_field.send_keys("updated@email.com")
        sleep(1)
        
        # Submit changes
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)
        
        # Check if alert is present for successful update
        alert_text = self.capture_alert()
        self.assertIsNotNone(alert_text)
        self.assertTrue("Update done successfully" in alert_text, f"Expected success message, got: {alert_text}")
        sleep(1)
        
        # Verify the changes were saved correctly
        self.manager_login()
        self.go_edit_customer()
        self.submit_cust_id("43593")
        sleep(1)
        
        # Verify all updated fields
        address_value = self.browser.find_element(By.NAME, "addr").get_attribute("value")
        city_value = self.browser.find_element(By.NAME, "city").get_attribute("value")
        state_value = self.browser.find_element(By.NAME, "state").get_attribute("value")
        pin_value = self.browser.find_element(By.NAME, "pinno").get_attribute("value")
        mobile_value = self.browser.find_element(By.NAME, "telephoneno").get_attribute("value")
        email_value = self.browser.find_element(By.NAME, "emailid").get_attribute("value")
        
        self.assertEqual(address_value, "123 Main St, Updated Address", "Address not updated correctly")
        self.assertEqual(city_value, "Toronto", "City not updated correctly")
        self.assertEqual(state_value, "Ontario", "State not updated correctly")
        self.assertEqual(pin_value, "654321", "PIN not updated correctly")
        self.assertEqual(mobile_value, "9876543210", "Mobile not updated correctly")
        self.assertEqual(email_value, "updated@email.com", "Email not updated correctly")
        
        print("Test 20 passed - Update successful")


if __name__ == '__main__':
    unittest.main()
