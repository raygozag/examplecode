#!/usr/bin/python

import re
from Bio import SeqIO
import sys
import time
import urllib2
from urllib2 import HTTPError

ldone =[line.rstrip('\n').strip() for line in  open("donem.txt","rU")]
genome = SeqIO.read(sys.argv[1],'genbank')
out = open('sigma_subtilis_all.txt','a')
for feature in genome.features:
	if feature.type=="gene":
		locus_tag = feature.qualifiers['locus_tag'][0]
		print locus_tag
		if locus_tag in ldone:
			continue
		if "gene" in feature.qualifiers:
			try:
				gene = feature.qualifiers["gene"][0].capitalize()
				gene = gene[:-1]+gene[-1].upper()
				
				response = urllib2.urlopen('http://subtiwiki.uni-goettingen.de/wiki/index.php/'+gene)

				html = response.read()
				
				lines = html.split("\n")
				found=False
				#print lines
				for line in lines:
					if "Sigma factor" in line:
						m = re.findall("title=\"[A-Z|a-z]+\"",line)
						if len(m)>0:
							print m
							out.write(locus_tag+"\t"+gene)
							for item in m:
								out.write("\t"+item.replace("\"","").replace("title=",""))
							out.write("\t"+str(len(m))+"\n")
							out.flush()
							found=True
				
				
				if not found:
					out.write(locus_tag+"\t"+gene+"\t"+"N/F"+"\n")
			except HTTPError:
				continue
		else:
			out.write(locus_tag+"\t"+gene+"\t"+"N/F"+"\n")
		time.sleep(3)

out.close()
		
			
			
