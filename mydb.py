import mysql.connector

dataBase = mysql.connector.connect(
	 host = 'localhost',
	 user = 'root',
	 passwd = 'D@riu$F06152017!!'
	 
	 )

# prepare a cursor onject
cursorObject = dataBase.cursor()

# create a dataBase
cursorObject.execute ("CREATE DATABASE HWD")

print("All Done!")

