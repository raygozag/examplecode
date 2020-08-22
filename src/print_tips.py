from Bio import Phylo
import sys

tree=Phylo.read(sys.argv[1],'newick')



for leaf in tree.get_terminals():
    print(leaf)