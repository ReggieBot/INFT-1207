# Reggie Brown
# INFT 1207
# Lab 5
# Prof Patel
# Desc: This Selenium script automates shopping, using different filters and web elements
# References: https://www.geeksforgeeks.org/move_to_element-method-action-chains-in-selenium-python/

import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


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
        women_menu = driver.find_element(By.ID, "ui-id-4")
        women_menu.click()
        sleep(2)

        # navigate to hoodies and sweatshirts
        hoodie_sweatshirt = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[1]/li[1]/a")
        hoodie_sweatshirt.click()
        sleep(2)

    def test2_filters(self):
        print("Test 2: Applying filters")

        driver = self.driver

        # expand style section
        expand_style = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div/div[1]/div[1]")
        expand_style.click()
        sleep(1)

        # click on pullover style
        select_pullover = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/ol/li[3]/a")
        select_pullover.click()
        sleep(2)

        # expand size filter
        expand_size = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div[3]/div[1]/div[1]")
        expand_size.click()
        sleep(1)

        # select size medium
        size_medium = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/div/a[3]/div")
        size_medium.click()
        sleep(1)

        # Expand price range filter
        price_filter = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div[3]/div[9]/div[1]")
        price_filter.click()
        sleep(1)

        # Select price range
        price_range = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div[3]/div[9]/div[2]/ol/li[3]/a/span[1]")
        price_range.click()
        sleep(1)

        # Expand colour filter
        expand_colour = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div[3]/div[2]/div[1]")
        expand_colour.click()
        sleep(1)

        # select purple colour
        colour_purple = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/div/a[4]/div")
        colour_purple.click()
        sleep(1)

        # Expand material filter
        expand_material = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div[3]/div[4]/div[1]")
        expand_material.click()
        sleep(1)

        # select polyester material
        polyester = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div[3]/div[4]/div[2]/ol/li[3]/a")
        polyester.click()
        sleep(1)

    def test3_add_to_cart(self):
        print("Test 3: Adding product to cart")
        # Unfortunately, if you select the product after applying all the filters, the product is then reset without
        # the filters. So action chains are needed to hover over the product.
        # When hovered over, an add to cart button appears
        # Though even after that, it still resets filters when added to cart. I give up.
        # I'll keep this action chains code in here though.

        driver = self.driver

        # find the first available product
        product = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a")
        sleep(1)

        # create action chain for hovering (see reference)
        actions = ActionChains(driver)
        actions.move_to_element(product).perform()
        sleep(2)

        # Look for add to cart button that appears after hovering
        add_to_cart = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[4]/div/div[1]/form/button")
        add_to_cart.click()
        sleep(3)

    def test4_verify_and_checkout(self):
        print("Test 4: Check cart and checkout")

        driver = self.driver

        # click on cart icon
        cart_icon = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a")
        cart_icon.click()
        sleep(2)

        # click on proceed to checkout
        checkout_button = driver.find_element(By.XPATH, "html/body/div[2]/header/div[2]/div[1]/div/div/div/div[2]/div[3]/div/button")
        checkout_button.click()
        sleep(2)

        # Assert the order summary
        order_summary = driver.find_element(By.CLASS_NAME, "opc-block-summary")
        self.assertTrue(order_summary.is_displayed(), "Order summary is not displayed")
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()


