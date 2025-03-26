import unittest
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager


class RadioButtonDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        sleep(2)

    def test01_radiobutton(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://demo.guru99.com/test/radio.html")
        sleep(5)

        # Check the Option 1 radiobutton
        driver.find_element(By.ID, "vfb-7-1").click()
        sleep(3)
        # Check the Option 3 radiobutton- SEE THE DIFFERENCE- at one point only one radio button is active
        driver.find_element(By.ID, "vfb-7-3").click()
        sleep(3)

        # Get the total of all buttons (number of radio buttons)
        num_radio_btn = driver.find_elements(By.XPATH, "//input[@type='radio']")
        print(f"There are {len(num_radio_btn)} buttons")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
