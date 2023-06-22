from selenium import webdriver
import time

from selenium.webdriver.common.by import By

def webElement_state():

    # step 1: launch the browser
    driver = webdriver.Chrome()

    # step 2 : go to log in page
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)

    # step 3: enter username
    username = driver.find_element(By.NAME,"username")


    try:
      assert username.is_displayed()
      username.send_keys("Admin")
    except AssertionError:
      print("username is not available")

    time.sleep(5)

    # step 4: Enter Password
    Password = driver.find_element(By.NAME, "password")


    try:
     assert Password.is_enabled()
     Password.send_keys("admin123")
    except AssertionError:
     print("wrong")
    time.sleep(5)
    # step 5 : click log in
    loginbtn = driver.find_element(By.CSS_SELECTOR, (
    "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button"))
    try:
        assert loginbtn.is_enabled()
        loginbtn.click()
    except AssertionError:
        print("login is not available")
    time.sleep(5)

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

   # step 9 : close browser
    driver.close()

webElement_state()