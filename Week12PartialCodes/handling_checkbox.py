import unittest
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By

# from webdriver_manager.firefox import FirefoxDriverManager


class CheckboxDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        sleep(2)

    def test01_checkbox(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://demo.guru99.com/test/radio.html")
        sleep(5)

        # Check the second checkbox
        driver.find_element(By.ID, "vfb-6-1").click()
        sleep(3)

        # Check the third checkbox- SEE THE DIFFERENCE- at one point only one radio button is active
        driver.find_element(By.ID, "vfb-6-2").click()
        sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
