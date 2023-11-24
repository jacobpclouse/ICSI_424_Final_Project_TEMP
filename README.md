# ICSI_424_Final_Project_TEMP
A temp repo to store our code and documentation for our x-frame final project until Amir creates one for us

## Authors:
- Michael Paglia 
- Rune Vannaken
- Jacob Clouse

## Run the test webserver:
1) CD into the 'Code/X-Frame-Webpage' directory
2) Run the python3 command: python -m http.server
(if you have python2 and python3 installed, use the command: python3 -m http.server)
3) In the target browser, go to the link: http://0.0.0.0:8000/
4) Run your tests!


## Resources used:
- Example Bootstrap code for webpage: https://getbootstrap.com/docs/4.0/examples/
- Bootstrap 4 cheat sheet: https://hackerthemes.com/bootstrap-cheatsheet/
- X frame example: https://youtu.be/odQMKq8QZ0k
- Clickjacking Defense - OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html

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
