from Bio import SeqIO
import sys


for record in SeqIO.parse(sys.argv[1],'fasta'):
    id=record.id.split("|")[1]
    print(id+"\t"+str(record.seq))