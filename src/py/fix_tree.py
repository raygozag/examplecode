from Bio import Phylo
import sys


def read_dict(fname):
    dct=dict()
    for line in open(fname):
        vals=line.strip().split("\t")
        dct[vals[0]]=vals[1]
    return dct


tree=Phylo.read(sys.argv[1],'newick')

mapping=read_dict(sys.argv[2])

for clade in tree.get_terminals():
    old=clade.name
    clade.name=mapping[old]

Phylo.write(tree,open(sys.argv[1],'w'),'newick')


