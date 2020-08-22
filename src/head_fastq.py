from Bio import SeqIO
import sys


top=int(sys.argv[1])

k=1
out=open(sys.argv[3],'w')
for record in SeqIO.parse(sys.argv[2],'fastq'):
    if k<=top:
        SeqIO.write(record,out,'fastq')
    else:
        break
    k=k+1
out.close()
