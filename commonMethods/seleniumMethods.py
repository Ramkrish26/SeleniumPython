# This file contains all the selenium methods that are used in common
from selenium import webdriver
from selenium.webdriver import *
from configparser import ConfigParser

config = ConfigParser()
config.read("D:/Python Projects/BasicAutomation/Configuration/Config.cfg")

class selMethods:

    def browserStart(self):
        if(config.get("BrowserSetup","BrowserName") == "chrome"):
            global driver
            driver = webdriver.Chrome("D:/Python Projects/BasicAutomation/drivers/chromedriver.exe")
            driver.maximize_window()

    def launchURL(self, url):
        driver.get(url)

    def getElement(self, locator, value):
         element = {
            "id" : driver.find_element_by_id(value),
            "class" : driver.find_element_by_class_name(value),
            "name" : driver.find_element_by_name(value),
            "xpath" : driver.find_element_by_xpath(value)
         }
         return element

    def getElements(self, locator, value):
        element = {
            "id": driver.find_elements_by_id(value),
            "class": driver.find_elements_by_class_name(value),
            "name": driver.find_elements_by_name(value),
            "xpath": driver.find_elements_by_xpath(value)
        }