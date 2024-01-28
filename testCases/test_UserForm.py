import os
import unittest
from pathlib import Path
import pytest
from pageObjects.GenericMethods import GenericMethods
from Utilities.readProperties import ReadConfig
from pageObjects.ProjectMethods import ProjectMethods
from Utilities.customLogger import LogGen
import time
from pageObjects.UsersPage import UserPage
from dotenv import load_dotenv
load_dotenv()

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class UserFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.logger = LogGen.loggen()
        self.up = UserPage(self.driver)
        self.gm = GenericMethods(self.driver)
        self.pm = ProjectMethods(self.driver)

    def test_001_login(self):
        url = self.gm.get_url()
        self.driver.get(url)
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=9)
        self.pm.verifyUserLoggedIN("Pass", "test_001_login_valid")

    def test_003_Create_New_User_with_All_Fields_Blank(self):
        self.gm.createMethod("users tab","add user btn","Name","Email","Phone","Address","Password","Save_btn",module_name="users",row_num=2,sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_003_Create_New_User_with_All_Fields_Blank",sheet_name="Create User",row_num=2,col_num=1,exp="fail")

    def test_004_Create_New_User_with_Name_Field_Blank(self):
        self.gm.createMethod("Name","Email","Phone","Address","Password","Save_btn",module_name="users",row_num=3,sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_004_Create_New_User_with_Name_Field_Blank",sheet_name="Create User",row_num=3,col_num=1,exp="fail")

    def test_005_Create_New_User_with_Email_Field_Blank(self):
        self.gm.createMethod("Name","Email","Phone","Address","Password","Save_btn",module_name="users",row_num=4,sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_005_Create_New_User_with_Email_Field_Blank",sheet_name="Create User",row_num=4,col_num=1,exp="fail")

    def test_006_Create_New_User_with_Phone_Field_Blank(self):
        self.gm.createMethod("Name","Email","Phone","Address","Password","Save_btn",module_name="users",row_num=5,sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_006_Create_New_User_with_Phone_Field_Blank",sheet_name="Create User",row_num=5,col_num=1,exp="fail")

    def test_007_Create_New_User_with_Address_Field_Blank(self):
        self.gm.createMethod("Name","Email","Phone","Address","Password","Save_btn",module_name="users",row_num=6,sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_007_Create_New_User_with_Address_Field_Blank",sheet_name="Create User",row_num=6,col_num=1,exp="fail")

    def test_008_Create_New_User_with_Password_Field_Blank(self):
        self.gm.createMethod("Name","Email","Phone","Address","Password","Save_btn",module_name="users",row_num=7,sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_008_Create_New_User_with_Password_Field_Blank",sheet_name="Create User",row_num=7,col_num=1,exp="fail")

    def test_009_Create_New_User_with_Valid_Data(self):
        self.gm.createMethod("Name","Email","Phone","Address","Password","Image","Save_btn",module_name="users",row_num=8,sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_009_Create_New_User_with_Valid_Data",sheet_name="Create User",row_num=8,col_num=1,exp="pass")

    # ---------------- Update User Test Cases --------------

    def test_009_Edit_New_Created_User_With_All_Fields_Blank(self):
        self.gm.updateMethod("edit btn", "Name", "Email", "Phone", "Address", "Password", "Update_btn", data="Test",module_name="users", row_num=2, sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_009_Edit_New_Created_User_With_All_Fields_Blank",sheet_name="Update User", row_num=2, col_num=1, exp="fail")

    def test_010_Edit_New_Created_User_With_Name_Field_Blank(self):
        self.gm.updateMethod("edit btn", "Name", "Email", "Phone", "Address", "Password", "Update_btn", data="Test",module_name="users", row_num=3, sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_010_Edit_New_Created_User_With_Name_Field_Blank",sheet_name="Update User", row_num=3, col_num=1, exp="fail")

    def test_011_Edit_New_User_with_Email_Field_Blank(self):
        self.gm.updateMethod("edit btn", "Name", "Email", "Phone", "Address", "Password", "Update_btn", data="Test",module_name="users", row_num=4, sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_011_Edit_New_User_with_Email_Field_Blank",sheet_name="Update User", row_num=4, col_num=1, exp="fail")

    def test_012_Edit_New_User_with_Phone_Field_Blank(self):
        self.gm.updateMethod("edit btn", "Name", "Email", "Phone", "Address", "Password", "Update_btn", data="Test",module_name="users", row_num=5, sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_012_Edit_New_User_with_Phone_Field_Blank", sheet_name="Update User", row_num=5, col_num=1, exp="fail")

    def test_013_Edit_New_User_with_Address_Field_Blank(self):
        self.gm.updateMethod("edit btn", "Name", "Email", "Phone", "Address", "Password", "Update_btn", data="Test", module_name="users", row_num=6, sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_013_Edit_New_User_with_Address_Field_Blank", sheet_name="Update User", row_num=6, col_num=1, exp="fail")

    def test_014_Edit_New_User_with_Password_Field_Blank(self):
        self.gm.updateMethod("edit btn", "Name", "Email", "Phone", "Address", "Password", "Update_btn", data="Test", module_name="users", row_num=7, sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_014_Edit_New_User_with_Password_Field_Blank", sheet_name="Update User", row_num=7, col_num=1, exp="fail")

    def test_015_Edit_New_User_with_Valid_Data(self):
        self.gm.updateMethod("edit btn", "Name", "Email", "Phone", "Address", "Password", "Update_btn","users tab", data="Test", module_name="users", row_num=8, sheet_name="Create User")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_015_Edit_New_User_with_Valid_Data", sheet_name="Update User", row_num=8, col_num=1, exp="fail")

    def test_016_Delete_New_Created_user(self):
        self.gm.deleteMethod("test1@yopmail.com","users","test_016_Delete_New_Created_user")

#     def test_017_Search_Valid_User(self):
#         self.up.searchVerifcationMethodValid("Samih")
#
#     def test_018_Search_Invalid_User(self):
#         self.up.searchVerifcationMethodInValid()



