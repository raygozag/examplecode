import csv
import sys



out=open(sys.argv[2],'w')

data=csv.reader(open(sys.argv[1]),delimiter='\t')

for record in data:
    out.write(">"+record[0]+"\n"+record[9]+"\n")

out.close()