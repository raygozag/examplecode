#!/usr/bin/python

import string
from Bio import SeqIO
import sys
import re


    
def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev!='':

                if count>2:
                    entry = prev+str(count)
                    lst.append(entry)
                else:
                    entry = prev*count
                    lst.append(entry)
                    
            count = 1
            prev = character
        else:
            count = count + 1
    return "".join(lst)

out =open(sys.argv[2],'w')
for record in SeqIO.parse(sys.argv[1],'fasta'):
    out.write(">"+record.description+"\n")
    out.write(encode(str(record.seq))+"\n")
    
    

out.close()

