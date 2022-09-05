"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900
selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from data.page_objects import submit_button_id, login_field_id, \
    password_field_id, admin_page_header_id

with open(
        "//data.json",
        "r") as f:
    secret_variables = json.load(f)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
)

driver.get(secret_variables["endpoint"])

name_field = driver.find_element(By.ID, login_field_id)
submit_button = driver.find_element(By.XPATH, submit_button_id)
password_field = driver.find_element(By.XPATH, password_field_id)

name_field.send_keys(secret_variables["name"])
time.sleep(1)
password_field.send_keys(secret_variables["password"])

submit_button.click()
time.sleep(1)

element_fo_found = driver.find_element(By.XPATH, admin_page_header_id)

assert element_fo_found.text == "Django administration"

driver.close()
