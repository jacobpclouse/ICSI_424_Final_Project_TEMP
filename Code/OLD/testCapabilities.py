from selenium import webdriver

# Set up the Firefox webdriver
options = webdriver.FirefoxOptions()

# Enable logging preferences to capture console logs
options.set_preference('browser.dom.window.dump.enabled', True)
options.set_preference('devtools.console.stdout.content', True)

# Create a Firefox webdriver instance
driver = webdriver.Firefox(options=options)

try:
    # Open the provided page
    url = "http://127.0.0.1:8000/x-frames_set_3.html"
    driver.get(url)

    # Get and print all logs
    logs = driver.get_log('browser')
    print("Logs:")
    for log_entry in logs:
        print(log_entry)

finally:
    # Close the webdriver
    driver.quit()

