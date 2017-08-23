#!/usr/bin/python

# pip install splinter
# brew install geckodriver
from splinter import Browser
import csv
import time

with Browser() as browser:
    # Visit URL
    url = "http://www.google.com"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnK')
    # Interact with elements
    button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        # Appending to csv files
        with open('found.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(['Yes the official website was found!', time.strftime("%m/%d/%Y")])
    else:
        # Appending to csv files
        with open('found.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(['No the official website was not found!', time.strftime("%m/%d/%Y")])