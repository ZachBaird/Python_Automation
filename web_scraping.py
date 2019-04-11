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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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


def seleniumBrowser():
    browser = webdriver.Firefox()
    #browser = webdriver.Chrome()
    print(type(browser))
    browser.get('http://inventwithpython.com')


def seleniumBookSearch(tag_search):
    browser = webdriver.Firefox()
    browser.get('http://inventwithpython.com')
    try:
        elem = browser.find_element_by_class_name(tag_search)
        print('Found <%s> element with that class name!' % (elem.tag_name))
    except:
        print('Was not able to find an element with that name.')


def seleniumTestBrowse(url, link_text):
    browser = webdriver.Firefox()
    browser.get(url)

    linkElems = browser.find_elements_by_link_text(link_text)

    linkElem = linkElems[9]
    linkElem.click()


def seleniumTestForm(url, link_text):
    browser = webdriver.Firefox()
    browser.get(url)

    linkElems = browser.find_elements_by_link_text(link_text)
    linkElem = linkElems[9]
    linkElem.click()

    # firstElem = browser.find_element_by_id(id here)
    #firstElem.send_keys('John Doe')
