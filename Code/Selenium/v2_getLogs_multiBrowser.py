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

import datetime  # get datetime
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

    current_datetime = current_datetime.replace(":", "_")
    current_datetime = current_datetime.replace(".", "-")
    current_datetime = current_datetime.replace(" ", "_")

    return current_datetime


# -- function to write string data to file --
def writeToFile(nameOfDoc, inputText):
    # # # save string to file
    text_file = open(f"{nameOfDoc}.txt", "w")
    n = text_file.write(inputText)
    text_file.close()

# -- function to append string data to file --


def appendToFile(nameOfDoc, inputText):
    # # # save string to file
    text_file = open(f"{nameOfDoc}.txt", "a")
    n = text_file.write(inputText)
    text_file.close()


# -- function to pass in the browser type and the page to scrape
def getLogsFunc(driverForBrowser, browserName, webpageURL, webpageName):

    # setup driver
    driverCurrent = driverForBrowser

    # create name of output file
    currentDatetime = defang_datetime()
    outputFileName = f"{browserName}_{webpageName}_{currentDatetime}"

    # use driver to get the webpage url
    driverCurrent.get(webpageURL)

    try:
        page_title = driverCurrent.title  # get title of page and write to file
        pageTitle = f"** Page Title: {page_title} **\n"
        print(pageTitle)
        writeToFile(outputFileName, pageTitle)

        h1_bois = driverCurrent.find_elements(
            By.TAG_NAME, 'h1')  # find all h1 tags
        for index, h1_element in enumerate(h1_bois, start=1):
            element_text = h1_element.text
            # append them to the file
            h1_stored = f"H1 Element {index} Text: {element_text}\n"
            print(h1_stored)
            appendToFile(outputFileName, h1_stored)

        # ----- now get logs -----
        appendToFile(outputFileName, "\n\n CONSOLE LOGS: \n")
        logs = driverCurrent.get_log("browser")
        for log_entry in logs:
            print(log_entry)
            appendToFile(outputFileName, log_entry)

    # if error, we will print
    except Exception as e:
        print(f"GETLOGS encountered an error: {e}")

    finally:
        # close window after all
        driverForBrowser.quit()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Main
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# store all pages inside this dictionary
# source: https://www.w3schools.com/python/python_dictionaries.asp
weblinks = {
    "Index": "http://127.0.0.1:8000/index.html",
    "No-X-Frames": "http://127.0.0.1:8000/no_x-frames_set_1.html",
    "SAMEORIGIN": "http://127.0.0.1:8000/x-frames_set_2.html",
    "DENY": "http://127.0.0.1:8000/x-frames_set_3.html"
}


browsers = {
    "Chrome": webdriver.Chrome(),
    "Firefox": webdriver.Firefox(),
    "Edge": webdriver.Edge(),
}

# # get driver and set webpage
# driverChrome = webdriver.Chrome()
# driverFirefox = webdriver.Firefox()
# driverEdge = webdriver.Edge()


# loop through dict of web pages
# source: https://www.w3schools.com/python/python_dictionaries_loop.asp
for key, url in weblinks.items():
    #   print(key, value)
    print(f"** Key: {key} with url: {url}")

    # now loop through each browser for the output
    for browserName, driver in browsers.items():
        print(f"==> Using Browser: {browserName} for webpage: {key}")
        # do each browser test:
        getLogsFunc(driver, browserName, url, key)

print("done!")

