# WebScraping Using BeautifulSoup

# Description

 It is a simple python project to scrap the data from a website.
 It extracts all the required data from a given url and feed into csv file.
 
# Installation

1. pip install requests
2. pip install bs4
3. pip install html5lib

# Usage

  It imports all required modules
  
    . import requests
    . from bs4 import BeautifulSoup
    . import csv
    . import re
    
  The get() method sends a GET request to the specified url.
  
     r = requests.get(url) 
  
  It gives the content of the response in bytes.
  
    content = r.content
    
  With this soup object, you can navigate and search through the HTML for data that you want.
  
    soup = BeautifulSoup(content,'html.parser')
    
  Find all anchor tags related to particular class id.
  
    anchor = soup.findAll('a',{'class':"_3UX9sLQPbNUbfbaigy35li"})
    
  Creating csv file and setting headers
  
    csvfile = open(filename, 'w+',newline = '')
    writer = csv.writer(csvfile)
    writer.writerow(fields)  
