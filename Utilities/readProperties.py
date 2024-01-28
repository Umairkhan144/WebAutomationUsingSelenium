# Here we will import configparser through which we will parse value from config.ini file to our testcases files
import configparser
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

config = configparser.RawConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
config_dir = BASE_DIR / "Configurations"
# Here we are using configparser to read our config.ini files
config.read(f'{config_dir}/config.ini')


class ReadConfig():
    # Here we are creating a static methods thorough which we can get this data in our main testcase file
    @staticmethod  # Staticmethod is useful now we don't need to create an object of this class to call this method
    def getbaseURl():
        url = config.get('admin credentials', 'baseURl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('admin credentials', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('admin credentials', 'password')
        return password

    @staticmethod
    def getImage():
        password = config.get('admin credentials', 'img')
        return password

    @staticmethod
    def getSearchText():
        password = config.get('admin credentials', 'searchText')
        return password
    @staticmethod
    def getEmailLV():
        element = config.get('Login Page', 'emailLV')
        return element

    @staticmethod
    def getEmailLT():
        element = config.get('Login Page', 'emailLT')
        return element

    @staticmethod
    def getPasswordLV():
        element = config.get('Login Page', 'passwordLV')
        return element

    @staticmethod
    def getPasswordLT():
        element = config.get('Login Page', 'passwordLT')
        return element

    @staticmethod
    def getLoginBtnLV():
        element = config.get('Login Page', 'loginBtnLV')
        return element

    @staticmethod
    def getLoginBtnLT():
        element = config.get('Login Page', 'loginBtnLT')
        return element

    # --------------------- Dashboard Locators Method ---------------------

    @staticmethod
    def getDashboardTabLV():
        element = config.get('Dashboard', 'dashboardTabLV')
        return element

    @staticmethod
    def getDashboardTabLT():
        element = config.get('Dashboard', 'dashboardTabLT')
        return element

    @staticmethod
    def getUserTabLV():
        element = config.get('Dashboard', 'userTabLV')
        return element

    @staticmethod
    def getUserTabLT():
        element = config.get('Dashboard', 'userTabLT')
        return element

# --------------------- User Form Locators Methods ---------------------

    @staticmethod
    def getAddUserBtnLV():
        element = config.get('User Form', 'addUserBtnLV')
        return element

    @staticmethod
    def getAddUserBtnLT():
        element = config.get('User Form', 'addUserBtnLT')
        return element

    @staticmethod
    def getUserNameFieldLV():
        element = config.get('User Form', 'userNameFieldLV')
        return element

    @staticmethod
    def getUserNameFieldLT():
        element = config.get('User Form', 'userNameFieldLT')
        return element

    @staticmethod
    def getUserEmailFieldLV():
        element = config.get('User Form', 'userEmailFieldLV')
        return element

    @staticmethod
    def getUserEmailFieldLT():
        element = config.get('User Form', 'userEmailFieldLT')
        return element

    @staticmethod
    def getUserPhoneFieldLV():
        element = config.get('User Form', 'userPhoneFieldLV')
        return element

    @staticmethod
    def getUserPhoneFieldLT():
        element = config.get('User Form', 'userPhoneFieldLT')
        return element

    @staticmethod
    def getUserAddressFieldLV():
        element = config.get('User Form', 'userAddressFieldLV')
        return element

    @staticmethod
    def getUserAddressFieldLT():
        element = config.get('User Form', 'userAddressFieldLT')
        return element

    @staticmethod
    def getUserPasswordFieldLV():
        element = config.get('User Form', 'userPasswordFieldLV')
        return element

    @staticmethod
    def getUserPasswordFieldLT():
        element = config.get('User Form', 'userPasswordFieldLT')
        return element

    @staticmethod
    def getProfilePicFieldLV():
        element = config.get('User Form', 'userProfilePicLV')
        return element

    @staticmethod
    def getProfilePicFieldLT():
        element = config.get('User Form', 'userProfilePicLT')
        return element

    @staticmethod
    def getUserSaveBtnLV():
        element = config.get('User Form', 'userSaveBtnLV')
        return element

    @staticmethod
    def getUserSaveBtnLT():
        element = config.get('User Form', 'userSaveBtnLT')
        return element

    @staticmethod
    def getUserResetBtnLV():
        element = config.get('User Form', 'userResetBtnLV')
        return element

    @staticmethod
    def getUserResetBtnLT():
        element = config.get('User Form', 'userResetBtnLT')
        return element

    @staticmethod
    def getEditUserBtnLV():
        element = config.get('User Form', 'editBtnLV')
        return element

    @staticmethod
    def getEditUserBtnLT():
        element = config.get('User Form', 'editBtnLT')
        return element

    @staticmethod
    def getUpdateUserBtnLV():
        element = config.get('User Form', 'updateBtnLV')
        return element

    @staticmethod
    def getUpdateUserBtnLT():
        element = config.get('User Form', 'updateBtnLT')
        return element

    @staticmethod
    def getDeleteUserBtnLV():
        element = config.get('User Form', 'deleteBtnLV')
        return element

    @staticmethod
    def getDeleteUserBtnLT():
        element = config.get('User Form', 'deleteBtnLT')
        return element

    @staticmethod
    def getConfirmDeleteUserBtnLV():
        element = config.get('User Form', 'confirmDeleteBtnLV')
        return element

    @staticmethod
    def getConfirmDeleteUserBtnLT():
        element = config.get('User Form', 'confirmDeleteBtnLT')
        return element

    @staticmethod
    def getSearchFieldLV():
        element = config.get('User Form', 'searchFieldLV')
        return element

    @staticmethod
    def getSearchFieldLT():
        element = config.get('User Form', 'searchFieldLT')
        return element

# ------------------- Category Form Locators Methods -----------------------

    @staticmethod
    def getCategoriesTabLV():
        element = config.get('Categories Form', 'CategoriesTabLV')
        return element

    @staticmethod
    def getCategoriesTabLT():
        element = config.get('Categories Form', 'CategoriesTabLT')
        return element

    @staticmethod
    def getAddCategoriesBtnLV():
        element = config.get('Categories Form', 'addCategoryBtnLV')
        return element

    @staticmethod
    def getAddCategoriesBtnLT():
        element = config.get('Categories Form', 'addCategoryBtnLT')
        return element

    @staticmethod
    def getCategoriesNameFieldLV():
        element = config.get('Categories Form', 'categoryNameFieldLV')
        return element

    @staticmethod
    def getCategoriesNameFieldLT():
        element = config.get('Categories Form', 'categoryNameFieldLT')
        return element

    @staticmethod
    def getSaveCategoriesBtnLV():
        element = config.get('Categories Form', 'saveCategoryBtnLV')
        return element

    @staticmethod
    def getSaveCategoriesBtnLT():
        element = config.get('Categories Form', 'saveCategoryBtnLT')
        return element

    @staticmethod
    def getResetCategoriesBtnLV():
        element = config.get('Categories Form', 'resetCategoryBtnLV')
        return element

    @staticmethod
    def getResetCategoriesBtnLT():
        element = config.get('Categories Form', 'resetCategoryBtnLT')
        return element

    @staticmethod
    def getEditCategoriesBtnLV():
        element = config.get('Categories Form', 'editCategoryBtnLV')
        return element

    @staticmethod
    def getEditCategoriesBtnLT():
        element = config.get('Categories Form', 'editCategoryBtnLT')
        return element

    @staticmethod
    def getDeleteCategoriesBtnLV():
        element = config.get('Categories Form', 'deleteCategoryBtnLV')
        return element

    @staticmethod
    def getDeleteCategoriesBtnLT():
        element = config.get('Categories Form', 'deleteCategoryBtnLT')
        return element

# --------------------- Pages Form Locators Methods -----------------------------
    @staticmethod
    def getPagesTabLV():
        element = config.get('Pages Form', 'pagesTabLV')
        return element

    @staticmethod
    def getPagesTabLT():
        element = config.get('Pages Form', 'pagesTabLT')
        return element

    @staticmethod
    def getAddPageBtnLV():
        element = config.get('Pages Form', 'addPageBtnLV')
        return element

    @staticmethod
    def getAddPageBtnLT():
        element = config.get('Pages Form', 'addPageBtnLT')
        return element

    @staticmethod
    def getTitleFieldLV():
        element = config.get('Pages Form', 'titleFieldLV')
        return element

    @staticmethod
    def getTitleFieldLT():
        element = config.get('Pages Form', 'titleFieldLT')
        return element

    @staticmethod
    def getSlugFieldLV():
        element = config.get('Pages Form', 'slugFieldLV')
        return element

    @staticmethod
    def getSlugFieldLT():
        element = config.get('Pages Form', 'slugFieldLT')
        return element

    @staticmethod
    def getContentFieldLV():
        element = config.get('Pages Form', 'contentFieldLV')
        return element

    @staticmethod
    def getContentFieldLT():
        element = config.get('Pages Form', 'contentFieldLT')
        return element

    @staticmethod
    def getPageSaveBtnLV():
        element = config.get('Pages Form', 'pageSaveBtnLV')
        return element

    @staticmethod
    def getPageSaveBtnLT():
        element = config.get('Pages Form', 'pageSaveBtnLT')
        return element

    @staticmethod
    def getEditPageBtnLV():
        element = config.get('Pages Form', 'editPageBtnLV')
        return element

    @staticmethod
    def getEditPageBtnLT():
        element = config.get('Pages Form', 'editPageBtnLT')
        return element

    @staticmethod
    def getDeletePageBtnLV():
        element = config.get('Pages Form', 'deletePageBtnLV')
        return element

    @staticmethod
    def getDeletePageBtnLT():
        element = config.get('Pages Form', 'deletePageBtnLT')
        return element

# --------------------- Pages Form Locators Methods -----------------------------
    @staticmethod
    def getProductTabLV():
        element = config.get('Products Form', 'productTabLV')
        return element

    @staticmethod
    def getProductTabLT():
        element = config.get('Products Form', 'productTabLT')
        return element

    @staticmethod
    def getAddProductBtnLV():
        element = config.get('Products Form', 'addProductBtnLV')
        return element

    @staticmethod
    def getAddProductBtnLT():
        element = config.get('Products Form', 'addProductBtnLT')
        return element

    @staticmethod
    def getProductNameFieldLV():
        element = config.get('Products Form', 'productNameFieldLV')
        return element

    @staticmethod
    def getProductNameFieldLT():
        element = config.get('Products Form', 'productNameFieldLT')
        return element

    @staticmethod
    def getProductCategoryFieldLV():
        element = config.get('Products Form', 'productCategoryFiledLV')
        return element

    @staticmethod
    def getProductCategoryFieldLT():
        element = config.get('Products Form', 'productCategoryFiledLT')
        return element

    @staticmethod
    def getProductStoreFieldLV():
        element = config.get('Products Form', 'productStoreFieldLV')
        return element

    @staticmethod
    def getProductStoreFieldLT():
        element = config.get('Products Form', 'productStoreFieldLT')
        return element

    @staticmethod
    def getProductColorFieldLV():
        element = config.get('Products Form', 'productColorFieldLV')
        return element

    @staticmethod
    def getProductColorFieldLT():
        element = config.get('Products Form', 'productColorFieldLT')
        return element

    @staticmethod
    def getProductImageFieldLV():
        element = config.get('Products Form', 'productImageLV')
        return element

    @staticmethod
    def getProductImageFieldLT():
        element = config.get('Products Form', 'productImageLT')
        return element

    @staticmethod
    def getProductDescriptionFieldLV():
        element = config.get('Products Form', 'productDescriptionLV')
        return element

    @staticmethod
    def getProductDescriptionFieldLT():
        element = config.get('Products Form', 'productDescriptionLT')
        return element

    @staticmethod
    def getProductPriceFieldLV():
        element = config.get('Products Form', 'productPriceLV')
        return element

    @staticmethod
    def getProductPriceFieldLT():
        element = config.get('Products Form', 'productPriceLT')
        return element

    @staticmethod
    def getProductURLFieldLV():
        element = config.get('Products Form', 'productURLLV')
        return element

    @staticmethod
    def getProductURLFieldLT():
        element = config.get('Products Form', 'productURLLT')
        return element

    @staticmethod
    def getProductSaveBtnLV():
        element = config.get('Products Form', 'productSaveBtnLV')
        return element

    @staticmethod
    def getProductSaveBtnLT():
        element = config.get('Products Form', 'productSaveBtnLT')
        return element

    @staticmethod
    def getProductEditBtnLV():
        element = config.get('Products Form', 'productEditBtnLV')
        return element

    @staticmethod
    def getProductEditBtnLT():
        element = config.get('Products Form', 'productEditBtnLT')
        return element

    @staticmethod
    def getProductDeleteBtnLV():
        element = config.get('Products Form', 'productDeleteBtnLV')
        return element

    @staticmethod
    def getProductDeleteBtnLT():
        element = config.get('Products Form', 'productDeleteBtnLT')
        return element

