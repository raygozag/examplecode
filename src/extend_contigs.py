from Bio import SeqIO
import sys


contigs=[]

for record in SeqIO.parse(sys.argv[1],'fasta'):
    contigs.append(str(record.seq))