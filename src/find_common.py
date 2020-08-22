from Bio import SeqIO
import sys



    
seqs=dict()





for record in SeqIO.parse(sys.argv[1],"fasta"):
    seqs[record.id]=str(record.seq).lower()
    

kmers=['atgacagtaaataaaataaagaacattttcaataatgcgacattgacta']

for kmer in kmers:
    k=0
    for key in seqs.keys():
        seq=seqs[key]
        if seq.find(kmer)>-1:
            name=key.split(".")[0]
            print("mv seqs/good_pO157/"+name+".dna good/")
