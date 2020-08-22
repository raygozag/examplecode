import sys
import re


for line in open(sys.argv[1]):
	line2 =re.sub(r"\(Fi.*\)\.", "",line.strip())
	print(line2)