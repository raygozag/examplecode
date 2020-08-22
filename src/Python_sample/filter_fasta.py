from Bio import SeqIO
import sys


keyword=sys.argv[2]


out=open(sys.argv[3],'w')
for record in SeqIO.parse(sys.argv[1],'fasta'):
    if keyword.strip() not in record.description.lower():
        continue
    SeqIO.write(record,out,'fasta')

out.close()

