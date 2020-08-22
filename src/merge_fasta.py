from Bio import SeqIO
import sys
import re

out=open(sys.argv[2],'w')

name=sys.argv[1].split(".")[0]
seq=''
for record in SeqIO.parse(sys.argv[1],'fasta'):
    seq=seq+str(record.seq)+"N"*2

#seq=re.sub("[N]+$","",seq)

out.write(">"+name+"\n"+seq+"\n")
out.close()
