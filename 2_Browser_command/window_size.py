from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get('https://www.google.com/')

# fetch title from browser
google_title = driver.title
# print(google_title)


# step 1 : current window size
# get  current window size
current_window_size = driver.get_window_size()
print("current_window_size: width = {}px , height ={}px".format(current_window_size['width'], current_window_size['height']))


# step 2 : Set window size

# set window size
driver.set_window_size(800,500)
set_window_size = driver.get_window_size()
print("set_window_size: width = {}px , height ={}px".format(set_window_size['width'], set_window_size['height']))


# step 3 : verify window size

# verify  window size
try:
    assert set_window_size['width'] == 800 and set_window_size['height']== 500 , "Window size is not 800*500"
    print("set window size is correct")

except AssertionError:
    print(str(AssertionError) + "Set window size incorrect")

time.sleep(2)
driver.close()
print("Test Done")