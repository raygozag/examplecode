from Bio import SeqIO
import sys


for record in SeqIO.parse(sys.argv[1],'fasta'):
    if sys.argv[2] in record.description:
        SeqIO.write(record,sys.stdout,'fasta')