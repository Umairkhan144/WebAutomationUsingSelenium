import os
import unittest
from pathlib import Path
import pytest
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time
from pageObjects.GenericMethods import GenericMethods
from pageObjects.ProjectMethods import ProjectMethods
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class PagesFormTest(unittest.TestCase):
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

    def test_004_Create_New_Page_With_All_Fields_Blank(self):
        self.gm.createMethod("pages tab", "add page btn", "Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Create Page", row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_004_Create_New_Page_With_All_Fields_Blank",sheet_name="Create Page", row_num=2, col_num=1, exp="Fail")

    def test_005_Create_New_Page_With_Name_Fields_Blank(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Create Page", row_num=3)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_005_Create_New_Page_With_Name_Fields_Blank",sheet_name="Create Page", row_num=3, col_num=1, exp="Fail")


    def test_006_Create_New_Page_With_Slug_Fields_Blank(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Create Page", row_num=4)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_006_Create_New_Page_With_Slug_Fields_Blank",sheet_name="Create Page", row_num=4, col_num=1, exp="Fail")

    def test_007_Create_New_Page_With_Content_Field_Blank(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Create Page", row_num=5)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_007_Create_New_Page_With_Content_Field_Blank",sheet_name="Create Page", row_num=5, col_num=1, exp="Fail")


    def test_008_Create_New_Page_With_NameAndSlug_Field_Blank(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Create Page", row_num=6)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_008_Create_New_Page_With_NameAndSlug_Field_Blank",sheet_name="Create Page", row_num=6, col_num=1, exp="Fail")


    def test_009_Create_New_Page_With_All_Valid_Data(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Create Page", row_num=7)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_009_Create_New_Page_With_All_Valid_Data",sheet_name="Create Page", row_num=7, col_num=1, exp="pass")


    def test_010_Update_Page_With_All_Fields_Blank(self):
        self.gm.updateMethod("Edit_btn","Title","Slug","Content", "Save_btn",data="Test", module_name="pages",sheet_name="Update Page", row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_010_Update_Page_With_All_Fields_Blank",sheet_name="Update Page", row_num=2, col_num=1, exp="Fail")


    def test_011_Update_Page_With_Name_Field_Blank(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Update Page", row_num=3)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_011_Update_Page_With_Name_Field_Blank",sheet_name="Update Page", row_num=3, col_num=1, exp="Fail")


    def test_012_Update_New_Page_With_Slug_Fields_Blank(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Update Page", row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_002_Create_Category_With_Blank_Name",sheet_name="Update Page", row_num=3, col_num=1, exp="Fail")


    def test_013_Update_New_Page_With_Content_Field_Blank(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",
                             sheet_name="Update Page", row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_002_Create_Category_With_Blank_Name",
                                              sheet_name="Update Page", row_num=3, col_num=1, exp="Fail")


    def test_014_Update_New_Page_With_NameAndSlug_Field_Blank(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",
                             sheet_name="Update Page", row_num=2)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_002_Create_Category_With_Blank_Name",
                                              sheet_name="Update Page", row_num=3, col_num=1, exp="Fail")


    def test_015_Update_New_Page_With_All_Valid_Data(self):
        self.gm.createMethod("Title","Slug","Content", "Save_btn", module_name="pages",sheet_name="Update Page", row_num=7)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_015_Update_New_Page_With_All_Valid_Data",sheet_name="Update Page", row_num=7, col_num=1, exp="Pass")


    def test_016Delete_Page(self):
        self.gm.deleteMethod(data="Test",module_name="pages",ssname="test_016Delete_Page")


    # def test_017_Search_Valid_User(self):
    #     self.pp.searchVerifcationMethodValid("About Us")
    #
    # def test_018_Search_Invalid_User(self):
    #     self.pp.searchVerifcationMethodInValid()

