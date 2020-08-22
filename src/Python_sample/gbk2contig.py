from Bio import SeqIO
import sys
import re

seq=str(SeqIO.read(sys.argv[1],'genbank').seq)

out=open(sys.argv[2],'w')

contigs= re.sub("^N|N$","",re.sub('[N]+',"N",seq)).split("N")
k=1
for contig in contigs:
    out.write(">contig_"+str(k)+"\n"+contig+"\n")
    k=k+1

out.close()