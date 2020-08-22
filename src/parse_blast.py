import xml.etree.ElementTree as ET
import sys

def query_length(it):
    k=int(it.findall("./Iteration_query-len")[0].text)
    return k

def print_hit(el,ln):
    name=el.findall("./Hit_def")[0].text
    for hit in el.findall(".//Hsp"):
        k=int(hit.findall("./Hsp_identity")[0].text)
        print(name +"\t"+str((k/float(ln))*100))

tree = ET.parse(sys.argv[1])
root = tree.getroot()
for it in root.findall('.//Iteration'):
    ql=query_length(it)
    for hit in it.findall(".//Hit"):
        print_hit(hit,ql)
        
