from Bio import SeqIO
import sys


lengtx=int(sys.argv[2])


out=open(sys.argv[3],'w')
for record in SeqIO.parse(sys.argv[1],'fasta'):
    if len(str(record.seq))<lengtx:
        continue
    SeqIO.write(record,out,'fasta')

out.close()

