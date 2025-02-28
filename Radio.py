#script for demoqa in element section to click on the radio buttons
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://demoqa.com/radio-button"
driver.get(url)

driver.maximize_window()
time.sleep(1)
driver.execute_script("window.scrollBy(0,200);")
yes=driver.find_element(*(By.XPATH,"//label[normalize-space()='Yes']"))
impressive=driver.find_element(*(By.XPATH,"//label[normalize-space()='Impressive']"))
# no=driver.find_element(*(By.XPATH,"//label[normalize-space()='No']"))
yes.click()
print("yes clicked")
time.sleep(1)
impressive.click()
print("impressinve clicked")
time.sleep(1)
# try:
#     no.click()
#     print("no clicked")
# except:
#     print("cant click")
time.sleep(2)
driver.quit()
