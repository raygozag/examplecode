from os import listdir
from os.path import isfile, join
import sys


manifest=open(sys.argv[2],'w')
manifest.write("sample-id,absolute-filepath,direction\n")
for f in listdir(sys.argv[1]):
    if "fastq"in str(f):
        name=str(f)
        id=name.split("_")[0]
        direction="forward"
        if "_2." in name:
            direction="reverse" 
        manifest.write(id+",$PWD/"+sys.argv[1]+"/"+name+","+direction+"\n")
        print(id)


manifest.close()
