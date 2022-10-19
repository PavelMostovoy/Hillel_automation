from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# setup the web driver and launch the webview app.
caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "emulator-5554"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
driver.implicitly_wait(100)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Messages")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start chat")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID,
                          value="com.android.camera2:id/progress_overlay")
el3.send_keys("11111111111")
el4 = driver.find_element(by=AppiumBy.ID,
                          value="com.google.android.apps.messaging:id"
                                "/contact_list_view")
el4.clear()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(
    interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1112, 2946)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(
    interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(730, 661)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(771, 74)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(
    interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(726, 1912)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(796, 90)
actions.w3c_actions.pointer_action.release()
actions.perform()
