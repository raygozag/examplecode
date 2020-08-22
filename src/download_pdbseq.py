import urllib
import sys

link = 'https://www.rcsb.org/pdb/download/viewFastaFiles.do?structureIdList='+sys.argv[1]+'&compressionType=uncompressed'
f = urllib.urlopen(link)           

for line in f:
    print line,