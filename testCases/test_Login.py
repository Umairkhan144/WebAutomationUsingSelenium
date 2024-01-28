import unittest
import pytest
from Utilities.readProperties import ReadConfig
from pageObjects.GenericMethods import GenericMethods
from pageObjects.ProjectMethods import ProjectMethods
from Utilities.customLogger import LogGen
import time
from dotenv import load_dotenv
import json
import os
load_dotenv()

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.logger = LogGen.loggen()
        self.gm = GenericMethods(self.driver)
        self.pm =ProjectMethods(self.driver)

    # This is our data which we are using in our Login Test case
    # coming from config.ini file using readProperties Methods form Utilities Package
    baseURL = ReadConfig.getbaseURl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # This is our function/method/testcase which will run the test on browser:
    def test_001_login_With_Balnk_Username_and_Blank_Password(self):
        url = self.gm.get_url()
        self.driver.get(url)
        self.gm.createMethod("forgot password btn", "Email", module_name="login", sheet_name="Forgot Password",row_num=2)
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=2)
        self.pm.verifyUserLoggedIN("Fail", "test_001_login_With_Blank_Username_and_Blank_Password")

    def test_002_login_With_Invalid_Username_and_Invalid_Password(self):
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=3)
        self.pm.verifyUserLoggedIN("fail", "test_002_login_With_Invalid_Username_and_Invalid_Password")

    def test_003_login_With_Invalid_Username_and_Blank_Password(self):
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=4)
        self.pm.verifyUserLoggedIN("fail", "test_003_login_With_Invalid_Username_and_Blank_Password")

    def test_004_login_With_Valid_Username_and_Invalid_Password(self):
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=5)
        self.pm.verifyUserLoggedIN("fail", "test_004_login_With_Valid_Username_and_Invalid_Password")

    def test_005_login_With_Balnk_Username_and_Valid_Password(self):
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=6)
        self.pm.verifyUserLoggedIN("fail", "test_005_login_With_Balnk_Username_and_Valid_Password")

    def test_006_login_With_Invalid_Username_and_Valid_Password(self):
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=7)
        self.pm.verifyUserLoggedIN("fail", "test_006_login_With_Invalid_Username_and_Valid_Password")

    def test_007_login_With_Invalid_Email_Format(self):
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=8)
        self.pm.verifyUserLoggedIN("fail", "test_007_login_With_Invalid_Email_Format")

    def test_008_login_With_Valid_Email_Blank_Password(self):
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=9)
        self.pm.verifyUserLoggedIN("fail", "test_008_login_With_Valid_Email_Blank_Password")

    def test_009_login_With_Valid_Credentials(self):
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=10)
        self.pm.verifyUserLoggedIN("fail", "test_009_login_With_Valid_Credentials")







