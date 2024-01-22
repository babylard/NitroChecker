import time
import random, string
import webbrowser
import requests

blue="\33[0;34m"
cyan="\033[1;36m"
purple="\033[0;35m" 
green="\033[0;32m"
orange ="\033[0;33m"
pink = "\033[1;31m"
darkblue = "\033[1;34m"
white = "\033[1;37m"
gray = "\033[1;30m"
red = "\033[0;31;47m"

num=input('Input how many links you would like to check: ')
print("---------------------------------------------------------------")

f=open("links.txt","w", encoding='utf-8')

with open("links.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(green," Working | {} ".format(line.strip("\n")))
            break
        else:
        	print(darkblue," Expired/Used | {} ".format(line.strip("\n")))

input("Done. Press Enter to exit.")