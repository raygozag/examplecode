from Bio import SeqIO
import sys




out = open(sys.argv[2],'w')
cnt=0
for gbk in  SeqIO.parse(sys.argv[1],'genbank'):
    for feature in gbk.features:
        if feature.type=="CDS":
            cnt=cnt+1
            out.write(">"+gbk.name+"_"+str(cnt)+"\n"+str(feature.extract(gbk).seq.translate(to_stop=False,table=11))+"\n")


out.close()