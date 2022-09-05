"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900
selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

# our variables
submit_button_id = '//*[@id="login-form"]/div[3]/input'
field_id = '//*[@id="id_username"]'
field_id_2 = '//*[@id="login-form"]/div[2]'

driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
)

driver.get("https://www.aqa.science/admin/")

field = driver.find_element(By.XPATH, field_id)
field = driver.find_element(By.XPATH, field_id)
button = driver.find_element(By.XPATH, submit_button_id)

field.send_keys("Some name ")
time.sleep(10)

button.click()
