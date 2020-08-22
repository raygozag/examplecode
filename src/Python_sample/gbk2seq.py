from Bio import SeqIO
import sys




out = open(sys.argv[2],'w')

for gbk in  SeqIO.parse(sys.argv[1],'genbank'):
    out.write(">"+gbk.name+"\n"+str(gbk.seq)+"\n")


out.close()