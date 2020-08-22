import re
from Bio import SeqIO
import sys

seq=SeqIO.read(sys.argv[1],'fasta')

prot=str(seq.seq.translate(table=11,to_stop=True))[1:]



