from Bio import SeqIO
import sys

suffix="/0"
outname=""
if "_1." in sys.argv[1]:
    suffix="/1"
    outname=sys.argv[1].replace("_1.","_1R.")
if "_2." in sys.argv[1]:
    suffix="/2"
    outname=sys.argv[1].replace("_2.","_2R.")

out=open(outname,'w')
print(sys.argv[1])

for record in SeqIO.parse(sys.argv[1],'fastq'):
    record.id=record.id+suffix
    record.description=""
    SeqIO.write(record,out,"fastq")

out.close()
