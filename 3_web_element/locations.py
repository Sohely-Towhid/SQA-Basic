from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

# step 1 : open google window
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(2)

# step 2 : find username input field
username = driver.find_element(By.NAME('username'))

# step 3 : find password
password = driver.find_element(By.NAME('password'))

# step 4 : log in btn
login_btn = driver.find_element(By.XPATH('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'))

# verify the element field is correct
if username is not None:
    print("username field is correct")
else:
    print("No username")
if password is not None:
    print("password field is correct")
else:
    print("no password")
if login_btn is not None:
    print("login btn is correct")
else:
    print("no login")

driver.close()
print("test complete")