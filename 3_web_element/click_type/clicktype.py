from selenium import webdriver
import time

from selenium.webdriver.common.by import By

def login_orangeHrm():

    # step 1: launch the browser

 driver = webdriver.Chrome()

    #step 2 : go to log in page
 driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
 time.sleep(5)
    #step 3: enter username
 username = driver.find_element(By.NAME,("username"))
 username.send_keys("Admin")
 time.sleep(5)
    #step 4: enter password
 password = driver.find_element(By.NAME,("password"))
 password.send_keys("admin123")
 time.sleep(5)

    #step 5 : click log in
 loginbtn = driver.find_element(By.CSS_SELECTOR,("#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button"))

 loginbtn.click()
 time.sleep(5)

    # step 6 : expected result , verify by url

 Expectedresult = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

 # step 7 : actual result
 ActualResult = driver.current_url
 #step 8: test result
 try:
      assert Expectedresult == ActualResult
      print("test result : passed")
 except AssertionError:
      print("test failed")

 # step 9 : close browser
 driver.close()

login_orangeHrm()

def invalid_login_orangeHrm():
    # step 1: launch the browser

 driver = webdriver.Chrome()

    #step 2 : go to log in page
 driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
 time.sleep(5)
    #step 3: enter username
 username = driver.find_element(By.NAME,("username"))
 username.send_keys("Adminaa")
 time.sleep(5)
    #step 4: enter password
 password = driver.find_element(By.NAME,("password"))
 password.send_keys("admin123aa")
 time.sleep(5)

    #step 5 : click log in
 loginbtn = driver.find_element(By.CSS_SELECTOR,("#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button"))

 loginbtn.click()
 time.sleep(5)

    # step 6 : expected result , verify by url

 Expectedresult = "Invalid credentials"

 # step 7 : actual result
 ActualResult = driver.find_element(By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > div > div.oxd-alert.oxd-alert--error > div.oxd-alert-content.oxd-alert-content--error > p").text
 #step 8: test result
 try:
      assert Expectedresult == ActualResult
      print("test result :invalid passed")
 except AssertionError:
      print("test failed. invalid failed")

 # step 9 : close browser
 driver.close()

invalid_login_orangeHrm()