import requests
from bs4 import BeautifulSoup
import csv
import re


def findLinks(page):
    regex = re.compile(r'<a href="(https://www.facebook.com.+?)" target')
    result = regex.findall(page)
    if result==[]:
        regex = re.compile(r'<a href="(https://facebook.com.+?)" target')
        result = regex.findall(page)

    return result[0]

url = "https://www.bandsintown.com/?came_from=257&hide_homepage=true&sort_by_filter=Number+of+RSVPs"
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content,'html.parser')
anchor = soup.findAll('a',{'class':"_3UX9sLQPbNUbfbaigy35li"})

filename = 'output.csv'
fields = ["Event Date", "Concert Name", "Genre","Facebook Page","Event Poster"]
csvfile = open(filename, 'w+',newline = '')
writer = csv.writer(csvfile)
writer.writerow(fields)

for link in range(len(anchor)):
    result =[]
    urls = anchor[link].get('href')
    req = requests.get(urls)
    html = req.content
    soup1 = BeautifulSoup(html,"html.parser")
    
    date = soup1.find("div", {"class":"_1pJ33vJuFJKauIgYOkCleu"})
    concert_name = soup1.find("div", {"class":"_31N2YODa7GUJWZgNSc_AWl"}) 
    name = soup1.find("h1", {"class":"_2ewREFNd4qGa6u_PLBCY9F"})
    genre = soup1.find("div", {"class":"_1v6hYzlTV-hB2ZkAb6CiCv"})
    facebook_links = findLinks(req.text)
    image = soup1.find_all(attrs={"class" : "_3FxoLllHIYDsTLMcW1mAl8"})
    res = str(image[0])
    end = (len(res))-7
    start = (res.index('src'))+5
    image_link = res[start:end]

    if date:
        if concert_name==None:
            concert_name = "None"
            result.append("".join(date.text))
            result.append("".join(concert_name))
            result.append("".join(genre.text))
            result.append("".join(facebook_links))
            result.append("".join(image_link))
        else:
            result.append("".join(date.text))
            result.append("".join(concert_name.text))
            result.append("".join(genre.text))
            result.append("".join(facebook_links))
            result.append("".join(image_link))
        writer.writerow(result)
        