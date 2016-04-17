from bs4 import BeautifulSoup
import os
import urllib2
import time
import re
import sys

def notify(message, url):

    exString = 'notify-send -i $(pwd)/oatmeal.png -t 3000 %s %s' % (message, url)
    os.system(exString)

if __name__ == '__main__':

    with open("cName") as f:
        currentName = f.readline()

    while True:

        oatmeal = urllib2.urlopen("http://theoatmeal.com/comics").read()
        soup = BeautifulSoup(oatmeal, 'html.parser')

        link = soup.find_all("a", href=re.compile("^/comics/"), recursive=True)[0]

        if link['href'][8:] != currentName:
            u = "http://theoatmeal.com/comics/" + link["href"][8:]
            print u
            notify("NEW COMIC", u)
            currentName = link["href"][8:]

            with open("cName", "w+") as f:
                f.write(currentName)

        time.sleep(3600)
