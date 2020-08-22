from Bio import SeqIO
import sys


for record in SeqIO.parse(sys.argv[1],'fasta'):
    out=open(record.id+".fasta",'w')
    SeqIO.write(record,out,'fasta')
    out.close()
    