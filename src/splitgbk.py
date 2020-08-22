from Bio import SeqIO
import sys

out = None
for record in SeqIO.parse(sys.argv[1],'genbank'):
    out = open(record.name+".gbk",'w')
    SeqIO.write(record,out,'genbank')
    out.close()
    