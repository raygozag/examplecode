import csv
import sys


out = open(sys.argv[2],'w')

data = csv.reader(open(sys.argv[1]),delimiter=" ")

for record in data:
	m=record[1]
	record[1]=record[0]
	record[0]=m
	out.write(" ".join(record)+"\n")

out.close()