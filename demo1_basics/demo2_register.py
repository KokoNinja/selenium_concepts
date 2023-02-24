import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://facebook.com/")
driver.maximize_window()
#i fpage loading takes time, it waits for the controls to be visible
driver.implicitly_wait(30)
#click on create new account

driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("John")
driver.find_element(By.NAME,"lastname").send_keys("Wick")
driver.find_element(By.NAME,"reg_email__").send_keys("kokoa@gmail.com")
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("kokoa@gmail.com")
driver.find_element(By.ID,"password_step_input").send_keys("welcome@@123")
driver.find_element(By.XPATH,"//input[@value='2']").click()
driver.find_element(By.XPATH,"//select[@id='day']").click()
#driver.find_element(By.ID,"day").send_keys("30")
#driver.find_element(By.ID,"month").send_keys("Apr")
#driver.find_element(By.ID,"year").send_keys("2000")
driver.find_element(By.NAME,"websubmit").click()

#dropdown
select_day=Select(driver.find_element(By.ID,"day"))
select_day.select_by_value("12")

select_month=Select(driver.find_element(By.ID,"month")) # also can use XPATH //select[@title="Month"]
select_month.select_by_visible_text("12")
time.sleep(5)

select_year=Select(driver.find_element(By.ID,"year"))
select_year.select_by_visible_text("2019")

#Select(driver.find_element(By.ID,"year")).select_by_value("2019")
#time.sleep(5)