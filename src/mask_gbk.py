from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import sys
import csv


out=open(sys.argv[2],'w')

for fas in SeqIO.parse(sys.argv[1],'genbank'):

    seq=list(str(fas.seq))

    for feature in fas.features:
        if feature.type.lower()=="rrna":
            start=feature.location.start
            end=feature.location.end
            ln=end-start
            seq[start:end]="N"*ln

            fas.seq=Seq("".join(seq),generic_dna)

            SeqIO.write(fas,out,'fasta')
            
out.close()