

from bs4 import BeautifulSoup
import requests 

base_url="https://ftp.ncbi.nih.gov/genomes/archive/old_genbank/Bacteria/"

headers = {'Accept-Encoding': 'identity'}
r = requests.get(base_url, headers=headers)
html_doc=r.content

out=open("frns.txt",'w')
def get_rna_file(url,file):
    r = requests.get(url, headers=headers)
    
    html_doc=r.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    for link in soup.find_all('a'):
       
        if "frn" in str(link.text):
            file.write("wget "+url+link.text+"\n")
            file.flush()
            break;

soup = BeautifulSoup(html_doc, 'html.parser')


for link in soup.find_all('a'):
    if link.text=="Parent Directory":
        continue
    get_rna_file(base_url+link.text,out)
    out.flush()

out.close()
