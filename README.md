# ICSI_424_Final_Project_TEMP
A temp repo to store our code and documentation for our x-frame final project until Amir creates one for us  [![GitHub contributors](https://img.shields.io/github/contributors/jacobpclouse/526-Final-Project.svg)]("https://github.com/jacobpclouse/526-Final-Project/graphs/contributors")

> Link to the original Repo: https://github.com/jacobpclouse/ICSI_424_Final_Project_TEMP

## TO DO:
- [x] need to set up servers for x frames exploits (testing of the headers, testing of the attacks) -- done with python server
- [x] expand from just iframes, use dom objects and features that are controlled by the x frame options
- [x] need to create and test selenium scripts for browsing the 4 web browsers
- [ ] (OPTIONAL) need to create attack with headers on vs headers off and see how x frame options stops it
- [ ] write everything up in the readme file as a report

## Authors:
- Michael Paglia 
- Rune Vannaken
- Jacob Clouse

## Run the test webserver:
1) CD into the 'Code/X-Frame-Webpage' directory
2) Run the python3 command: python -m http.server --bind 127.0.0.1
(if you have python2 and python3 installed, use the command: python3 -m http.server)
3) In the target browser, go to the link: http://127.0.0.1:8000/
4) Run your tests!


## Run Tests:
1) Create a virtual environment (use activateVirEnv.md to do this)
2) pip install -m requirements.text
3) Change directory into the Code/Selenium folder
4) Run ```python getLogs.py```
5) Analyze your results from the text outputs, change browsers and see what changes


## Resources used:
- Example Bootstrap code for webpage: https://getbootstrap.com/docs/4.0/examples/
- Bootstrap 4 cheat sheet: https://hackerthemes.com/bootstrap-cheatsheet/
- X frame example: https://youtu.be/odQMKq8QZ0k
- Clickjacking Defense - OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html
- Selenium IDE: https://www.selenium.dev/selenium-ide/
- Writing first script: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
- Getting logs in firefox with selenium: https://stackoverflow.com/questions/23231931/getting-console-log-output-from-firefox-with-selenium
- HTTP method not allowed when trying to capture console: https://stackoverflow.com/questions/62230582/http-method-not-allowed-when-trying-to-capture-console
- Opera Driver releases: https://github.com/operasoftware/operachromiumdriver/releases


## Browser notes:
- Chrome and Edge: ignore the now deprecated X-Frame-Options when Content-Security-Policy is sent
- Safari for some reason will choose to prioritise the old X-Frame-Options. Moreover, Safari will itself consider the default X-Frame-Options: DENY.

## X Frame Example:
<http>
    <!-- ... -->

    <headers>
        <frame-options
        policy="SAMEORIGIN" />
    </headers>
</http>

## Report Write Up:
