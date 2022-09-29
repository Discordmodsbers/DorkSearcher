from googlesearch import search
import time, sys, os
from colorama import Fore
import argparse
import webbrowser

#Slow print for things
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


#For loading screens ofc
delay = 0.2

#Clear screen since im too lazy to type out os.system('clear')
def cls():
  os.system('clear')

#Loading function
def loader():
  for i in range(1):
    cls()
    print("Loading")
    time.sleep(delay)
    cls()
    print("lOading.")
    time.sleep(delay)
    cls()
    print("loAding..")
    time.sleep(delay)
    cls()
    print("loaDing...")
    time.sleep(delay)
    cls()
    print("loadIng....")
    time.sleep(delay)
    cls()
    print("loadiNg.....")
    time.sleep(delay)
    cls()
    print("loadinG......")
    time.sleep(delay)
    cls()
    print("Loading.......")
    time.sleep(delay)
    cls()
    print("lOading........")
    time.sleep(delay)
    cls()
    print("loAding.........")
    time.sleep(delay)
    cls()
    print("loaDing..........")
    time.sleep(delay)
    cls()
    print("loadIng..........")
    time.sleep(delay)
    cls()
    print("loadiNg..........")
    time.sleep(delay)
    cls()
    print("loadinG..........")
    time.sleep(delay)
    cls()
    
#Text User Interface
def tui():
  os.system('clear')
  print("""______           _      _____                     _               
|  _  \         | |    /  ___|                   | |              
| | | |___  _ __| | __ \ `--.  ___  __ _ _ __ ___| |__   ___ _ __ 
| | | / _ \| '__| |/ /  `--. \/ _ \/ _` | '__/ __| '_ \ / _ \ '__|
| |/ / (_) | |  |   <  /\__/ /  __/ (_| | | | (__| | | |  __/ |   
|___/ \___/|_|  |_|\_\ \____/ \___|\__,_|_|  \___|_| |_|\___|_|   
                                                                  
                                                                  """)
  print("[1] Use dork once\n[2] Use multiple dorks")
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
  print("""______           _      _____                     _               
|  _  \         | |    /  ___|                   | |              
| | | |___  _ __| | __ \ `--.  ___  __ _ _ __ ___| |__   ___ _ __ 
| | | / _ \| '__| |/ /  `--. \/ _ \/ _` | '__/ __| '_ \ / _ \ '__|
| |/ / (_) | |  |   <  /\__/ /  __/ (_| | | | (__| | | |  __/ |   
|___/ \___/|_|  |_|\_\ \____/ \___|\__,_|_|  \___|_| |_|\___|_|   
                                                                  
                                                                  """)
  with open('targets.txt', 'r') as s:
    query = s.read()
    for j in search(query):
      print(Fore.GREEN + '{}'.format(j))
      print(Fore.LIGHTYELLOW_EX + "--------------------------------")

#Arguments
parser = argparse.ArgumentParser()

#Take from txt
parser.add_argument('-d', '--dictionary', action='store_true', 
help="Takes infomation from 'targets.txt' and searches them!")

#Opens tui version (buggy)
parser.add_argument('-i', '--interact',
action='store_true',
help="Runs the tui version of this tool! ")
args = parser.parse_args()

#Detect correct args
if args.dictionary:
    loader()
    dictionary()

if args.interact:
  loader()
  tui()


