import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as By

# setup the web driver and launch the webview app.
capabilities = {
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "browserName": "Chrome"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

# Navigate to the page and interact with the elements on the guinea-pig page
# using id.
driver.get('http://saucelabs.com/test/guinea-pig')
element = driver.find_element(By, value='i_am_an_id')
# check the text retrieved matches expected value
assert element.text == 'I am a div'
time.sleep(5)
# populate the comments field by id
comments = "//*[@id='comments']"
driver.find_element(By.XPATH, comments).send_keys('My comment')
time.sleep(10)

# close the driver
driver.quit()
