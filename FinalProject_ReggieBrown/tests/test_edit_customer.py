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



    def test1_edit_valid(self):
        print("Test1: Editing customer with valid data")

        self.go_edit_customer()
        self.submit_cust_id("43593")
        
        # update editable fields (name, gender, DOB - not editable)
        
        # address
        self.browser.find_element(By.NAME, "addr").clear()
        self.browser.find_element(By.NAME, "addr").send_keys("36 Hockley Avenue")
 
        # city
        self.browser.find_element(By.NAME, "city").clear()
        self.browser.find_element(By.NAME, "city").send_keys("Oshawa")

        # state (province)
        self.browser.find_element(By.NAME, "state").clear()
        self.browser.find_element(By.NAME, "state").send_keys("Alberta")

        # pin
        self.browser.find_element(By.NAME, "pinno").clear()
        self.browser.find_element(By.NAME, "pinno").send_keys("696969")

        # phone #
        self.browser.find_element(By.NAME, "telephoneno").clear()
        self.browser.find_element(By.NAME, "telephoneno").send_keys("911")

        # email
        self.browser.find_element(By.NAME, "emailid").clear()
        self.browser.find_element(By.NAME, "emailid").send_keys("testemail@gmail.com")
        sleep(.5)

        # sumbit changes
        self.browser.find_element(By.NAME, "sub").click()
        sleep(1)


        # check for success message
        try: 
            success_msg = self.browser.find_element(By.XPATH, "//p[contains(text(),'Edit Successfull')]")
            self.assertTrue(success_msg.is_displayed())
            print("Test1 passed: Valid edit successful.")

        except NoSuchElementException:
            print("No success message found")

            # check if data was still updated
            # checks if address = new address
            self.browser.get("http://demo.guru99.com/V4/")
            sleep(.5)
            self.browser.find_element(By.NAME, "uid").send_keys("mngr619261")
            self.browser.find_element(By.NAME, "password").send_keys("anugagy")
            self.browser.find_element(By.NAME, "btnLogin").click()
            self.go_edit_customer()
            self.submit_cust_id("43593")
            sleep(1)

            # checks if address = new address
            current_address = self.browser.find_element(By.NAME, "addr").get_attribute("value")

            if current_address == "36 Hockley Avenue":
                print("Data updated successfully. Success message not displayed. Test 1 failed.")
            else:
                print("No success message AND data not updated. Test 1 failed.")


    def test2_customer_id_nonexist(self):
        print("Test2: Attempt to edit a non existent ID.")
        self.go_edit_customer()

        # Enter a random invalid ID
        self.submit_cust_id("123456")

        # Expect alert
        # Switch to alert, then accept
        # assert that alert text contains expected message
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            self.assertIn("Customer does not exist!!", alert_text)
            print("Test2 passed: Alert displayed for non-existent ID.")
        except:
            self.fail("Non existent ID does not trigger alert. Test 2 failed.")
    
if __name__ == '__main__':
    unittest.main()
    