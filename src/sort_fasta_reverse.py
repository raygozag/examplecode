from Bio import SeqIO
import sys

def sort_fasta(item):
    return len(str(item.seq))

seqs=[item for item in SeqIO.parse(sys.argv[1],'fasta')]


seqs.sort(reverse=True,key=sort_fasta)


out=open(sys.argv[2],'w')
for record in seqs:
    SeqIO.write(record,out,'fasta')

out.close()
