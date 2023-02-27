import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
driver.maximize_window()
driver.implicitly_wait(30)

#o inspect à ctrl+shift+c or f12

driver.find_element(By.XPATH,"//img[@alt='Go']").click()

actual_alert_text=driver.switch_to.alert.text
print(actual_alert_text)

driver.switch_to.alert.accept()
time.sleep(5)