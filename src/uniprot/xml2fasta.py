from lxml import etree
import sys

def get_accession(entry):
    access=entry.findall(".//"+namespace+"accession")[0]
    return(access.text)
    
def get_sequence(entry):
    seq=entry.findall(".//"+namespace+"sequence")[0]
    return(seq.text)


namespace="{http://uniprot.org/uniprot}"
tree = etree.parse(sys.argv[1])


for entry in tree.findall("./"+namespace+"entry"):
    accession=get_accession(entry)
    sequence=get_sequence(entry)
    if accession!=None and sequence!=None:
        print(">"+accession.strip()+"\n"+sequence.strip())