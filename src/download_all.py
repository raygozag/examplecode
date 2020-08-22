from bs4 import BeautifulSoup
import requests


def download_file(fname):
    url="https://faculty.washington.edu/heagerty/Courses/VA-longitudinal/private/"
    r=requests.get(url+fname)
    out=open(fname,"wb")
    out.write(r.content)
    out.close()

url="https://faculty.washington.edu/heagerty/Courses/VA-longitudinal/private/"
r=requests.get(url)

soup=BeautifulSoup(r.text,features="lxml")

k=1

for link in soup.findAll("a"):
    if "." not in link['href']:
        continue
    fname=link['href']
    print(fname)
    download_file(fname)