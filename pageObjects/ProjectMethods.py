import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Utilities import XLUtilis
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
import json
from pathlib import Path

class ProjectMethods(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cl = LogGen.loggen()
    # -------------- Login Screen Methods --------------
    def verifyUserLoggedIN(self,expected,ssname):
        if expected == "pass" or expected == "Pass":
            url = self.driver.current_url
            exp = "dashboard"
            if exp in url:
                self.cl.info("---------- Test Passed - User Logged In Successfully -----------")
                assert True
            else:
                self.cl.info("---------- Test Failed - User Is Not Logged In Successfully -----------")
                self.takeScreenshot(ssname)
                assert False
        elif expected == "fail" or expected == "Fail":
            url = self.driver.current_url
            exp = "login"
            if exp in url:
                self.cl.info("---------- Test Passed - User Is Not Logged In Successfully -----------")
                assert True
            else:
                self.cl.info("---------- Test Failed - User Is Logged In Successfully -----------")
                self.takeScreenshot(ssname)
                assert False

    def verifyForgotPassword(self,expected,ssname):
        if expected == "pass" or expected == "Pass":
            url = self.driver.current_url
            exp = "reset-code"
            if exp in url:
                self.cl.info("---------- Test Passed - User Logged In Successfully -----------")
                assert True
            else:
                self.cl.info("---------- Test Failed - User Is Not Logged In Successfully -----------")
                self.takeScreenshot(ssname)
                assert False
        elif expected == "fail" or expected == "Fail":
            url = self.driver.current_url
            exp = "forgot-password"
            if exp in url:
                self.cl.info("---------- Test Passed - User Is Not Logged In Successfully -----------")
                assert True
            else:
                self.cl.info("---------- Test Failed - User Is Logged In Successfully -----------")
                self.takeScreenshot(ssname)
                assert False

    # -------------- Categories Screen Methods --------------

    def setSearchField(self, text):
        self.sendText(text, self.searchFieldLV, self.searchFieldLT)

    def searchVerifcationMethodValid(self, text):
        searchText = text
        self.setSearchField(searchText)
        try:
            time.sleep(3)
            element = self.driver.find_element(By.XPATH, "//td[@data-field='name']")
            if element is not None:
                text = element.text
                self.cl.info(text)
                self.cl.info(searchText)
                if searchText in text:
                    self.cl.info(" ---------- Test Passed - Data Found ---------- ")
                    assert True
                else:
                    self.cl.info(" ---------- Test Failed - Data Not Found---------- ")
                    assert False
            else:
                assert False
        except NoSuchElementException as exc:
            self.cl.info("No element found with given locator value")
            assert False

    def searchVerifcationMethodInValid(self):
        self.setSearchField("searchText")
        try:
            time.sleep(3)
            element1 = self.driver.find_element(By.XPATH, "//span[normalize-space()='No records found']")
            if element1 is not None:
                self.cl.info(" ---------- Test Passed - Data Not Found ---------- ")
                assert True
            else:
                self.cl.info(" ---------- Test Failed - Data Found---------- ")
                assert False
        except NoSuchElementException as exc:
            self.cl.info("No element found with given locator value")
            assert False
