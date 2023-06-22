from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

# step 1 : open google window
driver.get('https://www.google.com/')
time.sleep(2)

# Step 2 : open apple
driver.get('https://www.apple.com/')
time.sleep(2)

# Step 3:back to google

driver.back()
print(driver.title) #Google
time.sleep(2)

# step 4 :forward to apple
driver.forward()
print(driver.title) # Apple
time.sleep(2)

#  step 5 : refresh apple
driver.refresh()

# step 6 : finish
driver.close()