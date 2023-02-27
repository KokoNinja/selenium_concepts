import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.oracle.com/in/database/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,"acctBtnLabel").click()
page_title1=driver.find_element(By.LINK_TEXT,"Sign-In").click()

time.sleep(5)
print(page_title1)

page_title=driver.find_element(By.XPATH,"//h2[contains(text(),'Oracle account')]").text
print(page_title)
time.sleep(5)

driver.find_element(By.ID,"sso_username").send_keys("John")
driver.find_element(By.ID,"ssopassword").send_keys("john123")
driver.find_element(By.ID,"signin_button").click()
actual_error=driver.find_element(By.XPATH,"//div[contains(text(),'Invalid username and/or password')]").text
print(actual_error)
time.sleep(5)
driver.quit()