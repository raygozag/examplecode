#!/usr/bin/python

## Simple fastq compressor using a modified version of run-length encoding



import string
from Bio import SeqIO
import sys
import re

def get_qual_string(quals): 
    q=""
    for qual in quals:
        q=q+chr(qual+57)
    return q
    
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
for record in SeqIO.parse(sys.argv[1],'fastq'):
    out.write("@"+record.description+"\n")
    out.write(encode(str(record.seq))+"\n")
    get_qual_string(record.letter_annotations['phred_quality'])
    out.write(encode(get_qual_string(record.letter_annotations['phred_quality']))+"\n")
    

out.close()

