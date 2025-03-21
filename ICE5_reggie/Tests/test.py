# Reggie Brown
# INFT 1207
# Prof Patel
# Desc: Created a new user on test site with predefined credentials and validates successful auth using python/selenium
# References: https://www.browserstack.com/guide/isdisplayed-method-in-selenium
# github: https://github.com/ReggieBot/INFT-1207/tree/main/ICE5_reggie/Tests

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

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     sleep(5)
    #     cls.browser.quit()
    #     # Tear down method for closing script after exec.

    def test1_Register_User(self):
        # First test case: Register user with username "Reggie" and password "durhamcollege2025"
        # First login using "tutorial" as username/password
        # Print statement to keep track of test progress
        print("sending username and password = Tutorial")
        self.browser.find_element(By.NAME, "userName").send_keys("tutorial")
        self.browser.find_element(By.NAME, "password").send_keys("tutorial")
        self.browser.find_element(By.NAME, "submit").click()
        sleep(1)

        # Verify login was successful using assetTrue and .isDisplayed() method. (Referenced in header comments)
        # Uses XPATH to check if <h3> element contains "Login Successfully". Then asserts if true
        login_success = self.browser.find_element(By.XPATH, "//h3[contains(text(), 'Login Successfully')]")
        self.assertTrue(login_success.is_displayed())
        print("Initial login successfull")

        # Click on register
        # Searches for link with text "REGISTER"
        self.browser.find_element(By.LINK_TEXT, "REGISTER").click()
        # Filling in registration details (contact)
        self.browser.find_element(By.NAME, "firstName").send_keys("Reggie")
        self.browser.find_element(By.NAME, "lastName").send_keys("Brown")
        self.browser.find_element(By.NAME, "phone").send_keys("2898304494")
        self.browser.find_element(By.ID, "userName").send_keys("reggie.brown@dcmail.ca")
        print("Successfully filled in contact information")
        sleep(1)

        # Filling in registration details (mailing)
        self.browser.find_element(By.NAME, "address1").send_keys("35 Hockley Avenue")
        self.browser.find_element(By.NAME, "city").send_keys("Bowmanville")
        self.browser.find_element(By.NAME, "state").send_keys("Ontario")
        self.browser.find_element(By.NAME, "postalCode").send_keys("L1C 5P2")
        self.browser.find_element(By.NAME, "country").send_keys("CANADA")
        print("Successfully filled in mailing information")
        sleep(1)

        # Filling in registration details (user)
        # Why is the ID/name for Username = email? Who knows.
        self.browser.find_element(By.ID, "email").send_keys("Reggie")
        self.browser.find_element(By.NAME, "password").send_keys("durhamcollege2025")
        self.browser.find_element(By.NAME, "confirmPassword").send_keys("durhamcollege2025")
        sleep(1)

        # Submit
        self.browser.find_element(By.NAME, "submit").click()
        sleep(1)

        # Assert that registration successful
        registration_success = self.browser.find_element(By.XPATH, "//b[contains(text(),'Your user name is Reggie.')]")
        self.assertTrue(registration_success.is_displayed())
        print("Registration Successful")
        sleep(2)

    def test2_Login_User(self):
        # Second test case: Login with newly created user account and assert login successful
        # Return to homepage
        self.browser.get("https://demo.guru99.com/test/newtours/")
        print("Successfully navigated to homepage")
        sleep(2)

        # Click on "sign on" - This site is riddled with typos
        self.browser.find_element(By.LINK_TEXT, "SIGN-ON").click()
        sleep(1)

        # Login with new user account by locating elements and sending keys.
        self.browser.find_element(By.NAME, "userName").send_keys("Reggie")
        self.browser.find_element(By.NAME, "password").send_keys("durhamcollege2025")
        sleep(1)

        # Click on submit
        self.browser.find_element(By.NAME, "submit").click()
        sleep(2)

        # Assert that login successful
        newlogin_success = self.browser.find_element(By.XPATH, "//h3[contains(text(),'Login Successfully')]")
        self.assertTrue(newlogin_success.is_displayed())
        print("Successfully logged in with new user")


if __name__ == '__main__':
    unittest.main()
