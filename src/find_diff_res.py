from Bio.Restriction.Restriction import RestrictionBatch
from Bio.Seq import Seq
import os
from Bio.Alphabet import generic_dna
import sys



def get_enzymes(seq,rb):
    ez=[]
    res=rb.search(seq)
    for key in res.keys():
        if len(res[key])>0:
            ez.append(str(key))
    return set(ez)

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


f = open(sys.argv[1], "rb")

homedir = os.environ['HOME']+"/"

seq1=Seq(get_sequence(open(sys.argv[1],"rb")),generic_dna)
seq2=Seq(get_sequence(open(sys.argv[2],"rb")),generic_dna)


enzymes=[item.strip() for item in open(homedir+"."+sys.argv[3])]

rb = RestrictionBatch()

for enzyme in enzymes:
    rb.add(enzyme)


enzymes1 = get_enzymes(seq1,rb)

enzymes2 = get_enzymes(seq2,rb)


print(enzymes1-enzymes2)