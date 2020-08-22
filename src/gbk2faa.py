from Bio import SeqIO
import sys




out = open(sys.argv[2],'w')
cnt=0
for gbk in  SeqIO.parse(sys.argv[1],'genbank'):
    for feature in gbk.features:
        if feature.type=="CDS":
            cnt=cnt+1
            id=gbk.name+"_"+str(cnt)
            if "locus_tag" in feature.qualifiers:
                id=feature.qualifiers["locus_tag"][0]
            if "translation" in feature.qualifiers:
                out.write(">"+id+"\n"+feature.qualifiers['translation'][0]+"\n")
            else:
                out.write(">"+id+"\n"+str(feature.extract(gbk).seq.translate(to_stop=True,table=11))+"\n")

out.close()
