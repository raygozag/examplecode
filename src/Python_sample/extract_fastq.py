from Bio import SeqIO
import sys


list=[item.strip() for item in open(sys.argv[1])]

out=open(sys.argv[3],'w')
for record in SeqIO.parse(sys.argv[2],'fastq'):
    if record.id in list:
        SeqIO.write(record,out,'fasta')

out.close()
