import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://facebook.com/")
driver.maximize_window()
#i fpage loading takes time, it waits for the controls to be visible
driver.implicitly_wait(30)
#click on create new account

driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("John")
driver.find_element(By.NAME,"lastname").send_keys("Wick")
driver.find_element(By.ID,"password_step_input").send_keys("welcome@@123")
driver.find_element(By.XPATH,"//input[@value='-1']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//select[@id='day']").click()
#driver.find_element(By.XPATH,"//select[text()='2']").click()
time.sleep(5)

#time.sleep(5)
#driver.find_element(By.XPATH,"//select[@text()='2']").click()
#time.sleep(5)




#20 dec 2000 dropdow

#driver.find_element(By.ID,"//select[@day='3']").click()


driver.implicitly_wait(10)
