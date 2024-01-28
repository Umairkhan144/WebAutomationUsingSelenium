import os
import unittest
from pathlib import Path
import pytest
from Utilities.customLogger import LogGen
from pageObjects.GenericMethods import GenericMethods
from pageObjects.ProjectMethods import ProjectMethods
from dotenv import load_dotenv

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
        self.gm.createMethod("Category_Tab","Add_Category_btn","Name","Save_btn",module_name="categories",sheet_name="Create Category",row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_002_Create_Category_With_Blank_Name",sheet_name="Create Category",row_num=3,col_num=1,exp="Fail")

    def test_003_Create_Category_With_Valid_Name(self):
        self.gm.createMethod("Name","Save_btn",module_name="categories",sheet_name="Create Category",row_num=3)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_003_Create_Category_With_Valid_Name",sheet_name="Create Category",row_num=3,col_num=1,exp="Pass")

    def test_005_Update_Category_With_Blank_Category_Name(self):
        self.gm.updateMethod("Edit_btn", "Name", "Save_btn", data="Test", module_name="categories",sheet_name="Update Category", row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_005_Update_Category_With_Blank_Category_Name",sheet_name="Update Category", row_num=3, col_num=1, exp="Fail")

    def test_006_Update_Category_With_Valid_Category_Name(self):
        self.gm.updateMethod("Name", "Save_btn", "Category_Tab", data="Test", module_name="categories",sheet_name="Update Category", row_num=3)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_006_Update_Category_With_Valid_Category_Name",sheet_name="Update Category", row_num=3, col_num=1, exp="Pass")

    def test_007_Delete_Category(self):
        self.gm.deleteMethod(data="Test",module_name="categories",ssname="test_007_Delete_Category")

    # def test_008_Search_Valid_User(self):
    #     self.cp.searchVerificationMethodValid("About Us")
    #
    # def test_009_Search_Invalid_User(self):
    #     self.cp.searchVerificationMethodInValid()

