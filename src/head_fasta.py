from Bio import SeqIO
import sys


top=int(sys.argv[1])

k=1
out=open(sys.argv[3],'w')
for record in SeqIO.parse(sys.argv[2],'fasta'):
    if k<=top:
        SeqIO.write(record,out,'fasta')
    else:
        break
    k=k+1
out.close()
