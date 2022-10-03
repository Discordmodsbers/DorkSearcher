# DorkSearcher
This Dork Searcher is like no other.

:fire: It uses the googlesearch library to search up dorks and output them.

:fire: It can pull up websites just by the library webbrowser so you dont have to leave the terminal but copying the links and opening up a browser.




:rocket: What else can it do?
It can exploit websites with a xss vuln (You would need to use your own dorks for that)

:rocket: What does the preset dorks search for?
It searches for sqli vulns and they all work.


# Usage


usage: DorkSearcher.py [-h] [-d] [-i] [-c]

optional arguments:
  -h, --help        show this help message and exit
  -d, --dictionary  Takes infomation from 'targets.txt'
                    and searches them!
  -i, --interact    Runs the tui version of this tool!
  -c, --crawl       Runs the crawler to check for sqli (can be used in interactive mode and dictionary mode) -interactive not yet-

# Known bugs.

1. Not being able to dork search the entire txt

2. Occasonally get rate limted by google

3. Some how not reading targets.txt (Newly found so ima patch this right now)

# Updates added.

1. Added a working setup file that lets the user run 'dorksearch' from anywhere

2. Ascii art

# To do.

1. Patch some bugs

2. Use proxies

3. Update ToS to something proffesional 
