from Bio import SeqIO 
import sys
import random


def fastalen(record):
    return(len(str(record.seq)))
seqs=[]

for record in SeqIO.parse(sys.argv[1],'fasta'):
    if len(str(record.seq))< 1000:
        seqs.append(record)

seqs.sort(key=fastalen)
#random.shuffle(seqs)
limit=int(sys.argv[3])
sample=seqs[:limit]

out=open(sys.argv[2],'w')

for record in sample:
    SeqIO.write(record,out,'fasta')

out.close()
