import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://facebook.com/")

ele=driver.find_element(By.ID,"email")
ele.click()
ele.send_keys("test@gmail.com")
driver.find_element(By.ID,"email").send_keys("test123@gmail.com")
driver.find_element(By.ID,"pass").send_keys("welcome123")
driver.find_element(By.NAME,"login").click()


driver.quit()


time.sleep(5)

