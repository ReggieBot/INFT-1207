import unittest
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


class RadioButtonDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        sleep(2)

    def test01_radiobutton(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://demo.guru99.com/test/radio.html")
        sleep(5)

        # Check the Option 1 radiobutton


        # Check the Option 3 radiobutton- SEE THE DIFFERENCE- at one point only one radio button is active


        # Get the total of all buttons

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
