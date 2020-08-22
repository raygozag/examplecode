from Bio import SeqIO
import sys
import gzip


contig_rd=SeqIO.read(sys.argv[1],"fasta")
contig=str(contig_rd.seq)
contig=contig[len(contig)-200:]
name=contig_rd.description
k=1
for record in gzip.open(sys.argv[2],'rt'):
    seq1=record.strip()
    sub=seq1[:50]
    k=1
    
    
    pos=contig.find(sub)
    if pos!=-1:
        ovh=(len(contig))-(pos+len(seq1))
        if ovh<0:
            print(">seq"+str(k)+"\n"+str(record.strip()))
        
    k=k+1
    

#print(str(len(contig))+"\t"+str(pos)+"\t"+str(len(seq1))+"\t"+str(pos+len(seq1)))