import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.automationworld.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.LINK_TEXT,"Subscribe").click()

driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,"id24_344").click()
driver.find_element(By.ID,"id1").send_keys("Konika")
driver.find_element(By.ID,"id2").send_keys("Negi")
driver.find_element(By.ID,"id10").send_keys("Engineer")
driver.find_element(By.ID,"id11").send_keys("9999999999")
driver.find_element(By.ID,"id195").send_keys("www.test.com")
driver.find_element(By.ID,"id3").send_keys("Einfo")

country_name=Select(driver.find_element(By.ID,"id7"))
country_name.select_by_value("189")
driver.find_element(By.ID,"id6").send_keys("chennai")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='2327']").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
print_error=driver.find_element(By.XPATH,"//li[text()='Email Address is required.']").text
print(print_error)