from bs4 import BeautifulSoup
from urllib.request import urlopen



soup = BeautifulSoup(open("/Users/raygoza/tmp/olink.txt"),features="html.parser")


for link in soup.find_all('a'):
    print(link.get("href"))


