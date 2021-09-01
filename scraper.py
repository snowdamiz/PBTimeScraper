from bs4 import BeautifulSoup
import urllib.request
import urllib

# open login credentials file
# convert file into tuple
# create uname and pword variables
with open('config.txt') as file:
    my_list = [x.rstrip() for x in file]
    uname = my_list[0]
    pword = my_list[1]

# open chassis list
# convert file into tuple
with open('chassis.txt') as file:
    my_list = [x.rstrip() for x in file]

# open entry url
with urllib.request.urlopen("http://suppliers.www.uprr.com/iem/secure/jas/") as response:
    html = response.read()

soup = BeautifulSoup(html, 'lxml')

print(soup)