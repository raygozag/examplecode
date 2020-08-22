import requests
from lxml import etree
from lxml.etree import fromstring
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import sys


namespace="{http://uniprot.org/uniprot}"

def find_signal(xmlo):
    end=-1
    
    for signal in xmlo.findall('.//'+namespace+'feature[@type="signal peptide"]'):
       end=int(signal.findall('.//'+namespace+'end')[0].attrib["position"])
       # print(signal)
    return(end)


out=open(sys.argv[2],'w')      

for record in SeqIO.parse(sys.argv[1],'fasta'):
    id = record.id.split("|")[1].strip()
    print(id)
    req = requests.request('GET', "https://www.uniprot.org/uniprot/"+id+".xml")

    xml_obj = etree.fromstring(str(req.text))
    end=find_signal(xml_obj)
    if end>0:
        seq=str(record.seq)
        record.seq=Seq(seq[end+1:],generic_dna)
    
    SeqIO.write(record,out,'fasta')