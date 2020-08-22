from Bio import SeqIO
import sys


seq=sys.argv[2].upper()

for record in SeqIO.parse(sys.argv[1],'fastq'):
    seq1=str(record.seq)
    if seq1.find(seq)>-1:
        print record.id
        print str(record.seq)
        continue
    seq1=str(record.seq.reverse_complement())
    if seq1.find(seq)>-1:
        print record.id
        print str(record.seq)
        continue