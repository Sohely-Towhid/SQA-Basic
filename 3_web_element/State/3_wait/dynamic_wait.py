from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait():

    # step 1: launch the browser
    driver = webdriver.Chrome()

    # step 2 : go to log in page
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    # step 3: enter username

    username = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"username")))


    try:
      assert username.is_displayed()
      username.send_keys("Admin")
    except AssertionError:
      print("username is not available")



    # step 4: Enter Password
    Password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"password")))



    try:
     assert Password.is_enabled()
     Password.send_keys("admin123")
    except AssertionError:
     print("wrong")

    # step 5 : click log in
    loginbtn =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")))


    try:
        assert loginbtn.is_enabled()
        loginbtn.click()
    except AssertionError:
        print("login is not available")


    # step 6 : expected result , verify by url

    Expectedresult = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # step 7 : actual result
    ActualResult = driver.current_url
    # step 8: test result
    try:
     assert Expectedresult == ActualResult
     print("test result : passed")
    except AssertionError:
     print("test failed")
    time.sleep(5)

   # step 9 : close browser
    driver.close()

wait()