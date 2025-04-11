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
sc
import unittest;
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class TestDeleteCustomer(unittest.TestCase):
    # 8 Test cases 

