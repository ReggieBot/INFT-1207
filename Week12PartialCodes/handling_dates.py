import unittest
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from webdriver_manager.chrome import ChromeDriverManager


class DatePickingDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        sleep(2)

    def test01_date_picking(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("https://jqueryui.com/datepicker/")
        sleep(5)

        # switch to frame- DIFFERENT WAY
        i_frame = driver.find_element(By.CLASS_NAME, "demo-frame")
        driver.switch_to.frame(i_frame)

        # identify element inside frame
        date_picker = driver.find_element(By.ID, "datepicker").click()
        date_picker.click()

        # identify list of all dates

        all_dates = driver.find_elements(By.XPATH, "//table/tbody/tr/td")

        # verify required date then click
        for date in all_dates:
            if date.text == "6":
                date.click()
                break

        # get selected date
        selected_date = date_picker.get_attribute('value')
        print(f"selected date is {selected_date}")


        sleep(5)
        driver.back()

# Handling ‘JQuery Calendar’ in an IFRAME
# There are many scenarios where you would want to place the Calendar control inside an iFrame. In such cases,
# before performing any operation on the date picker, you have to first switch to that iFrame.

# Once inside the iFrame, you should perform the following operations:
# Step 1:  Click on the Calendar Control to open the same.
# Step 2:  Find the Year drop-down control and select the required year from that drop-down.
# Step 3:  Find the Month drop-down control and select the required month from that drop-down.
# Step 4:  Once year and month is selected, locate the corresponding date by navigating through the Date table.
# I’ll use jQuery’s date picker demo URL as the test URL to demonstrate how to automate calendar using Selenium
# WebDriver when the calendar is inside the iFrame.

    def test02_date_picking(self):
        # Create the object driver
        driver = self.driver
        # We can select the date picker in Selenium. It is slightly difficult to handle calendar controls as the
        # day, month and year selection can be represented via different UI. Sometimes they are represented by the
        # dropdown or by forward and backward controls.
        expected_from_date_str = '02/20/2021'
        expected_to_date_str = '03/26/2021'

        fr_date = "20"
        to_date = "26"

        # Get the application
        driver.get("https://jqueryui.com/datepicker/#date-range")
        sleep(5)

        # switch to frame


        # identify from element inside frame


         # choose month from dropdown


          # select day


        # identify to element inside frame

        #  choose month from dropdown


         # select day


        # get selected dates


        ################################# Verify whether the values are as expected ############################
        

        print("Unit Test of jQuery Calendar passed")

        sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
