#!/usr/bin/python
'''
Leechd - find your stolen items

Leechd tries to find your stolen item on Ricardo, a Swiss e-shopping plattform.
Once a candidate is found, the url is printed in the console.

Author : Christoph Lauper
Version: 0.1
'''
from lxml import html
import urllib2 as urllib
import time
import threading
import datetime

''' main class '''
class Leechd():
    isRunning  = False
    timeOut    = 5
    foundItems = []

    # constructor
    ## @arg     searchObject    the object to be searched
    ## @mod     none
    ## @ret     none
    def __init__(self, searchObject):
        self.searchObject  = searchObject
        self.url = "https://www.ricardo.ch/search/index/"+ \
               "?SearchId=yY2dSnIKLFW-nnvxIxWOMr&SearchOneOf="+ \
               searchObject.searchSentence+ \
               "&UseDescription=True&Zip="+searchObject.zipCode+ \
               "&Range="+searchObject.radius+"&ar=8&AreaCountryNr="+ \
               searchObject.areaCountryNr
    # run
    ## @arg     none
    ## @mod     self.foundItems
    ## @ret     none
    def run(self):
        if self.isRunning:
            return
        self.isRunning = True
        while self.isRunning:
            page  = html.fromstring(urllib.urlopen(self.url).read())
            links = page.xpath('//div[@class="ric-main-content"]//a/@href')
            for link in links:
                if link not in self.foundItems:
                    self.foundItems.append(link)
                    print "[+]" + "http://www.ricardo.ch" + link
            time.sleep(self.timeOut)

    # stop
    ## @arg     none
    ## @mod     self.isRunning
    ## @ret     none
    def stop(self):
        self.isRunning = False

''' defines an object to search '''
class SearchObject():
    def __init__(self, searchSentence, zipCode, radius, areaCountryNr="2"):
       self.searchSentence = searchSentence
       self.zipCode        = zipCode
       self.radius         = radius
       self.areaCountryNr  = areaCountryNr

''' entry point '''
if __name__ == '__main__':
    searchObject = SearchObject("velo%20fahrrad%20gangurru", "8400", "20")
    leechd       = Leechd(searchObject)
    numDays      = 30

    thread = threading.Thread(target = leechd.run)
    thread.start()

    while True:
        pass

    leechd.stop()
    thread.join()
