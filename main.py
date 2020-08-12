import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bandsintown.com/?came_from=257&hide_homepage=true&sort_by_filter=Number+of+RSVPs"
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content,'html.parser')
anchor = soup.find_all('a')

filename = 'output.csv'
fields = ["Event Date", "Concert Name", "Genre"]
csvfile = open(filename, 'w+',newline = '')
writer = csv.writer(csvfile)
writer.writerow(fields)

for link in range(36,len(anchor)-10):
    result =[]
    urls = anchor[link].get('href')
    req = requests.get(urls)
    html = req.content
    soup1 = BeautifulSoup(html,"html.parser")
    
    date = soup1.find("div", {"class":"_1pJ33vJuFJKauIgYOkCleu"})
    concert_name = soup1.find("div", {"class":"_31N2YODa7GUJWZgNSc_AWl"}) 
    name = soup1.find("h1", {"class":"_2ewREFNd4qGa6u_PLBCY9F"})
    genre = soup1.find("div", {"class":"_1v6hYzlTV-hB2ZkAb6CiCv"})
    if date:
        if concert_name==None:
            concert_name = "None"
            result.append("".join(date.text))
            result.append("".join(concert_name))
            result.append("".join(genre.text))
        else:
            result.append("".join(date.text))
            result.append("".join(concert_name.text))
            result.append("".join(genre.text))
        writer.writerow(result)
        