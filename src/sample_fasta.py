from Bio import SeqIO 
import sys
import random

seqs=[item for item in SeqIO.parse(sys.argv[1],'fasta')]

random.shuffle(seqs)

sample=seqs[:20]

out=open(sys.argv[2],'w')

for record in sample:
    SeqIO.write(record,out,'fasta')

out.close()
