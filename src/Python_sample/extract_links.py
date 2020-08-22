from lxml import html
import requests

page = requests.get('https://www.ebi.ac.uk/genomes/phage.html')
tree = html.fromstring(page.content)

fastal=tree.xpath("//a[contains(text(),'fasta')]")
out=open("phagesembl.fasta",'w')
for element in fastal:
    print(element.attrib["href"])
    page2 = requests.get(element.attrib["href"])
    out.write(page2.content.strip()+"\n")

out.close()