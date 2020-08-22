from Bio import SeqIO
import sys
import re


n=re.compile("[n]+")

for record in SeqIO.parse(sys.argv[1],'fasta'):
    seq=str(record.seq).lower()
    print(record.description)
    it=n.finditer(seq)
    for m in it:
        print(str(m.span()[0])+"\t"+str(m.span()[1])+"\t"+str(m.span()[1]-m.span()[0]))
    