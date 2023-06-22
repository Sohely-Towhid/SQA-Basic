from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def select_dropdown():
    # step 1: launch the browser
    driver = webdriver.Chrome()

    # step 2 : go to log in page
    driver.get('https://the-internet.herokuapp.com/dropdown')

    # step 3: find dropdown

    dropdown = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"dropdown"))))

    # step 4:select option

    # dropdown.select_by_visible_text("Please select an option")


    # test 1:verify default option selected or not

    # get the selected option and check if it is selected

    default_selected_option = dropdown.first_selected_option

    try:
        assert default_selected_option.is_selected, "Please select an option"
        print("Please select an option is selected. test passed")
    except AssertionError:
        print(" no option is selected. test failed")

     # step 5:select option for test 2

    dropdown.select_by_value("1")
    time.sleep(5)

    # test 2:verify new option selected or not

    # get the selected option and check if it is selected

    new_selected_option = dropdown.first_selected_option

    try:
        assert new_selected_option.is_selected,"option 1"
        print("option 1 is selected. test passed")
    except AssertionError:
        print(" no option is selected. test failed")

    # test 3:verify all option selected or not

    expected_option = ["Please select an option is selected","option 1","option 2"]

    actual_option = []

    #loop for dropdown

    for opt in dropdown.options:
        options_text = opt.text
        actual_option.append(options_text)
        print(actual_option)

    # accepted and actual
    try:
        assert actual_option == expected_option
        print("option list test passed")
    except AssertionError:
        print("option list test failed")

    #step 6: close

    driver.close()
select_dropdown()

