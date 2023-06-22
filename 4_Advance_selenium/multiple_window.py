from selenium import webdriver
import time
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def multi_window_demo():
    driver = webdriver.Chrome()

    # step 2 : go to log in page
    driver.get("https://www.google.com/")

    time.sleep(5)
    assert "Google" in driver.title
    print(driver.title)

    # open new window

    driver.execute_script("window.open('https://www.apple.com/');")
    total_windows = driver.window_handles
    print(total_windows)

    # switch to new window(apple)

    driver.switch_to.window(total_windows[1])
    assert "Apple" in driver.title
    print("switch to new window:" + driver.title)
    time.sleep(5)

    # switch to old window (google)

    driver.switch_to.window(total_windows[0])
    assert "Google" in driver.title
    print("switch to old window:" + driver.title)
    time.sleep(5)

    driver.quit() 

multi_window_demo()