# Reggie Brown
# INFT 1207
# Lab 5
# Prof Patel
# Desc: This Selenium script automates shopping, using different filters and web elements

import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class Lab5TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        sleep(2)

    def test1_navigate_category(self):
        print("Test 1: Navigate to women, tops, hoodies and sweatshirts")

        driver = self.driver

        driver.get("https://magento.softwaretestingboard.com/")
        sleep(2)

        # click on women menu
        driver.find_element(By.ID, "ui-id-4").click()
        sleep(2)

        # navigate to hoodies and sweatshirts
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[1]/li[1]/a").click()

    def test2_filters(self):
        print("Test 2: Applying filters")

        driver = self.driver

        # expand style section





