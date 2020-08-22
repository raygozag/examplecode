import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.SeqFeature import SeqFeature
import xml.etree.ElementTree as ET



def get_sequence(file):
    byte = f.read(1)
    seq=""
    printk=False
    while byte != "":
        byte = file.read(1)
        pos=ord(byte)
        
        if pos==2:
            break
        if printk==True:
            seq=seq+chr(ord(byte))
            
        if pos==31:
            printk=True
    return seq


def get_xml(file):
    byte = f.read(1)
    seq=""
    printk=False
    while byte != "":
        byte = file.read(1)
        pos=ord(byte)
        if pos==60:
            byte = file.read(1)
            pos=ord(byte)
            if pos==63:
                return("<?"+file.readline().strip())
                
def get_features(file):
    ftxml=get_xml(file)
    features=[]
    root=ET.fromstring(ftxml)
    print(root.tag)
    for feature in root.findall('Feature'):
        if feature.attrib['type']=="CDS":
            print feature.attrib['name']
        
        
    return features


f = open(sys.argv[1], "rb")

sname=sys.argv[1].split(".")[0]
try:
    seq=get_sequence(f)
    seqdata=SeqRecord(Seq(seq,generic_dna),id=sname,name=sname)
    seqdata.features=get_features(f)
    SeqIO.write(seqdata,open("test.gbk",'w'),'genbank')
finally:
    f.close()