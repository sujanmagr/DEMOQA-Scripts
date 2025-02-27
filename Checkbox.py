#script for demoqa in element section to click checkboxes
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url="https://demoqa.com/checkbox"
driver.get(url)
driver.maximize_window()
time.sleep(1)
driver.execute_script("window.scrollBy(0,550);")
expand=driver.find_element(*(By.XPATH,"//button[@title='Toggle']//*[name()='svg']"))
expand.click()
time.sleep(1)
desktop=driver.find_element(*(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']/div[@class='col-12 mt-4 col-md-6']/div[@class='check-box-tree-wrapper']/div[@id='tree-node']/ol/li[@class='rct-node rct-node-parent rct-node-expanded']/ol/li[1]/span[1]/button[1]//*[name()='svg']"))
document=driver.find_element(*(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']/div[@class='col-12 mt-4 col-md-6']/div[@class='check-box-tree-wrapper']/div[@id='tree-node']/ol/li[@class='rct-node rct-node-parent rct-node-expanded']/ol/li[2]/span[1]/button[1]//*[name()='svg']"))
download=driver.find_element(*(By.XPATH,"//li[3]//span[1]//button[1]//*[name()='svg']"))
desktop.click()
time.sleep(1)
document.click()
time.sleep(1)
download.click()
time.sleep(1)
time.sleep(2)
driver.quit()
