# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# v2_getLogs_multiBrowser.py
'''
 create virt envir and then run: pip install selenium
 source: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

 TO DO:
add multiple browsers
add multiple pages to check -- do index, no xframe, sameorigin, and deny
add function to store outputs with browsername_page_accesssed_logs - either text or CSV
'''

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules / Headers
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import datetime # get datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function to Defang date time ---
def defang_datetime():
    current_datetime = f"_{datetime.datetime.now()}"

    current_datetime = current_datetime.replace(":","_")
    current_datetime = current_datetime.replace(".","-")
    current_datetime = current_datetime.replace(" ","_")
    
    return current_datetime


# -- function to pass in the browser type and the page to scrape
def getLogsFunc(driverForBrowser,webpageURL,webpageName):

    # use driver to get the webpage url
    driverForBrowser.get(webpageURL)

    try:
        page_title = driverForBrowser.title # title of page
        print(f"Page Title: {page_title}")

        h1_bois = driverForBrowser.find_elements(By.TAG_NAME, 'h1') # find all h1 tags
        for index, h1_element in enumerate(h1_bois, start=1):
            element_text = h1_element.text
            print(f"H1 Element {index} Text: {element_text}")


        # now get logs -----
        logs = driverForBrowser.get_log("browser")
        for log_entry in logs:
            print(log_entry)

    # if error, we will print
    except Exception as e:
        print(f"GETLOGS encountered an error: {e}")

    finally:
        # close window after all
        driverForBrowser.quit()



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Main
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#store all pages inside this dictionary
# source: https://www.w3schools.com/python/python_dictionaries.asp
weblinks = {
  "Index": "http://127.0.0.1:8000/index.html",
  "No-X-Frames": "http://127.0.0.1:8000/no_x-frames_set_1.html",
  "SAMEORIGIN": "http://127.0.0.1:8000/x-frames_set_2.html",
  "DENY": "http://127.0.0.1:8000/x-frames_set_3.html"
}

# get driver and set webpage
driverChrome = webdriver.Chrome()
driverFirefox = webdriver.Firefox()

# driver.get("http://127.0.0.1:8000/x-frames_set_3.html")

# try:
#     page_title = driver.title # title of page
#     print(f"Page Title: {page_title}")

#     h1_bois = driver.find_elements(By.TAG_NAME, 'h1') # find all h1 tags
#     for index, h2_element in enumerate(h1_bois, start=1):
#         element_text = h2_element.text
#         print(f"H2 Element {index} Text: {element_text}")


#     # now get logs -----
#     logs = driver.get_log("browser")
#     for log_entry in logs:
#         print(log_entry)


# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     # Close the browser window
#     driver.quit()
