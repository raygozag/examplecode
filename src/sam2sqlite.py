import csv
import sys
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
    
        return conn
    except Error as e:
        print(e)
    

def create_sam_table(db_conn):
    try:
        c = conn.cursor()
        c.execute("create table if not exists sam( qname varchar(250),flag INTEGER, rname varchar(250),pos INTEGER, mapq INTEGER, cigar varchar(500),rnext varhcra(500),pnext INTEGER, tlen INTEGER, seq varchar(500),qual varchar(500),other varchar(500))")
        c.execute("CREATE INDEX ref ON sam(rname)")
        c.execute("CREATE INDEX pos ON sam(pos)")
    except Error as e:
        print(e)




def insert_sam_record(conn,record):     
    try:   
        remaining="\t".join(record[11:])
        insert_st="insert into sam values('"+record[0]+"',"+record[1]+",'"+record[2]+"',"+record[3]+","+record[4]+",'"+record[5]+"','"+record[6]+"',"+record[7]+","+record[8]+",'"+record[9]+"','"+record[10]+"','"+remaining+"')"
        cur = conn.cursor()
        cur.execute(insert_st)
    except Error as e:
        print(e)

sam=csv.reader(open(sys.argv[1]),delimiter="\t")
conn=create_connection(sys.argv[2]+".sqlite")
create_sam_table(conn)
for record in sam:
    if len(record)<7:
        continue
    insert_sam_record(conn,record)
conn.commit()
conn.close()
