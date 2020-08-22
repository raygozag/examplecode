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

enzyme=sys.argv[2]

seq=Seq(get_sequence(open(sys.argv[1],"rb")),generic_dna)

rb = RestrictionBatch()

rb.add(enzyme)


res=rb.search(seq)
for key in res.keys():
    if str(key)==enzyme:
        print(sys.argv[1]+"\t"+str(len(res[key])))


