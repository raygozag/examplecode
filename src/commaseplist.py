import os
import sys

pattern =sys.argv[1]

fs=[]

for file in os.listdir("."):
	if pattern in str(file):
		fs.append(str(file))

fs.sort()
print(",".join(fs))