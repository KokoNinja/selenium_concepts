import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.medibuddy.in/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.LINK_TEXT,"Login").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[text()='I have a Corporate Account']").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Login using Username & Password')]").click()
driver.find_element(By.NAME,"userName").send_keys("john")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.NAME,"password").send_keys("john123")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()

#check_error=driver.find_element(By.XPATH,"//div[text()='Please enter valid username and password']").text
error=driver.find_element(By.XPATH,"//div[text()='You have entered incorrect password. If you forgot the password please reset your password by clicking on the forgot password link.']").text
print(error)
time.sleep(5)
driver.quit()