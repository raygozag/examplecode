import mysql.connector

try:

	cnx = mysql.connector.connect(user='root', password='hermosillo',host='localhost',port=3306)


	cursor.execute("show databases")


	for db in cursor:
		print db

	cnx.close()

except mysql.connector.Error as err:
	print err
