from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import sys
import csv



def read_data(fname):
    d=dict()
    data=csv.reader(open(fname),delimiter='\t')
    for record in data:
        d[int(record[0])]=record[1]
    return d

gbk=SeqIO.read(sys.argv[1],'genbank')

seq=list("N"*len(str(gbk.seq)))



data = read_data(sys.argv[2])

for key in data.keys():
    try:
        seq[key-1]=data[key]
    except:
        
        print(str(key)+"\t"+data[key])

    
gbk.seq=Seq(''.join(seq),generic_dna)

SeqIO.write(gbk,open(sys.argv[3],'w'),'genbank')




