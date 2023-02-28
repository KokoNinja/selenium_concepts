import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://nasscom.in/")
driver.maximize_window()
driver.implicitly_wait(30)


# mouse hover instead of click
actions=webdriver.ActionChains(driver)
# actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Membership']")).perform()
#element is present but not visible
# driver.find_element(By.XPATH,"//a[text()='Members Listing']").click()

# mouse hover instead of click
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Membership']")).perform()
# mouse hover instead of click
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Become a Member']")).perform()
#element is present but not visible. Click on it
driver.find_element(By.XPATH,"//a[text()='Membership Benefits']").click()
