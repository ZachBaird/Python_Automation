# Dev: Zach Baird
# Purpose:
#  This file's code is derived from Automate the Boring Stuff from the fantastic author Al Sweigart.
#  The resource online can be found here: https://automatetheboringstuff.com :but I strongly encourage you to buy
#  his book or Udemy course to support him. This file is Python code scraping the web.
#
# How to Use:
#  Each little example is encapsulated in its own function. To see an example in action, simply call the function
#  at the bottom of the page. Feel free to play with its code to change the results and see what web scraping in Python
#  can truly do.
#

import requests
import bs4


def basicBrowserOpen():
    # Import webbrowser to use this. Web Browser is a simpler module than its counterparts.
    webbrowser.open('http://inventwithpython.com/')


def basicRequestsGet():
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

    print(res.status_code == requests.codes.ok)


def requestsSaveFileLocally():
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.raise_for_status()
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)

    playFile.close()


def noStarch():
    res = requests.get('http://nostarch.com')
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text)
