import sys


chr=int(sys.argv[2])
pos=int(sys.argv[3])

#print(pos)

min=1000000000000
minsnp=0

for snp in open(sys.argv[1]):
	tokens=snp.strip().split(":")
	if chr != int(tokens[0]):
		continue
	#print(tokens[1])
	if abs(pos-int(tokens[1]))<min:
		min=abs(pos-int(tokens[1]))
		minsnp=int(tokens[1])

print(str(chr)+":"+str(minsnp)+"\t"+str(min))
