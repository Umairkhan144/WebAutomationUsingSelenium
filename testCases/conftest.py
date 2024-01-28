from selenium import webdriver
import pytest

#Here we are setting up the brwosers to run our test cases
import os
import pytest
import time
from pageObjects.DriverClass import Driver

@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')

#
# @pytest.fixture()
# def setup(request):
#     browser = request.config.getoption("--browser") or "chrome"  # default browser is chrome
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         driver = webdriver.Chrome()
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser name")
#
# @pytest.fixture()
# def browser(request):
#     # Here we will return the browser name to the setup method
#     return request.config.getoption("--browser")

################### PyTest HTML Report ######################

# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Case Management'
    config._metadata['Module Name'] = 'Super Admin'
    config._metadata['Tester'] = 'Umair'

# It is hook for delete/modify Environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)