from Bio import SeqIO
import sys


ids=[item.strip() for item in open(sys.argv[2])]

gbk=SeqIO.read(sys.argv[1],'genbank')

fts=[]

out=open(sys.argv[3],'w')

for feature in gbk.features:
    if feature.type=="CDS":
        if "locus_tag" in feature.qualifiers:
            if feature.qualifiers['locus_tag'][0].strip() in ids:
                locus_tag=feature.qualifiers['locus_tag'][0]
                product=""
                if "product" in feature.qualifiers:
                    product=feature.qualifiers['product'][0]
                seq=""
                if "translation" in feature.qualifiers:
                    seq=feature.qualifiers['translation'][0].strip()
                else:
                    seq = feature.extract(gbk).translate(to_stop="true",table=11)
                out.write(">"+locus_tag+" "+product+ "\n"+seq+"\n")

out.close()



