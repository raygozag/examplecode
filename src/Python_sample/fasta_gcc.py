from Bio import SeqIO
from Bio.SeqUtils import GC
import sys


for record in SeqIO.parse(sys.argv[1],'fasta'):
    print(record.id+"\t"+str(len(str(record.seq)))+"\t"+str(GC(str(record.seq))))