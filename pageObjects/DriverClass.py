from selenium import webdriver
import pytest

class Driver:
    def getDriverMethod(self):
        driver = webdriver.Chrome()
        return driver