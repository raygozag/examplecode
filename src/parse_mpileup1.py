import csv
import sys
import re

data=csv.reader(open(sys.argv[1]),delimiter='\t')


for record in data:
    
    pstrin=''.join(set(re.sub("[^a-zA-Z]+", "", record[4]).upper()))
    if pstrin.strip()=="":
        continue
    print(record[1]+"\t"+pstrin[0])
