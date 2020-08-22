from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import sys
import csv




fas=SeqIO.read(sys.argv[1],'fasta')

seq=list(str(fas.seq))

gff=csv.reader(open(sys.argv[2]),delimiter="\t")

for record in gff:
    if record[0].startswith("#"):
        continue
    start=int(record[3])-1
    end=int(record[4])-1
    ln=end-start
    seq[start:end]="N"*ln

fas.seq=Seq("".join(seq),generic_dna)

SeqIO.write(fas,open(sys.argv[3],'w'),'fasta')