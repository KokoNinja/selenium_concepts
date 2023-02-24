import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.db4free.net/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()
# //b[contains(text(),'phpMy')]
#"//a[@href='/phpMyAdmin']

print(driver.title)
print(driver.current_url)

# switching from one tab to another
# if two tabs, it will be 0,1 as per the index value
#driver.window_handles
#print(driver.window_handles[0])
#print(driver.window_handles[1])
#driver.switch_to.window()
#switch to second tab
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,'input_username').send_keys("koni")
driver.find_element(By.ID,'input_password').send_keys("welcome@123")
driver.find_element(By.ID,"input_go").click()
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)
driver.close()