import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.NAME,"UserFirstName").send_keys("Konika")
driver.find_element(By.NAME,"UserLastName").send_keys("Negi")
Select(driver.find_element(By.NAME,"UserTitle")).select_by_value("IT_Manager_AP")
Select(driver.find_element(By.NAME,"CompanyEmployees")).select_by_visible_text("101 - 500 employees")
Select(driver.find_element(By.NAME,"CompanyCountry")).select_by_value("GB")
driver.find_element(By.XPATH,"//div[@class='checkbox-ui']").click()
driver.find_element(By.NAME,"start my free trial").click()

#driver.find_element((By.XPATH,"//span[contains@id,'UserPhone']")).text
actual_error=driver.find_element(By.XPATH,"//span[contains(text(),'valid phone')]").text
print(actual_error)
time.sleep(5)
driver.quit()

