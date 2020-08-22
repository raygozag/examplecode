from Bio import Phylo
import sys

tree=Phylo.read(sys.argv[1],'newick')


ids=[]
for leaf in tree.get_terminals():
    ids.append(str(leaf).strip())
    
for record in SeqIO.parse(sys.argv[2],'fasta'):
    