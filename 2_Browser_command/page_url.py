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
    assert "https://www.google.com/" in driver.current_url
    print("Assertion passed. Url is correct")
except AssertionError:
    print(str(AssertionError) + "Url not found")

time.sleep(2)
driver.close()
print("Test Done")