import requests
from lxml import etree
import sys



namespace="{http://uniprot.org/uniprot}"

def get_entry(document):
    return document.findall("./"+namespace+"entry")[0]

entry_ids =[item.strip() for item in open(sys.argv[1])]

xmlroot_string="<uniprot xmlns=\"http://uniprot.org/uniprot\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://uniprot.org/uniprot http://www.uniprot.org/support/docs/uniprot.xsd\"/>"

root=etree.fromstring(xmlroot_string)


url = "https://www.uniprot.org/uniprot/"
for id in entry_ids:
    
    xml =requests.get(url+id+".xml")
    subroot=etree.fromstring(xml.content)
    root.append(get_entry(subroot))

tree = etree.ElementTree(root)
tree.write(sys.argv[2])


