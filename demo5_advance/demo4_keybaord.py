import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://google.com/")
driver.maximize_window()
driver.implicitly_wait(30)

#modifier keys  -- ctrl, alt, shift

actions=webdriver.ActionChains(driver)
actions.key_down((webdriver.Keys.SHIFT)\
                 .send_keys("Hello World").key_up(webdriver.Keys.SHIFT).pause(1)\
                 .send_keys(webdriver.Keys.ARROW_DOWN).send_keys(webdriver.Keys.ARROW_DOWN)\
                 .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).send_keys(webdriver.Keys.ENTER)