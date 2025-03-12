from time import sleep
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoSeleniumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        # Open the following url in the browser
        cls.browser.get("https://www.selenium.dev/selenium/web/web-form.html")
        sleep(1)

    def test_page_title(self):
        self.assertIn("Web form", self.browser.title)
        sleep(1)

    def test_fill_text_and_submit(self):
        # find the Text input textbox
        text_box = self.browser.find_element(By.NAME, "my-text")
        # fill in the textbox using send_keys method
        text_box.send_keys("Hello Selenium")
        sleep(1)

        # find the submit button using find_element
        submit_button = self.browser.find_element(By.CSS_SELECTOR, "button")
        # click the submit button
        submit_button.click()
        sleep(1)

        # find the message button
        message = self.browser.find_element(By.ID, "message")
        # verify the text is correct
        self.assertEqual("Received!", message.text, "Error in Form Submission")
        sleep(1)

    def test_scroll_and_click(self):
        self.browser.get("https://www.selenium.dev/")
        sleep(1)

        # scroll to the bottom
        # 1. Find the footer
        # 2. Scroll the page till the footer is in view

        footer = self.browser.find_element(By.CSS_SELECTOR, "footer")

        # use the execute script method
        self.browser.execute_script("arguments[0].scrollIntoView(true);", footer)
        sleep(1)

        # click the "Open Collective" link
        open_collective_link = self.browser.find_element(By.LINK_TEXT, "Open Collective")
        open_collective_link.click()
        sleep(1)
        self.browser.switch_to(self.browser.window_handles[-1])
        self.assertIn("Selenium - Open Collective", self.browser.title)
