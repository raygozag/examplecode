from Bio import SeqIO
import sys

ids=[item.strip() for item in open(sys.argv[1])]

out = open(sys.argv[3],'w')

for record in SeqIO.parse(sys.argv[2],'fasta'):
    if record.id in ids:
        v=ids.index(record.id)
        del ids[v]
        continue
    SeqIO.write(record,out,'fasta')

out.close()