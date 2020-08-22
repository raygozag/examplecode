from Bio import SeqIO
import sys


for record in SeqIO.parse(sys.argv[1],'fastq'):
    print(str(record.seq))