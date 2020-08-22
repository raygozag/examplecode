from Bio import SeqIO
import sys
import os,binascii
from asyncore import write


def write_dict(fname,dct):
    out=open(fname,'w')
    for key in dct.keys():
        out.write(key+"\t"+dct[key]+"\n")
    out.close()




seqs=dict()

prefix=sys.argv[1].split(".")[0]
print(prefix)

out=open("/tmp/aln.fa",'w')
for record in SeqIO.parse(sys.argv[1],'fasta'):
    tmp=binascii.b2a_hex(os.urandom(15))[0:9]
    seqs[tmp]=record.id
    record.id=tmp
    record.description=""
    SeqIO.write(record,out,'fasta')
    
out.close()
    
write_dict(prefix+".dat", seqs)

