from Bio import SeqIO
import sys


start=int(sys.argv[2])
end=int(sys.argv[3])

k=1

for record in SeqIO.parse(sys.argv[1],'fasta'):
    if k<start:
        continue
    if k>end:
        break
    print(">"+record.id)
    print(str(record.seq))
    k=k+1

        