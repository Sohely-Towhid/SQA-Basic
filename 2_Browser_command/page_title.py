from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get('https://www.google.com/')

# fetch title from browser
google_title = driver.title
print(google_title)

# verify title
try:
    assert "Google" in driver.title
except AssertionError:
    print(str(AssertionError) + "Title not found")

time.sleep(2)
driver.close()
print("Test Done")