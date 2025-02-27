#script for demoqa in element section to fillup the textbox field
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url="https://demoqa.com/elements"
driver.get(url)
driver.maximize_window()
time.sleep(1)
textbox=driver.find_element(By.ID, "item-0")
textbox.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
#find input fields 
fullName=driver.find_element(By.ID,"userName")
email=driver.find_element(By.ID, "userEmail")
C_Address=driver.find_element(By.ID, "currentAddress")
P_Address=driver.find_element(By.ID,"permanentAddress")
#sending input values to the fields using send keys 
fullName.send_keys("Sachin Budhathoki")
time.sleep(1)
email.send_keys("busafh@gmail.com")
time.sleep(1)
C_Address.send_keys("Kathmandu")
time.sleep(1)
P_Address.send_keys("Baglung")
time.sleep(1)
driver.execute_script("window.scrollBy(0,50);")
Submit=driver.find_element(By.ID, "submit")
try:
    Submit.click()
    print("the form is submitted")
except:
    print("no submit button pressed")

time.sleep(2)
driver.quit()