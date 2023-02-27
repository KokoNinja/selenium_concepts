import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.maximize_window()
driver.implicitly_wait(30)


#driver.find_element(By.XPATH,"//input[@name='fldLoginUserId']").send_keys("test123")

driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']").send_keys("test123"))
driver.find_element(By.LINK_TEXT,"CONTINUE").click()


#go to the main HTML 
driver.switch_to.default_content()