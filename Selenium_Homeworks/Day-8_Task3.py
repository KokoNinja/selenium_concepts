import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.online.citibank.co.in/")
driver.maximize_window()
driver.implicitly_wait(30)


#driver.find_element(By.XPATH,"//a[contains(@title,'Close')]").click()
driver.find_element(By.XPATH,"//a[@title='Close']").click()   #USE CLASS_NAME
driver.find_element(By.LINK_TEXT,"Login").click()           ##span[normalize-space()='Login']
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//div[contains(text(),'Forgot User ID')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[contains(text(),'select your product type')]").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()
driver.find_element(By.ID,"citiCard1").send_keys("4545")

driver.find_element(By.ID,"citiCard2").send_keys("5656")
driver.find_element(By.ID,"citiCard3").send_keys("8887")
driver.find_element(By.ID,"citiCard4").send_keys("9998")
driver.find_element(By.ID,"cvvnumber").send_keys("003")

time.sleep(5)
driver.find_element(By.NAME,"DOB").click()
time.sleep(5)

select_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
select_month.select_by_value("0")

select_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
select_year.select_by_value("1989")

driver.find_element(By.LINK_TEXT,"4").click()

#driver.find_element(By.XPATH,"//input[@type = 'button']").click()
driver.find_element(By.XPATH,"//input[@value = 'PROCEED']").click()
time.sleep(5)

print_terms=driver.find_element(By.XPATH,"//li[text()='• Please accept Terms and Conditions ']").text
print(print_terms)

print_dialog=driver.find_element(By.XPATH, "//div[@role='dialog']").text
print(print_dialog)
#select_product.select_by_value("Credit Card")



#CSS Selector
#driver.find_element(By.CSS_SELECTOR,"#citiCard1").send_keys("4545")
# select_year=Select(d.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
# select_year.select_by_visible_text("2000")
#
# select_month=Select(d.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
# select_month.select_by_visible_text("Apr")


# CSS selector - https://www.w3schools.com/cssref/css_selectors.php 
# #id
# .classname
# tagname[attribute='']
# [attribute='']


#Javascript
#driver.execute_script("document.querySelector('#bill-date-long').value='11/09/2000'")

#javascript & webelement
