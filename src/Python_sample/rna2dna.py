from Bio import SeqIO
import sys


out=open(sys.argv[2],'w')

for record in SeqIO.parse(sys.argv[1],'fasta'):
    record.seq = record.seq.back_transcribe()
    SeqIO.write(record,out,'fasta')

out.close()

