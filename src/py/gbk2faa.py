from Bio import SeqIO
import sys



gbk = SeqIO.read(sys.argv[1], 'genbank')


out = open(sys.argv[2],'w')

for feature in gbk.features:
    if feature.type=="CDS":
        if "gene" in feature.qualifiers.keys():
            out.write(">"+feature.qualifiers['gene'][0]+"\n")
        else:
            out.write(">"+feature.qualifiers['locus_tag'][0]+"\n")
            
        
        if "translation" in feature.qualifiers.keys():
            out.write(feature.qualifiers['translation'][0]+"\n")


out.close()