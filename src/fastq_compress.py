import sys
from Bio import SeqIO
import sqlite3


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


try:
    conn = sqlite3.connect(sys.argv[2])
    c=conn.cursor()
    c.execute("CREATE TABLE data(NAME varchar(500),sequence varchar(500),quality varchar(500))")
    k=1
    name=""
    seq=""
    qual=""
    for line in open(sys.argv[1]):
        
        if k==1:
            name=line.strip()
        if k==2:
            seq=encode(line.strip())
            
        if k==4:
            qual=encode(line.strip())
            c.execute("insert into data values(?,?,?)",(name,seq,qual))
            k=1
            name=""
            seq=""
            qual=""
            continue
        k=k+1
        
        
        
    conn.commit()
    conn.close()
except Exception as e:  
    print(e)  


