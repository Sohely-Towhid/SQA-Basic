from selenium import webdriver
import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handel_alert():

    driver = webdriver.Chrome()

    # step 2 : go to log in page
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    #normal js alert


    normal_alert_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#content > div > ul > li:nth-child(1) > button")))
    normal_alert_btn.click()
    time.sleep(5)

    normal_alert = WebDriverWait(driver,10).until(EC.alert_is_present())
    # verify js alert

    try:

        assert normal_alert.text =="I am a JS Alert"
        print("test passed.Normal alert open")

    except AssertionError:
        print("Test failed. normal Alert not open")

    # handel alert
    normal_alert.accept()

    try:
        alert_text = normal_alert.text
        assert False,"test failed alert still open"

    except NoAlertPresentException:
        print("test passed normal alart closed")
        pass

    #close the alert

    driver.close()





handel_alert()