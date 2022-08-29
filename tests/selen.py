"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 -v
/dev/shm:/dev/shm selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
)

driver.get("http://google.com")

data_users = {"Alex": "password-1"}
data_users["Bill"] = "Password2"

button = driver.find_elements(By.XPATH, '//button')

# listed below is pseudocode
field = driver.find_element(By.XPATH, '//field')
field2 = driver.find_element(By.XPATH, '//field')

for name, password in data_users.items():
    password = f"dddd{password}ghrtid"
    field.send_keys(name)
    field2.send_keys(password)

    assert button == 1
