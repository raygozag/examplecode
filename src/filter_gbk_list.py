from Bio import SeqIO
import sys


keyword=sys.argv[2]

gbk=SeqIO.read(sys.argv[1],'genbank')

fts=[]

for feature in gbk.features:
    for qualifier in feature.qualifiers:
        for value in feature.qualifiers[qualifier]:
            if keyword in value.lower():
                fts.append(feature)


gbk.features = fts

SeqIO.write(gbk,open(sys.argv[3],'w'),'genbank')