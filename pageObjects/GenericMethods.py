import time
from typing import re

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Utilities import XLUtilis
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
import json
from pathlib import Path

class GenericMethods(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cl = LogGen.loggen()
    searchFieldLV = ReadConfig.getSearchFieldLV()
    searchFieldLT = ReadConfig.getSearchFieldLT()
    BASE_DIR = Path(__file__).resolve().parent.parent
    config_dir = BASE_DIR / "Configurations"
    configFile = "configSaloon.json"
    excelFile = BASE_DIR / "testData"
    pathExcelfile = f'{excelFile}/TestDataSaloon.xlsx'

    # -------------------  Generic Methods------------------------
    def get_url(self):
        with open(f'{self.config_dir}/' + self.configFile) as f:
            data = json.load(f)

            for field in data["basic info"]['fields']:
                if field['name'] == 'URL':
                    return field['url']

            return None

    def createMethod(self, *fields, module_name, sheet_name, row_num):
        self.data = {}
        with open(f'{self.config_dir}/'+self.configFile+'') as f:
            self.data = json.load(f)

        col = XLUtilis.getColumnCount(self.pathExcelfile, sheet_name)

        for field in fields:
            field_attr_LV = None
            field_attr_LT = None
            field_attr_LV1 = None
            field_attr_LT1 = None
            field_type = None

            for field_data in self.data[module_name]["fields"]:
                if field_data["name"] == field:
                    field_type = field_data.get("type", None)
                    if field_type == "dropdown":
                        field_attr_LV = field_data["locatorLV"]
                        field_attr_LT = field_data["locatorLT"]
                        field_attr_LV1 = field_data["locatorLV1"]
                        field_attr_LT1 = field_data["locatorLT1"]
                    else:
                        field_attr_LV = field_data["locatorLV"]
                        field_attr_LT = field_data["locatorLT"]
                    break

            if field_attr_LV is not None and field_attr_LT is not None:
                if field_type == "button":
                    self.clickElement(field_attr_LV, field_attr_LT)
                    time.sleep(3)
                else:
                    for c in range(1, col + 1):
                        data = XLUtilis.readData(self.pathExcelfile, sheet_name, 1, c)
                        if data == field:
                            value = XLUtilis.readData(self.pathExcelfile, sheet_name, row_num, c)
                            if value is not None:
                                if field_type == "dropdown":
                                    self.setDropDown(value, field_attr_LV, field_attr_LT,field_attr_LV1,field_attr_LT1)
                                elif field_type == "image":
                                    self.setImage(value,field_attr_LV, field_attr_LT)
                                elif field_type == "autofill":
                                    self.setAutofill(value, field_attr_LV, field_attr_LT)
                                else:
                                    self.sendText(value, field_attr_LV, field_attr_LT)
                            else:
                                self.clearElement(field_attr_LV, field_attr_LT)
            else:
                self.cl.error(f"Field {field} not found in {module_name}")

    def deleteMethod(self,data,module_name,ssname):
        self.data = {}
        with open(f'{self.config_dir}/' + self.configFile) as f:
            self.data = json.load(f)

        element = None
        try:
            delete_btn_locatorLV = None
            delete_btn_locatorLT = None
            confirm_delete_locatorLV = None
            confirm_delete_locatorLT = None

            for field in self.data[module_name]["fields"]:
                if field["name"] == "Delete_btn":
                    delete_btn_locatorLV = field["locatorLV"].replace("{data}", data)
                    delete_btn_locatorLT = field["locatorLT"]
                elif field["name"] == "Confirm_Delete_btn":
                    confirm_delete_locatorLV = field["locatorLV"]
                    confirm_delete_locatorLT = field["locatorLT"]

                # Check if all values are set
                if (
                        delete_btn_locatorLV is not None
                        and delete_btn_locatorLT is not None
                        and confirm_delete_locatorLV is not None
                        and confirm_delete_locatorLT is not None
                ):
                    break

            if delete_btn_locatorLV is not None and delete_btn_locatorLT is not None:
                self.clickElement(delete_btn_locatorLV,delete_btn_locatorLT)
                self.clickElement(confirm_delete_locatorLV,confirm_delete_locatorLT)
            else:
                print(f"Field '{delete_btn_locatorLV}' not found.")
            element = self.getElement(delete_btn_locatorLV,delete_btn_locatorLT)
            if element is not None:
                self.takeScreenshot(ssname)
                self.log.error("Test Failed - Data is not Deleted Successfully")
                assert False
            else:
                self.log.info("Test Passed - Data is Deleted Successfully")
                assert True
        except Exception as e:
            print(f"An error occurred while deleting user: {str(e)}")

    def verifyDataIsAddedSuccessfully(self,ssname,sheet_name,row_num,col_num,exp):
        username = XLUtilis.readData(self.pathExcelfile, sheet_name, row_num, col_num)
        path = None
        if exp == "pass" or  exp == "Pass":
            path = "//table//tr[contains(., '"+username+"')]"
        self.element = None
        try:
            if exp == "pass" or exp == "Pass":
                self.element = self.getElement(path, "xpath")
                if self.element is not None:
                    self.log.info("Test Passed - Data is Added Successfully")
                    assert True
                else:
                    self.takeScreenshot(ssname)
                    self.log.error("Test Failed - Data is not Added Successfully")
                    assert False
            elif exp == "fail" or exp == "Fail":
                self.element = self.getElement(path, "xpath")
                if self.element is None:
                    self.log.info("Test Passed - Data is not Added Successfully")
                    assert True
                else:
                    self.takeScreenshot(ssname)
                    self.log.error("Test Failed - Data is Added Successfully")
                    assert False
        except Exception as e:
            print(f"An error occurred while deleting user: {str(e)}")

    def updateMethod(self, *fields, data, module_name, sheet_name, row_num):
        self.data = {}
        with open(f'{self.config_dir}/' + self.configFile + '') as f:
            self.data = json.load(f)

        col = XLUtilis.getColumnCount(self.pathExcelfile, sheet_name)

        for field in fields:
            field_attr_LV = None
            field_attr_LT = None
            field_attr_LV1 = None
            field_attr_LT1 = None
            field_type = None

            for field_data in self.data[module_name]["fields"]:
                if field_data["name"] == field:
                    field_type = field_data.get("type", None)
                    if field_type == "dropdown":
                        field_attr_LV = field_data["locatorLV"]
                        field_attr_LT = field_data["locatorLT"]
                        field_attr_LV1 = field_data["locatorLV1"]
                        field_attr_LT1 = field_data["locatorLT1"]
                    else:
                        field_attr_LV = field_data["locatorLV"].replace("{data}", data)
                        field_attr_LT = field_data["locatorLT"]
                    break

            if field_attr_LV is not None and field_attr_LT is not None:
                if field_type == "button":
                    self.clickElement(field_attr_LV, field_attr_LT)
                else:
                    for c in range(1, col + 1):
                        data = XLUtilis.readData(self.pathExcelfile, sheet_name, 1, c)
                        if data == field:
                            value = XLUtilis.readData(self.pathExcelfile, sheet_name, row_num, c)
                            if value is not None:
                                if field_type == "dropdown":
                                    self.setDropDown(value, field_attr_LV, field_attr_LT, field_attr_LV1,
                                                     field_attr_LT1)
                                elif field_type == "image":
                                    self.setImage(value, field_attr_LV, field_attr_LT)
                                elif field_type == "autofill":
                                    self.setAutofill(value, field_attr_LV, field_attr_LT)
                                else:
                                    self.sendText(value, field_attr_LV, field_attr_LT)
                            else:
                                self.clearElement(field_attr_LV, field_attr_LT)
            else:
                self.cl.error(f"Field {field} not found in {module_name}")

    def verifyFieldNotEmpty(self, *fields, module_name, sheet_name, row_num):
        self.data = {}
        result = []
        with open(f'{self.config_dir}/'+self.configFile+'') as f:
            self.data = json.load(f)

        col = XLUtilis.getColumnCount(self.pathExcelfile, sheet_name)

        for field in fields:
            field_attr_LV = None
            field_attr_LT = None
            field_attr_LV1 = None
            field_attr_LT1 = None
            field_type = None

            for field_data in self.data[module_name]["fields"]:
                if field_data["name"] == field:
                    field_type = field_data.get("type", None)
                    if field_type == "dropdown":
                        field_attr_LV = field_data["locatorLV"]
                        field_attr_LT = field_data["locatorLT"]
                        field_attr_LV1 = field_data["locatorLV1"]
                        field_attr_LT1 = field_data["locatorLT1"]
                    else:
                        field_attr_LV = field_data["locatorLV"]
                        field_attr_LT = field_data["locatorLT"]
                    break

            if field_attr_LV is not None and field_attr_LT is not None:
                if field_type == "button":
                    self.clickElement(field_attr_LV, field_attr_LT)
                    time.sleep(3)
                else:
                    for c in range(1, col + 1):
                        data = XLUtilis.readData(self.pathExcelfile, sheet_name, 1, c)
                        if data == field:
                            value = XLUtilis.readData(self.pathExcelfile, sheet_name, row_num, c)
                            if value is not None:
                                if field_type == "dropdown":
                                    self.setDropDown(value, field_attr_LV, field_attr_LT, field_attr_LV1,
                                                     field_attr_LT1)
                                elif field_type == "image":
                                    self.setImage(value, field_attr_LV, field_attr_LT)
                                elif field_type == "autofill":
                                    self.setAutofill(value, field_attr_LV, field_attr_LT)
                                else:
                                    self.sendText(value, field_attr_LV, field_attr_LT)
                                    text = self.getText(field_attr_LV, field_attr_LT)
                                    if field_type == "alphabets":
                                        if text.isalpha() or text is None:
                                            result.append("pass")
                                            self.cl.info(f"Field '{text}' contains only alphabets.")
                                        else:
                                            result.append("fail")
                                            self.cl.info(f"Field '{text}' does not contain only alphabets.")

                                    elif field_type == "alphanumeric":
                                        if text.isalnum() or text is None:
                                            result.append("pass")
                                            self.cl.info(f"Field '{text}' contains only alphanumeric characters.")
                                        else:
                                            result.append("fail")
                                            self.cl.info(
                                                f"Field '{text}' does not contain only alphanumeric characters.")

                                    elif field_type == "email":
                                        if re.match(r"[^@]+@[^@]+\.[^@]+", text):
                                            result.append("pass")
                                            self.cl.info(f"Field '{text}' contains a valid email address.")
                                        else:
                                            result.append("fail")
                                            self.cl.info(f"Field '{text}' does not contain a valid email address.")

                                    else:
                                        result.append("pass")
                                        self.cl.info(
                                            f"Skipping field '{text}' as its type '{field_type}' is not supported.")

                            else:
                                self.clearElement(field_attr_LV, field_attr_LT)
            else:
                self.cl.error(f"Field {field} not found in {module_name}")

            if "fail" in result:
                self.cl.error("Test Failed")
                assert False
            else:
                assert True
