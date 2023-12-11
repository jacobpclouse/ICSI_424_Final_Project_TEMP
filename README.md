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
### How we built this:
- We originally built this software to test out how xframe options work and learn by doing. The first thing that we did was to use HTML and Bootstrap to setup a test website that would have several pages for us to test against. We had an index page (just a general landing page that would be a compass to explain what we were doing and a control for a normal webpage), a no xframes set page (this would be host a number of images and links to serve as our main control page), a SAMEORIGIN page (displaying options from the same origin, we had some trouble getting this working with our data), and a DENY page (this would be where the meat of our testing and would show how various browsers would handle x frames set to deny). The deny page had additional content to test including links to Google maps, youtube and twitter within different DOM objects. We tested our pages manually and confirmed that the consoles were displaying the outputs that we needed in regards to our xframe options. We then set about building our testing script with the selenium webdriver. Originally, we wanted to use the selenium IDE to test each page, but it would not allow us to recover the logs of each page we visited, so it was not going to be viable. We instead used the selenium webdriver to create a python script that would allow us to loop through the 4 pages and grab their logs. This also had the added benefit that it would be much more scalable than using the IDE as we didn’t have to go through manually and open up each page in a target browser to get the data we wanted, it would simply be a matter of adding a new browser and the corresponding webdriver to our browser dictionary. We made the code modular enough so that we could do the scraping inside a function and it would create specific text files labeled with the page and browser information and containing the scraped data. We also would store the output text files from each scraping session in their own individual folders for easy organization. 
The biggest hurdle that we had to overcome was that only a select few types of browsers were natively supported in the selenium webdriver python library, these being Chrome, Microsoft Edge, Internet Explorer, Firefox and Safari. We attempted to use Opera by installing a third party web driver and using that with the chrome webdriver, but it never was able to work and kept throwing errors about not being supported. We had issues with Internet Explorer as well, it would not throw any errors but it would cause the program to hang and we would have to terminate it manually. Most likely this is due to it being deprecated several years ago and not receiving updates. Firefox worked with the selenium webdriver script but it does not support the get_logs function to recover logs from the webdriver and would throw an HTTP error each time (this lead to our Firefox console logs not saving to the text files). There was no specific way to get around this and we couldn’t get a workaround to it implemented in time for the due date of this project, though we can still manually test and see the outputs of our work in the browser. A similar issue occurs with safari with this software and no logs are created.

### How it runs: 
- Running this software first requires us to setup and run our test bootstrap website on a local webserver with python. Before we do anything though, we need to make sure we have python3 and the latest version of the selenium webdriver installed on our computer (you can create a virtual environment and use the ‘pip install -r requirements.text’ command to install all the required packages for our project).  We change directory into the ‘X-Frame-Webpage’ directory and then run the following command in our terminal: python -m http.server --bind 127.0.0.1 . This will allow us to access our web pages in our browser and subsequently with our selenium webdriver. In another terminal, we can change directory into the Code folder and then run the command “python getLogs.py” to run the webdriver script. (NOTE: if you are on windows, you will have to comment out the safari key in the browsers dictionary within the script, otherwise it will fail). Then the script will take over, opening up the browser windows, navigating to all the pages and then storing the results. 

### Observations: 
- When looking at our output files, we can see how different browsers treat different output. For instance, going back to Firefox we see that it doesn’t even allow the logs to be captured while the other browsers do (hence we had to manually navigate to the pages and read the output for ourselves). We see that chrome only threw a couple of errors related to xframes vs Edge that threw many more lines of errors concerning xframes and seemed to go more into depth. Looking at the Firefox logs manually, there were more details logs and more about how features are going to be depreciated in the future (ie: ‘The Components object is deprecated. It will soon be removed. Babys_first_data_breach.jpeg’ ). Edge has much more about tracking prevention then the other browsers, it seems to have the most detailed and robust logs out of the group. 
