# another example: 
# https://github.com/douglasmiranda/splinter-examples/blob/master/another_examples/screenshot.py

# more here: 
# http://splinter.readthedocs.io/en/latest/tutorial.html

# pip install splinter
# brew install geckodriver
from splinter import Browser
import csv
from BeautifulSoup import BeautifulSoup
from time import sleep

player = 'michael+thomas'
team = 'saints'

with Browser() as browser:
    # Visit URL
    url = "https://www.google.com/search?q=" + player + "+" + team + "&safe=active&source=lnt&tbs=cdr%3A1%2Ccd_min%3A7%2F1%2F2016%2Ccd_max%3A9%2F10%2F2016&tbm=nws"
    browser.visit(url)
    sleep(45)
    html = browser.html
    print(html)
    soup = BeautifulSoup(html)

    for line in soup.findAll('a', href=True):
        # Appending to csv files
        with open('links.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow([time.strftime("%m/%d/%Y"), 'michael thomas', line])

    for link in soup.find_all('a'):
        print(link.get('href'))

