import mysql.connector
from mysql.connector import errorcode

def handleDatabaseConnection():
	print("Trying to connect to the database...")
	try:
		connection = mysql.connector.connect (
			user = 'root',
			password = 'root',
			host = 'localhost',
			database = 'taskmanager'
		)
		print("Database connected!")
	except mysql.connector.Error as e:
		if (e.errno == errorcode.ER_ACCESS_DENIED_ERROR):
			print("Wrong user and/or password")
		elif (e.errno == errorcode.ER_BAD_DB_ERROR):
			print("Database doesn't exist")
		else:
			print(e)