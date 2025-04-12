# Reggie Brown
# reggie.brown@dcmail.ca
# INFT 1207 - Final Project 
# Prof. Patel
# Desciption: This file contains 20 test cases for the "delete customer" 
# functionality of the guru99 bank application. Test cases were written with unittest & selenium
# Github: https://github.com/ReggieBot/INFT-1207/tree/main/FinalProject_ReggieBrown

# REFERENCES: 
# https://www.selenium.dev/documentation/webdriver/elements/interactions/      .clear()
# https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-element-exception noSuchElementException
# https://www.browserstack.com/guide/alerts-and-popups-in-selenium
# https://www.browserstack.com/guide/noalertpresentexception-in-selenium

# This test file assumes that a customer accont has already been created.
# Account created by me - Customer ID = 43593

import unittest;
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class TestDeleteCustomer(unittest.TestCase):
    # 8 test cases for the delete customer functionality

    @classmethod
    def setUpClass(cls) -> None:
        # set up webdriver (firefox)
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()

        # nav to site
        cls.browser.get("http://demo.guru99.com/V4/")
        sleep(1.5)

        # log in with manager credentials
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
    def go_delete_customer(self):
        # nav to delete customer page
        self.browser.find_element(By.LINK_TEXT, "Delete Customer").click()
        sleep(1)

    def enter_customer_id(self, customer_id):
        # enter customer id
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        customer_id_field.clear()
        customer_id_field.send_keys(customer_id)
        sleep(.5)

    def accept_alert(self):
        # accept alert if present
        try:
            alert = self.browser.switch_to.alert
            text = alert.text  
            alert.accept()
            return text
        except NoAlertPresentException:
            return None

    def manager_login(self):
        # log in with manager credentials
        self.browser.find_element(By.NAME, "uid").send_keys("mngr619261")
        self.browser.find_element(By.NAME, "password").send_keys("anugagy")
        self.browser.find_element(By.NAME, "btnLogin").click()
        sleep(1)

    def test01_blank_cust_id(self):
        # test 1: blank customer id
        self.go_delete_customer()
        self.enter_customer_id("")

        # tab to trigger warning message
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)

        try:
            warning_msg = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
            self.assertTrue(warning_msg.is_displayed())
            self.assertEqual(warning_msg.text, "Customer ID can not be blank")
            print("Test 1 warning displayed")
        except NoSuchElementException:
            print("Test 1 warning not displayed")
        
        # check if alert is present
        self.browser.find_element(By.NAME, "cusid").click()
        sleep(1)
        alert_text = self.accept_alert()
        if alert_text:
            print("Test 1 alert displayed")
        else:
            print("Test 1 alert not displayed")

        print("Test 1 completed")

    def test02_numeric_id(self):
        # test 2: customer ID must be numeric
        self.go_delete_customer()
        self.enter_customer_id("1234")
        sleep(1)

        # tab to trigger warning message (should not be displayed)
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)

        try:
            warning_msg = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
            self.assertFalse(warning_msg.is_displayed())
            print("Test 2 warning not displayed")
        except:
            print("Test 2 warning displayed unexpectedly")

        self.enter_customer_id("Acc123")
        sleep(1)

        # tab to trigger warning message
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)

        try: 
            warning_msg = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
            self.assertTrue(warning_msg.is_displayed())
            self.assertEqual(warning_msg.text, "Characters are not allowed")
            print("Test 2 warning displayed")
        except NoSuchElementException:
            print("Test 2 warning not displayed")

        # check if alert is present
        self.browser.find_element(By.NAME, "cusid").click()
        sleep(1)
        alert_text = self.accept_alert()
        if alert_text:
            print("Test 2 alert is displayed")
        else:
            print("Test 2 alert not displayed")

        print("Test 2 completed")

    def test03_specialChar(self):
        # test 3: customer ID must not contain special characters 
        self.go_delete_customer()
        self.enter_customer_id("123!@#")
        sleep(1)

        # tab to trigger warning message
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)

        try:
            warning_msg = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
            self.assertTrue(warning_msg.is_displayed())
            self.assertEqual(warning_msg.text, "Special characters are not allowed")
            print("Test 3 warning displayed")
        except NoSuchElementException:
            print("Test 3 warning not displayed")

        self.enter_customer_id("!@#")
        sleep(1)
        
        # tab to trigger warning message
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)

        try:
            warning_msg = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
            self.assertTrue(warning_msg.is_displayed())
            self.assertEqual(warning_msg.text, "Special characters are not allowed")
            print("Test 3 warning displayed")
        except NoSuchElementException:
            print("Test 3 warning not displayed")

        # check if alert is present
        self.browser.find_element(By.NAME, "cusid").click()
        sleep(1)
        alert_text = self.accept_alert()
        if alert_text:
            print("Test 3 alert is displayed")
        else:
            print("Test 3 alert not displayed")

        print("Test 3 completed")

    def test04_blank_spaces(self):
        # test 4: customer ID must not contain blank spaces
        self.go_delete_customer()
        self.enter_customer_id("123 12")
        sleep(1)

        # tab to trigger warning message
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)

        try:
            warning_msg = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
            self.assertTrue(warning_msg.is_displayed())
            self.assertEqual(warning_msg.text, "Special characters are not allowed")
            print("Test 4 warning displayed")
        except NoSuchElementException:
            print("Test 4 warning not displayed")

        # check if alert is present
        self.browser.find_element(By.NAME, "cusid").click()
        sleep(1)
        alert_text = self.accept_alert()
        if alert_text:
            print("Test 4 alert is displayed")
        else:
            print("Test 4 alert not displayed")

        print("Test 4 completed")

    def test05_first_char_space(self):
        # test 5: first character cannot be space
        self.go_delete_customer()
        self.enter_customer_id(" ")
        sleep(1)

        # tab to trigger warning message
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)

        try:
            warning_msg = self.browser.find_element(By.CSS_SELECTOR, "label#message14")
            self.assertTrue(warning_msg.is_displayed())
            self.assertEqual(warning_msg.text, "First character can not have space")
            print("Test 5 warning displayed")
        except NoSuchElementException:
            print("Test 5 warning not displayed")
        
        # check if alert is present
        self.browser.find_element(By.NAME, "cusid").click()
        sleep(1)
        alert_text = self.accept_alert()
        if alert_text:
            print("Test 5 alert is displayed")
        else:
            print("Test 5 alert not displayed")
        
        print("Test 5 completed")

    def test06_invalid_cust_id(self):
        # test 6: customer ID must be valid to delete
        self.go_delete_customer()
        self.enter_customer_id("123456")
        sleep(1)
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        alert_text = self.accept_alert()
        
        # accept first alert
        self.assertIsNotNone(alert_text, "Test 6 alert_1 not displayed")
        print("Test 6 alert_1 displayed")
        sleep(2)
        
        # accept second alert and assert text
        alert_text2 = self.accept_alert()
        self.assertIsNotNone(alert_text2, "Test 6 alert_2 not dislayed")
        self.assertEqual(alert_text2, "Customer does not exist!!")

        print("Test 6 completed")

    def test07_valid_id(self):
        # test 7: valid customer ID 
        self.go_delete_customer()
        self.enter_customer_id("43593")
        sleep(1)
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        # accept first alert
        alert_text = self.accept_alert()
        self.assertIsNotNone(alert_text, "Test 7 alert_1 not displayed")
        print("Test 7 alert_1 displayed")
        sleep(2)

        # accept second alert and assert text
        alert_text02 = self.accept_alert()
        self.assertIsNotNone(alert_text02, "Test 7 alert_2 not displayed")
        self.assertEqual(alert_text02, "Customer does not exist!!")
        print("Test 7 alert_2 displayed")
        
        print("Test 7 completed")

    def test08_reset_btn(self):
        # test 8: verify reset button clears customer ID field
        self.go_delete_customer()
        self.enter_customer_id("qwer")
        sleep(1)
        self.browser.find_element(By.NAME, "res").click()
        sleep(1)
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        id_field_value = customer_id_field.get_attribute("value")
        self.assertEqual(id_field_value, "", "Test 8 btn not working")

        self.enter_customer_id("123457")
        sleep(1)
        self.browser.find_element(By.NAME, "res").click()
        sleep(1)
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        id_field_value = customer_id_field.get_attribute("value")
        self.assertEqual(id_field_value, "", "Test 8 btn not working")

        print("Test 8 completed")


if __name__ == '__main__':
    unittest.main()
