import sys
import csv


sam= csv.reader(open(sys.argv[1]),delimiter='\t')

for record in sam:
    if len(record) <7:
        continue
    print("@"+record[0]+"\n"+record[9]+"\n+\n"+record[10])
    
