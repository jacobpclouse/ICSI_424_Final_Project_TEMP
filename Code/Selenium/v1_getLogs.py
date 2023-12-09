# create virt envir and then run: pip install selenium

# source: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get driver and set webpage
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/x-frames_set_3.html")

try:
    page_title = driver.title # title of page
    print(f"Page Title: {page_title}")

    h1_bois = driver.find_elements(By.TAG_NAME, 'h1') # find all h1 tags
    for index, h2_element in enumerate(h1_bois, start=1):
        element_text = h2_element.text
        print(f"H2 Element {index} Text: {element_text}")


    # now get logs -----
    logs = driver.get_log("browser")
    for log_entry in logs:
        print(log_entry)


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()
