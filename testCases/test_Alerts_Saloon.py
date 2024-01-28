import os
import time
import unittest
from pathlib import Path
import pytest
from Utilities.customLogger import LogGen
from pageObjects.GenericMethods import GenericMethods
from pageObjects.ProjectMethods import ProjectMethods
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class CategoryFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.logger = LogGen.loggen()
        self.gm = GenericMethods(self.driver)
        self.pm = ProjectMethods(self.driver)

    def test_001_login_valid(self):
        url = self.gm.get_url()
        self.driver.get(url)
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=10)
        self.pm.verifyUserLoggedIN("Pass", "test_001_login_valid")

    def test_002_Redirect_To_Alerts(self):
        self.gm.createMethod("skip tour","alerts tab","create alert btn","immediate btn","continue btn","Alert Title","Alert Message","assign recipients","everyone","send alert btn",module_name="alerts",sheet_name="Alerts",row_num=2)

