from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "emulator-5554"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Messages")
el9.click()
el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start chat")
el10.click()
el11 = driver.find_element(by=AppiumBy.ID,
                           value="com.google.android.apps.messaging:id"
                                 "/recipient_text_view")
el11.send_keys("Code generator")
el11.click()
el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                           value="Switch between entering text and numbers")
el12.click()
el13 = driver.find_element(by=AppiumBy.CLASS_NAME,
                           value="/hierarchy/android.widget.FrameLayout"
                                 "/android.widget.LinearLayout")
el13.click()
el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el14.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(
        interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(681, 1060)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(663, 107)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(
        interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(630, 2769)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(666, 326)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(
        interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1103, 2952)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(
        interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(673, 1888)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(670, 344)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.quit()
