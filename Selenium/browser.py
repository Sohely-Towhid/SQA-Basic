from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get('https://www.google.com/')
time.sleep(5)
driver.close()