from Bio import SeqIO
import sys


list=[item.strip() for item in open(sys.argv[1])]

for record in SeqIO.parse(sys.argv[2],'fasta'):
    if record.id in list:
        print(">"+record.id+"\n"+str(record.seq))