import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://github.com/login")
driver.maximize_window()


driver.find_element(By.ID,"login_field").send_keys("hello")
driver.find_element(By.ID,"password").send_keys("hello")
driver.find_element(By.NAME,"commit").click()


time.sleep(5)

