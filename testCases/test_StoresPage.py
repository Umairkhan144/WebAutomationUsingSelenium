import os
import unittest
import pytest
from pageObjects.GenericMethods import GenericMethods
from pageObjects.ProjectMethods import ProjectMethods
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time
from pageObjects.StoresPage import StorePage
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class UserFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.logger = LogGen.loggen()
        self.gm = GenericMethods(self.driver)
        self.pm = ProjectMethods(self.driver)

    def test_001_login(self):
        url = self.gm.get_url()
        self.driver.get(url)
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=9)
        self.pm.verifyUserLoggedIN("Pass", "test_001_login_valid")

    def test_003_Create_Store_With_All_Fields_Blank(self):
        self.gm.createMethod("store tab", "add store btn", "Name", "Logo", "URL", "Save_btn", module_name="stores", row_num=2, sheet_name="Create Store")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_003_Create_Store_With_All_Fields_Blank",sheet_name="Create Store", row_num=2, col_num=1, exp="fail")

    def test_004_Create_Store_With_StoreName_Blank(self):
        self.gm.createMethod("store tab", "add store btn", "Name", "Logo", "URL", "Save_btn", module_name="stores",row_num=3, sheet_name="Create Store")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_004_Create_Store_With_StoreName_Blank",sheet_name="Create Store", row_num=3, col_num=1, exp="fail")

    def test_005_Create_Store_With_Logo_Field_Blank(self):
        self.gm.createMethod("store tab", "add store btn", "Name", "Logo", "URL", "Save_btn", module_name="stores",row_num=4, sheet_name="Create Store")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_005_Create_Store_With_Logo_Field_Blank",sheet_name="Create Store", row_num=4, col_num=1, exp="fail")

    def test_006_Create_Store_With_URL_Field_Blank(self):
        self.gm.createMethod("store tab", "add store btn", "Name", "Logo", "URL", "Save_btn", module_name="stores",row_num=5, sheet_name="Create Store")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_006_Create_Store_With_URL_Field_Blank",sheet_name="Create Store", row_num=5, col_num=1, exp="fail")

    def test_007_Create_Store_With_All_Valid_Data(self):
        self.gm.createMethod("store tab", "add store btn", "Name", "Logo", "URL", "Save_btn", module_name="stores",row_num=6, sheet_name="Create Store")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_007_Create_Store_With_All_Valid_Data",sheet_name="Create Store", row_num=6, col_num=1, exp="pass")

    def test_008_Delete_New_Created_Store(self):
        self.gm.deleteMethod("Test Store",module_name="stores",ssname="test_008_Delete_New_Created_Store")

    