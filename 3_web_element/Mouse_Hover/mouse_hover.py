from selenium import webdriver
import time
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
def mouse_hover_demo():

    driver = webdriver.Chrome()

    # step 2 : go to log in page
    driver.get("https://demo.opencart.com/")
    time.sleep(2)

    menu_desktops = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Desktops")))

    actions = ActionChains(driver)

    actions.move_to_element(menu_desktops).perform()

    submenu_mac1 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Mac (1)")))

    submenu_mac1.click()

    # verify mac page open

    try:
        assert "Mac" in driver.title
        print("Test Passed.Mac page is found")
    except AssertionError:
        print(" Test Failed.Mac page not found")

    driver.close()

mouse_hover_demo()
