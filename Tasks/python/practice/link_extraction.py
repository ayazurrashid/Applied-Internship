import requests
import urllib
from bs4 import BeautifulSoup
links=list()
url = 'http://www.jkerationghat.tk/reg.html'
r = requests.get(url)
text=r.text
file=open('source.txt',"w")
file.write(text)
file.close()
file=open('source.txt',"r")
f=file.read()
soup = BeautifulSoup(f)
links = soup.find_all('a')

for i in links:
    link = i.get('href',None)
    if link is not None:
        print(link)