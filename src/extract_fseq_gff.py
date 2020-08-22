from Bio import SeqIO
import sys
import csv

def load_fasta_dict(fname):
    seqs=dict()
    for record in SeqIO.parse(fname,'fasta'):
        seqs[record.id]=record
    return seqs

seqs=load_fasta_dict(sys.argv[1])

data=csv.reader(open(sys.argv[2]),delimiter="\t")

for record in data:
    sq=str(seqs[record[0]].seq)
    print(">"+record[0])
    print(sq[int(record[3]):int(record[4])])
