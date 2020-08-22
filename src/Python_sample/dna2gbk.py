import sys

def get_sequence(file):
    byte = f.read(1)
    seq=""
    printk=False
    while byte != "":
        byte = file.read(1)
        pos=ord(byte)
        
        if pos==2:
            break
        if printk==True:
            seq=seq+chr(ord(byte))
            
        if pos==31:
            printk=True
    return seq


def get_xml(file):
    byte = f.read(1)
    seq=""
    printk=False
    while byte != "":
        byte = file.read(1)
        pos=ord(byte)
        if pos==60:
            byte = file.read(1)
            pos=ord(byte)
            if pos==63:
                return("<?"+file.readline().strip())

f = open(sys.argv[1], "rb")

print(">"+sys.argv[1].split(".")[0])
try:
    seq=get_sequence(f)
    #print(seq)
    print(get_xml(f))
    print(get_xml(f))
finally:
    f.close()