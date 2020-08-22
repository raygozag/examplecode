import csv
import sys


data=csv.reader(open(sys.argv[1]),delimiter='\t')

start=-1
end=-1
inter=0
for record in data:
    if int(record[2])>0 and inter==0:
        start=int(record[1])
        inter=1
        continue
    if int(record[2])==0 and inter==1:
        print(str(start)+"\t"+record[1])
        inter=0
        