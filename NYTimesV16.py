#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:03:31 2019

Add new column with Datetime for current stories for every row. 
Add Column that says NYTIMES for every headline pulled here.

Updated on Sat June 29 10:40:00 2019
Row added for NYT and datetime

"""


import re
import csv
import requests
from datetime import datetime
from datetime import date
from bs4 import BeautifulSoup
from shutil import copyfile

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
currentDT = str(datetime.now())
currentDate = date.today().strftime("%m/%d/%y")
mylist = []
mylist2 = []


for allh2 in soup.findAll('h2'):
    allh3 = allh2.text.encode('ascii', 'ignore').decode('ascii')
    mylist.append(allh3)
mylist.remove('Site Index')
mylist.remove('Site Information Navigation')
    
for story in mylist:
    mylist2 = (story,currentDT,currentDate)

    
with open('NYTimesTwo.csv', 'a', newline='') as open_file:
    wr = csv.writer(open_file, delimiter=',', dialect='excel')
    #wr.writerows('')
    for story in mylist:
        mylist2 = (story,currentDT,currentDate, 'NYT')
        wr.writerows([mylist2])
    wr.writerows('\n')

copyfile('NYTimesTwo.csv', 'NYTimesWork.csv')    
        
        
        
