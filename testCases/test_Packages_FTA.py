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
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=9)
        self.pm.verifyUserLoggedIN("Pass", "test_001_login_valid")

    def test_002_Create_Category_With_Blank_Name(self):
        self.gm.createMethod("memberships tab","packages tab","add package btn","Title","Sub Title","Description","Ordering","Type","Duration","Price","Product Id","Ahi Product Id","Save_btn",module_name="memberships",sheet_name="Create Packages",row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_002_Create_Category_With_Blank_Name",sheet_name="Create Packages",row_num=2,col_num=1,exp="Fail")

    def test_003_Create_Category_With_Tile_Blank(self):
        self.gm.createMethod("Title","Sub Title","Description","Ordering","Type","Duration","Price","Product Id","Ahi Product Id","Save_btn",module_name="memberships",sheet_name="Create Packages",row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_003_Create_Category_With_Tile_Blank",sheet_name="Create Packages",row_num=3,col_num=1,exp="Fail")

    def test_004_Create_Category_With_Ordering_Blank(self):
        self.gm.createMethod("Title","Sub Title","Description","Ordering","Type","Duration","Price","Product Id","Ahi Product Id","Save_btn",module_name="memberships",sheet_name="Create Packages",row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_004_Create_Category_With_Blank_Name",sheet_name="Create Packages",row_num=4,col_num=1,exp="Fail")

    def test_005_Create_Category_With_Type_Blank(self):
        self.gm.refreshPage()
        self.gm.createMethod("Title","Sub Title","Description","Ordering","Type","Duration","Price","Product Id","Ahi Product Id","Save_btn",module_name="memberships",sheet_name="Create Packages",row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_005_Create_Category_With_Type_Blank",sheet_name="Create Packages",row_num=5,col_num=1,exp="Fail")
