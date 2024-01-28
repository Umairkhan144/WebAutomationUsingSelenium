import unittest
import pytest
from Utilities.customLogger import LogGen
import time
from pageObjects.ProductPage import ProductPage
from pageObjects.ProjectMethods import ProjectMethods
from pageObjects.GenericMethods import GenericMethods
from dotenv import load_dotenv
load_dotenv()

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ProductFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.logger = LogGen.loggen()
        self.pp = ProductPage(self.driver)
        self.gm = GenericMethods(self.driver)
        self.pm = ProjectMethods(self.driver)

    def test_001_login(self):
        url = self.gm.get_url()
        self.driver.get(url)
        self.gm.createMethod("Email", "Password", "login btn", module_name="login", sheet_name="Login", row_num=9)
        self.pm.verifyUserLoggedIN("Pass", "test_001_login_valid")

    def test_004_Add_Product_With_All_Fields_Blank(self):
        self.gm.createMethod("products tab","add product btn","Name", "Category", "Store", "Color", "Description", "Image", "Save_btn",module_name="products", row_num=2, sheet_name="Create Product")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_004_Add_Product_With_All_Fields_Blank",sheet_name="Create Product",row_num=2,col_num=1,exp="fail")

    def test_005_Add_Product_With_Name_Field_Blank(self):
        self.gm.createMethod("Name", "Category", "Store", "Color", "Description", "Image","Save_btn", module_name="products", row_num=3, sheet_name="Create Product")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_005_Add_Product_With_Name_Field_Blank",sheet_name="Create Product",row_num=3,col_num=1,exp="fail")

    def test_006_Add_Product_With_Category_Field_Blank(self):
        self.gm.refreshPage()
        self.gm.createMethod("Name", "Category", "Store", "Color", "Description", "Image", "Save_btn",module_name="products", row_num=4, sheet_name="Create Product")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_006_Add_Product_With_Category_Field_Blank",sheet_name="Create Product",row_num=4,col_num=1,exp="fail")


    def test_007_Add_Product_With_Store_Field_Blank(self):
        self.gm.refreshPage()
        self.gm.createMethod("Name", "Category", "Store", "Color", "Description", "Image", "Save_btn", module_name="products", row_num=5, sheet_name="Create Product")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_007_Add_Product_With_Store_Field_Blank",sheet_name="Create Product",row_num=5,col_num=1,exp="fail")


    def test_008_Add_Product_With_Color_Field_Blank(self):
        self.gm.refreshPage()
        self.gm.createMethod("Name", "Category", "Store", "Color", "Description", "Image", "Save_btn", module_name="products", row_num=6, sheet_name="Create Product")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_008_Add_Product_With_Color_Field_Blank",sheet_name="Create Product",row_num=6,col_num=1,exp="fail")


    def test_009_Add_Product_With_Image_Field_Blank(self):
        self.gm.refreshPage()
        self.gm.createMethod("Name", "Category", "Store", "Color", "Description", "Image", "Save_btn",module_name="products", row_num=7, sheet_name="Create Product")
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_009_Add_Product_With_Image_Field_Blank",sheet_name="Create Product",row_num=7,col_num=1,exp="fail")


    def test_010_Add_Product_With_All_Valid_Data(self):
        self.gm.refreshPage()
        self.gm.createMethod("Name", "Category", "Store", "Color", "Description", "Image", "Save_btn", module_name="products", row_num=8, sheet_name="Create Product")
        time.sleep(10)
        self.gm.verifyDataIsAddedSuccessfully(ssname="test_010_Add_Product_With_All_Valid_Data",sheet_name="Create Product",row_num=8,col_num=1,exp="fail")

    # --------------------------- Delete Test Cases ---------------------------
    def test_011_Delete_New_Created_Product(self):
        self.gm.deleteMethod("Test Product","products","test_011_Delete_New_Created_Product")
