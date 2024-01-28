import os
import unittest
import pytest
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.GenericMethods import GenericMethods
import time
from pageObjects.UsersPage import UserPage
from pageObjects.CategoryPage import CategoryPage
from pageObjects.ProductPage import ProductPage
from dotenv import load_dotenv
load_dotenv()

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class UserFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ap = Login(self.driver)
        self.logger = LogGen.loggen()
        self.up = UserPage(self.driver)
        self.cp = CategoryPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.gm = GenericMethods(self.driver)

    # This is our data which we are using in our Login Test case
    # coming from config.ini file using readProperties Methods form Utilities Package
    baseURL = ReadConfig.getbaseURl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    pathUserCreation = f"{os.getenv('ROOT_DIR')}testData/Testdatauser.xlsx"

    def test_001_login(self):
        # Here we are setting driver from conftest.py class to here. Using @pytest.fixtures
        self.logger.info(" ------- Test Case 001 - Login Test -------")
        self.logger.info(" ------- Verifying Login with valid Credentiasl -------")

        # Here using driver our first command will execute to open the perticular site.
        self.driver.get(self.baseURL)

        # Here we are calling the methods and passing values to driver which we created in LoginPage of objectPages.
        self.ap.setUsername(self.username)
        self.ap.setPassword(self.password)
        self.ap.clickLogin()
        # This command is for the hold the browser to move to next command
        time.sleep(3)
        # Here we are getting the title of the page and comparing to expected and will check if test passed or failed.
        hometitle = self.driver.title
        exptitle = "Price Comparison"

        if hometitle == exptitle:
            # If both will be same our test case will be passed
            self.logger.info(" ------- Test Case 001 - Test Passed -------")
            assert True
        else:
            # If both will not be equal test case will fail.
            self.driver.save_screenshot(
                "/Users/mac/PycharmProjects/TekrevolAutomationProjectWebApps/TekrevolAutomationWebApp/Screenshots/" + "test_login.png")
            self.logger.error(" ------- Test Case 001 - Test Failed -------")
            assert False

    def test_002_Redirect_To_UserForms(self):
        # self.up.clickSideOptions()
        self.up.clickUserTab()
        self.gm.deleteMethod("love@yopmail.com",module_name="users",ssname="test")
        # self.up.clickAddUserBtn()
        time.sleep(3)

    # def test_003_Create_New_User_with_All_Fields_Blank(self):
    #     self.up.formFillMethod("Name","Email","Phone","Address","Password","Save_btn",module_name="users"
    #                            ,row_num=2,sheet_name="Users Form Create",pathSignup=self.pathUserCreation)
    #     self.up.verifyUserIsNotCreated("test_003_Create_New_User_with_All_Fields_Blank")
    #
    # def test_004_Create_New_User_with_Name_Field_Blank(self):
    #     self.up.formFillMethod("Name","Email","Phone","Address","Password","Save_btn",module_name="users"
    #                            ,row_num=8,sheet_name="Users Form Create",pathSignup=self.pathUserCreation)
    #     self.up.verifyUserCreatedSuccessfully(self.pathUserCreation,"Users Form Crete",8)
    #
    # def test_005_Redirect_To_Category_Page(self):
    #     self.cp.clickCategoriesTab()
    #     self.cp.clickAddCategoryBtn()
    #     time.sleep(3)
    #
    # def test_006_Create_New_Cataegory_With_All_Fields_Blank(self):
    #     self.up.formFillMethod("Name","Save_btn",module_name="categories",row_num=2,sheet_name="Create Category",pathSignup=self.pathUserCreation)
    #     # self.cp.clickSaveCategoryBtn()
    #
    # def test_007_Create_New_Category_With_Valid_Data(self):
    #     self.up.formFillMethod("Name","Save_btn", module_name="categories", row_num=3,
    #                            sheet_name="Create Category",pathSignup=self.pathUserCreation)
    #     # self.cp.clickSaveCategoryBtn()
    #
    # def test_008_Redirect_To_Products_Page(self):
    #     self.pp.clickProductTab()
    #
    # def test_009_Open_Product_Form(self):
    #     self.pp.clickAddProductBtn()
    #
    # def test_010_Create_Product_With_All_Fields_Blank(self):
    #     self.up.formFillMethod("Name","Category","Store","Color","Description","Save_btn", module_name="products", row_num=2,
    #                            sheet_name="Create Product",pathSignup=self.pathUserCreation)
    #     time.sleep(5)
