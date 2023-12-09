# ICSI_424_Final_Project_TEMP
A temp repo to store our code and documentation for our x-frame final project until Amir creates one for us

## TO DO:
- [ ] need to set up servers for x frames exploits (testing of the headers, testing of the attacks)
- [ ] expand from just iframes, use dom objects and features that are controlled by the x frame options
- [ ] need to create and test selenium scripts for browsing the 4 web browsers
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


## Resources used:
- Example Bootstrap code for webpage: https://getbootstrap.com/docs/4.0/examples/
- Bootstrap 4 cheat sheet: https://hackerthemes.com/bootstrap-cheatsheet/
- X frame example: https://youtu.be/odQMKq8QZ0k
- Clickjacking Defense - OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html
- Selenium IDE: https://www.selenium.dev/selenium-ide/


## Browser notes:
- Chrome and Edge: ignore the now deprecated X-Frame-Options when Content-Security-Policy is sent
- Safari for some reason will choose to prioritise the old X-Frame-Options. Moreover, Safari will itself consider the default X-Frame-Options: DENY.

## Example:
<http>
    <!-- ... -->

    <headers>
        <frame-options
        policy="SAMEORIGIN" />
    </headers>
</http>
