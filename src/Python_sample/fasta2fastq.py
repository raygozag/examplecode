from Bio import SeqIO
import sys


readlen=int(sys.argv[2])
out= open(sys.argv[3],'w')
readn=0
for record in SeqIO.parse(sys.argv[1],'fasta'):
    seq=str(record.seq)
    for i in range(0,len(seq)-readlen,80):
        for i in range(1,5):
            readn=readn+1
            out.write("@read"+str(readn)+"\n"+seq[i:i+readlen]+"\n+\n"+"I"*readlen+"\n")
        
out.close()