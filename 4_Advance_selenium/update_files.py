from selenium import webdriver
import time
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def upload_files_demo():

    driver = webdriver.Chrome()

    # step 2 : go to log in page
    driver.get("https://the-internet.herokuapp.com/upload")
    time.sleep(3)

    chose_file_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"file-upload")))
    #chose_file_btn.send_keys("E:\SQA\Git and GitHub.pdf")
    file_path = "E:\SQA\Git and GitHub.pdf"

    try:
        chose_file_btn.send_keys(file_path)
        print("file available")

        update_btn= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"file-submit")))
        update_btn.click()

        success_message =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h3")))

        try:
            assert "File Uploaded" in success_message.text
            print("test passed. file upload")
        except AssertionError:
            print("test failed. files doesn't upload")

    except Exception:
        print("file is not availabe.exception" + str(Exception))








    driver.close()
upload_files_demo()