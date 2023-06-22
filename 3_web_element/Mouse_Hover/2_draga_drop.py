from selenium import webdriver
import time
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def drag_drop_demo():
    driver = webdriver.Chrome()

    # step 2 : go to log in page
    driver.get("https://material.angular.io/cdk/drag-drop/examples")

    time.sleep(5)

    source_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#cdk-drag-drop-axis-lock > div > div.docs-example-viewer-body.ng-star-inserted > cdk-drag-drop-axis-lock-example > div:nth-child(2)")))

    target_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#cdk-drag-drop-axis-lock > div > div.docs-example-viewer-body.ng-star-inserted > cdk-drag-drop-axis-lock-example > div:nth-child(1)")))

    actions = ActionChains(driver)

    actions.drag_and_drop(source_element,target_element).perform()


drag_drop_demo()