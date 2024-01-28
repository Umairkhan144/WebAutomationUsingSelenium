import json

import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Utilities.customLogger import LogGen
import time
import string
import random
import os
from dotenv import load_dotenv
load_dotenv()

class BasePage:
    log = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def clickSideOptions(self):
        self.clickElement("//button[@id='kt_aside_mobile_toggler']","xpath")

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(By.ID,locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(By.CLASS_NAME,locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(By.ANDROID_UIAUTOMATOR, 'UiSelector().descriptionContains("' + locatorvalue + '")'))
            # element = wait.until(lambda x: x.find_element(By.XPATH, locatorvalue))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(By.ANDROID_UIAUTOMATOR, "UiSelector().index("+locatorvalue+")"))
            return element
        elif locatorType == "text":
            #element = wait.until(lambda x: x.find_element(By.ANDROID_UIAUTOMATOR, 'text("'+locatorvalue+'")'))
            element = wait.until(lambda x: x.find_element(By.ANDROID_UIAUTOMATOR, 'textContains("' + locatorvalue + '")'))  # //*[text()[contains(.,'ABC')]]
            return element
        elif locatorType == "xpathdes":
            # element = wait.until(lambda x: x.find_element(By.XPATH,"//*[contains((@text(),'"+locatorvalue+"') or (@content-desc(),'"+locatorvalue+"'))]"))
            element = wait.until(lambda x: x.find_element(By.XPATH, "//*[contains(@text,'"+locatorvalue+"') or contains(@content-desc,'"+locatorvalue+"')]"))
            if element is not None:
                self.log.info(
                    "Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorvalue)
                return element
            else:
                self.log.info(
                    "Element not found with LocatorType: " + locatorType + " with the locatorValue :" + locatorvalue)
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(By.XPATH,locatorvalue))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + " not found")
        return element

    def getElement(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue)
            return element
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def clearElement(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            element.clear()
            self.log.info(
                "Element Text Cleared with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to clear Element Text with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def clickElement(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def sendText(self, text, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            element.clear()
            element.send_keys(text)
            self.log.info(
                "Text '"+text+"' send on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def setAutofill(self, text, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.RETURN)
            self.log.info(
                "Text '"+text+"' send on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def setImage(self, text, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Text '"+text+"' send on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)


    def setDropDown(self,text, locatorValue, locatorType, locatorValue1, locatorType1):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            element1 = self.waitForElement(locatorValue1, locatorType1)
            element1.send_keys(text)
            element1.send_keys(Keys.RETURN)
            self.log.info(
                "Text '" + text + "' send on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def isDisplayed(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
            return True
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            return False

    def refreshPage(self):
        self.driver.refresh()

    # def screenShot(self, screenshotName):
    #     fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
    #     screenshotDirectory = "C:\\Users\\Umair\\PycharmProjects\\LinkFront\\Screenshots\\"
    #     screenshotPath = screenshotDirectory + fileName
    #     try:
    #         self.driver.save_screenshot(screenshotPath)
    #         self.log.info("Screenshot save to Path : " + screenshotPath)
    #
    #     except:
    #         self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, screenshotName):
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName, attachment_type=AttachmentType.PNG)
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = f"{os.getenv('ROOT_DIR')}Screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def backBtn(self):
        self.driver.back()



    def randomString(self):
        # initializing size of string
        N = 7
        # using random.choices() = generating random strings
        email = ''.join(random.choices(string.ascii_lowercase +
                                       string.digits, k=N))
        email = email + "@yopmail.com"
        return email

    def getTextLength(self,locatorValue,locatortype):
        element = self.waitForElement(locatorValue, locatortype)
        eltext = element.text
        realLength = len(eltext)
        return realLength

    def getText(self,locatorValue,locatortype):
        element = self.waitForElement(locatorValue, locatortype)
        eltext = element.text
        return eltext

    def getSplitLocatorValue(self,locatorType):
        x = locatorType.split(",")
        a = x[0]
        b = x[1]
        return a, b

    def scrolltoBottom(self,locatorValue):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        ele = wait.until(lambda x: x.find_element(By.ANDROID_UIAUTOMATOR,
                                                  'new UiScrollable(new UiSelector()).scrollIntoView(descriptionContains("'+locatorValue+'"))'))

    def scrolltoTop(self,locatorValue):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        ele = wait.until(lambda x: x.find_element(By.ANDROID_UIAUTOMATOR,
                                                  'new UiScrollable(new UiSelector()).scrollIntoView(textContains("'+locatorValue+'"))'))

    def SwipeTop(self):
        # out of print statement is :Device Width and Height :  {'width': 1440, 'height': 2621}
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']

        ###### Swipe from Bottom to Top  #######
        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 8 / 9
        endy = screenHeight / 9

        actions = TouchAction(self.driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

    def SwipeBottom(self):
        # out of print statement is :Device Width and Height :  {'width': 1440, 'height': 2621}
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']

        ###### Swipe from Top to Bottom #######
        startx2 = screenWidth / 2
        endx2 = screenWidth / 2
        starty2 = screenHeight * 2 / 9
        endy2 = screenHeight * 8 / 9

        actions = TouchAction(self.driver)
        actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()

    def SwipeRightToLeft(self):
        # out of print statement is :Device Width and Height :  {'width': 1440, 'height': 2621}
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']

        ###### Swipe from Top to Bottom #######
        startx = screenWidth * 2 / 9
        endx = screenWidth * 8 / 9
        starty = screenHeight / 2
        endy = screenHeight / 2

        actions = TouchAction(self.driver)
        actions.long_press(None, endx, starty).move_to(None, startx, endy).release().perform()

    def scrollScreenUp(self):
        touch = TouchAction(self.driver)
        touch.press(x=40,y=1800).move_to(x=40 , y=679).release().perform()

    def scrollScreenDown(self):
        touch = TouchAction(self.driver)
        touch.press(x=500,y=679).move_to(x=500 , y=1800).release().perform()

    def tapOnScreen(self):
        actions = TouchAction(self.driver)
        # actions.tap(None,700,1990,1)
        actions.tap(None, 20, 500, 1)
        actions.perform()

    def tapOnProfileTab(self):
        actions = TouchAction(self.driver)
        # actions.tap(None,700,1990,1)
        actions.tap(None, 980, 2136, 1)
        actions.perform()

##############################################################################################################
    def getUrl(self, URL):
        self.driver.get(URL)
        time.sleep(2)

    def update_jira_issues(self, ssname):
        with open(f"{self.BASE_DIR}/Configurations/jira_issues.json", "r") as output_file:
            json_data = json.load(output_file)

            filtered_array = [d for d in json_data if d.get("summary") != ssname]

        with open(f"{self.BASE_DIR}/Configurations/jira_issues.json", "w") as output_file:
            json_object = json.dumps(filtered_array, indent=4)
            output_file.write(str(json_object))

    def verifyFunction(self, exp, LVP=None, LTP=None, LVF=None, LTF=None, ssname=None):
        filtered_array = []

        if exp == "pass" or exp == "Pass":
            try:
                verify = self.getElement(LVP, LTP)
                if verify is not None:
                    self.log.info(">>>>>>>>>>>>>>>>>>>>>>>>> Test Passed <<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    # self.update_jira_issues(ssname)
                    assert True
                else:
                    self.log.error(">>>>>>>>>>>>>>>>>>>>>>>>> Test Failed <<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    self.takeScreenshot(ssname)
                    assert False
            except NoSuchElementException as exc:
                self.log.error(exc)
        elif exp == "fail" or exp == "Fail":
            try:
                time.sleep(3)
                verify = self.getElement(LVF, LTF)
                if verify is not None:
                    self.log.info(">>>>>>>>>>>>>>>>>>>>>>>>> Test Passed <<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    # self.update_jira_issues(ssname)
                    assert True
                else:
                    self.log.error(">>>>>>>>>>>>>>>>>>>>>>>>> Test Failed <<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    self.takeScreenshot(ssname)
                    assert False
            except NoSuchElementException as exc:
                self.log.error(exc)

    def scrollToElement(self,LV):
        target_element = self.driver.find_element(By.XPATH,LV)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

    def selectElement(self,LV,LT,selectBy,_value):
        selectElement= Select(self.getElement(LV,LT))
        time.sleep(3)
        if selectBy == 'text':
            selectElement.select_by_visible_text(_value)
        elif selectBy == 'index':
            selectElement.select_by_index(_value)
        elif selectBy == 'value':
            selectElement.select_by_value(_value)

    def getTextFromPage(self, text):
        pageText = self.driver.page_source
        print(pageText)
        if text in pageText:
            return True
        else:
            return False

    def actionChains(self,LV,LT):
        element = self.getElement(LV,LT)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def pressEnter(self, LV, LT):
        element = self.getElement(LV, LT)
        element.send_keys(Keys.RETURN)
        time.sleep(2)


    def enterBtn(self):
        # self.driver.press_keycode(66)
        action = ActionChains(self.driver)
        action.send_keys(Keys.RETURN)
        action.perform()

    def downArrowBtn(self):
        # self.driver.press_keycode(66)
        action = ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.perform()

    def switchIframe(self, LV, LT):
        iframe = self.getElement(LV, LT)
        self.driver.switch_to.frame(iframe)

    def leaveIframe(self):
        self.driver.switch_to.default_content()