from Bio import SeqIO
import sys


done=[line.strip() for line in open(sys.argv[1])]

out=open(sys.argv[3],'a+')
j=0
don=open(sys.argv[1],'a')
for record in SeqIO.parse(sys.argv[2],'fasta'):
    j=j+1
    if record.id in done:
        continue
    print(str(j)+"\t"+record.description)
    goodx=raw_input("Good ? ")
    if goodx==1:
        don.write(record.id+"\n")
        SeqIO.write(record,out,'fasta')
        out.flush()
        don.flush()

out.close()
    