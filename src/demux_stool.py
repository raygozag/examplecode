import csv
import sys



data=csv.reader(open(sys.argv[1]),delimiter=',')

i=1
print("stool_id\tstool_date\tsubject_id\tnumber_samples\tsample_number")
for record in data:
    if i==1:
        i=2
        continue
        
    if record[7]=="0":
        continue
        
    dstool=record[6].strip().split("_")
    idstool=record[8].strip().split("_")
    #if len(idstool)==1:
        #print(idstool[0]+"\t"+dstool[0]+"\t"+record[0].strip()+"\t"+str(record[7]))
       # continue
    if len(dstool)==len(idstool):
        for k in range(0,len(idstool)):
            print(idstool[k]+"\t"+dstool[k]+"\t"+record[0].strip()+"\t"+str(record[7])+"\t"+str(k+1))
            
    else:
        if len(dstool)<len(idstool):
            for k in range(0,len(dstool)):
                print(idstool[k]+"\t"+dstool[k]+"\t"+record[0].strip()+"\t"+str(record[7])+"\t"+str(k+1))
        else:
            for k in range(0,len(idstool)):
                print(idstool[k]+"\t"+dstool[k]+"\t"+record[0].strip()+"\t"+str(record[7])+"\t"+str(k+1))