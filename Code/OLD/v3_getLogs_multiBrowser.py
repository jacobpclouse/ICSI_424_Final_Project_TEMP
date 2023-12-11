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
import os  # folder
from selenium import webdriver # selenium imports
from selenium.webdriver.common.by import By

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function to print out our logo ---
def printOurLogo():
    ourLogoBOI = [
        "|  \\/  (_) |          | ___ \\                     |_  |     | |       ",
        "| .  . |_| | _____    | |_/ /   _ _ __   ___        | | __ _| | _____ ",
        "| |\\/| | | |/ / _ \\   |    / | | | '_ \\ / _ \\       | |/ _` | |/ / _ \\",
        "| |  | | |   <  __/_  | |\\ \\ |_| | | | |  __/_  /\\__/ / (_| |   <  __/",
        "\\_|  |_|_|_|\\_\\___( ) \\_| \\_\\__,_|_| |_|\\___( ) \\____/ \\__,_|_|\\_\\___|",
        "                  |/                        |/                          "
    ]

    print("Create and Tested by:")
    for boi in ourLogoBOI:
        print(boi)
    print("ICSI 424/524 Final Project -- Fall 2023")


# --- Function to Defang date time ---
def defang_datetime():
    current_datetime = f"_{datetime.datetime.now()}"

    current_datetime = current_datetime.replace(":", "_")
    current_datetime = current_datetime.replace(".", "-")
    current_datetime = current_datetime.replace(" ", "_")

    return current_datetime


# ---  Function to write string data to file ---
def writeToFile(nameOfDoc, inputText, parentDirectory):
    nameOfTextFile = f"{nameOfDoc}.txt"
    path = os.path.join(parentDirectory, nameOfTextFile)
    # # # save string to file
    text_file = open(path, "w")
    writeOver = text_file.write(inputText)
    text_file.close()

# --- Function to append string data to file ---
def appendToFile(nameOfDoc, inputText, parentDirectory):
    nameOfTextFile = f"{nameOfDoc}.txt"
    path = os.path.join(parentDirectory, nameOfTextFile)
    # # # save string to file
    text_file = open(path, "a")
    append = text_file.write(inputText)
    text_file.close()


# --- Function to pass in the browser type and the page to scrape ---
def getLogsFunc(driverForBrowser, browserName, webpageURL, webpageName, parentDir):

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
        writeToFile(outputFileName, pageTitle, parentDir)

        driver.implicitly_wait(0.5)

        h1_bois = driverCurrent.find_elements(
            By.TAG_NAME, 'h1')  # find all h1 tags
        for index, h1_element in enumerate(h1_bois, start=1):
            element_text = h1_element.text
            # append them to the file
            h1_stored = f"H1 Element {index} Text: {element_text}\n"
            print(h1_stored)
            appendToFile(outputFileName, h1_stored, parentDir)

        # ----- now get logs -----
        appendToFile(outputFileName, "\n\n CONSOLE LOGS: \n", parentDir)

        if browserName.lower() == "firefox":
            # For Firefox, use different method to get logs
            print("Firefox logs...")
            # logs = driverCurrent.get_log("moz:browser")
            logs = driverCurrent.get_log("server")
        else:
            # For Chrome and Edge
            logs = driverCurrent.get_log("browser")
        # loop through logs
        for log_entry in logs:
            print(log_entry)
            appendToFile(outputFileName, str(log_entry), parentDir)
            appendToFile(outputFileName, "\n", parentDir)

    # if error, we will print
    except Exception as e:
        print(f"GETLOGS encountered an error: {e}")

    # finally:
    #     # close window after all
    #     time.sleep(5)  # Adjust the delay as needed
    #     driverForBrowser.quit()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Main
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# store all pages inside this dictionary
# source: https://www.w3schools.com/python/python_dictionaries.asp
weblinks = {
    "1_INDEX": "http://127.0.0.1:8000/index.html",
    "2_NO-X-FRAMES-SET": "http://127.0.0.1:8000/no_x-frames_set_1.html",
    "3_SAMEORIGIN": "http://127.0.0.1:8000/x-frames_set_2.html",
    "4_DENY": "http://127.0.0.1:8000/x-frames_set_3.html"
}

# webpages to use
browsers = {
    "Chrome": webdriver.Chrome(),
    "Firefox": webdriver.Firefox(),
    "Edge": webdriver.Edge()
}

# create a directory: https://www.geeksforgeeks.org/create-a-directory-in-python/
folderDatetime = defang_datetime()
folderName = f"getLogs_from_{folderDatetime}"
os.mkdir(folderName)

# loop through dict of web pages
# source: https://www.w3schools.com/python/python_dictionaries_loop.asp
for key, url in weblinks.items():
    print(f"** Key: {key} with url: {url}")

    # now loop through each browser for the output
    for browserName, driver in browsers.items():
        print(f"==> Using Browser: {browserName} for webpage: {key}")
        # do each browser test:
        getLogsFunc(driver, browserName, url, key, folderName)

printOurLogo()
